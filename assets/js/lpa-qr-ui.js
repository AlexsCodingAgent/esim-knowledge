/*!
 * lpa-qr-ui.js — wires the SGP.22 activation-code tool to the page.
 *
 * Zero network: this file contains no fetch/XHR/WebSocket/sendBeacon and never
 * loads a remote resource. Everything (QR encode, QR decode) happens in-page.
 */
(function () {
  'use strict';
  var Q = window.LpaQr;
  if (!Q) return;

  function $(id) { return document.getElementById(id); }
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  var last = { value: '', qr: null, svg: '' };

  /* ── messages ───────────────────────────────────────────────────────── */
  function renderMsgs(el, res) {
    if (!el) return;
    var html = '';
    (res.errors || []).forEach(function (e) {
      html += '<div class="lpa-msg err"><b>' + esc(e.code) + '</b> ' + esc(e.message) + '</div>';
    });
    (res.warnings || []).forEach(function (w) {
      html += '<div class="lpa-msg warn"><b>' + esc(w.code) + '</b> ' + esc(w.message) + '</div>';
    });
    if (!html) html = '<div class="lpa-msg ok">No problems found — conformant Activation Code.</div>';
    el.innerHTML = html;
  }

  /* ── build side ─────────────────────────────────────────────────────── */
  function fields() {
    return {
      address: ($('f-addr') || {}).value || '',
      matchingId: ($('f-token') || {}).value || '',
      oid: ($('f-oid') || {}).value || '',
      confirmationRequired: !!($('f-conf') && $('f-conf').checked),
      ciPublicKey: ($('f-ci') || {}).value || '',
      deleteNotification: ($('f-del') || {}).value || ''
    };
  }

  function rebuild() {
    var res = Q.build(fields());
    var ecl = ($('f-ecl') || {}).value || 'M';
    var strEl = $('lpa-str');
    var qrEl = $('qr-holder');

    last.value = res.value;
    last.svg = '';

    if (strEl) {
      strEl.innerHTML = highlight(res.value);
      strEl.setAttribute('data-empty', res.value === 'LPA:1$$' ? 'true' : 'false');
    }

    if (res.ok && qrEl) {
      try {
        var qr = Q.encodeMatrix(res.value, ecl);
        last.qr = qr;
        last.svg = Q.toSVG(qr, { scale: 7, quiet: 4 });
        qrEl.innerHTML = last.svg;
        var meta = $('qr-meta');
        if (meta) {
          meta.textContent = 'Version ' + ((qr.getModuleCount() - 17) / 4) + ' · ' +
            qr.getModuleCount() + '×' + qr.getModuleCount() + ' modules · EC ' + ecl + ' · ' +
            res.qrMode.toLowerCase() + ' mode · ' + res.value.length + ' chars';
        }
      } catch (e) {
        qrEl.innerHTML = '';
        if ($('qr-meta')) $('qr-meta').textContent = 'QR error: ' + e.message;
      }
    } else if (qrEl) {
      qrEl.innerHTML = '<div class="lpa-qr-empty">Fix the errors to generate a QR code</div>';
      if ($('qr-meta')) $('qr-meta').textContent = '';
    }

    renderMsgs($('build-msgs'), res);
    var dl = $('dl-wrap');
    if (dl) dl.style.display = res.ok ? '' : 'none';
    return res;
  }

  function highlight(value) {
    // "$" delimiters in purple, everything else plain — makes field boundaries visible.
    return String(value).split('$').map(function (p, i) {
      var sep = i === 0 ? '' : '<span class="lpa-dollar">$</span>';
      return sep + '<span class="lpa-part">' + esc(p) + '</span>';
    }).join('');
  }

  /* ── downloads ──────────────────────────────────────────────────────── */
  function dl(name, mime, data) {
    var blob = new Blob([data], { type: mime });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url; a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 1000);
  }

  function svgName() {
    var addr = (fields().address || 'activation-code').replace(/[^A-Za-z0-9.-]/g, '_');
    return 'lpa-' + addr + '.svg';
  }

  function downloadPng() {
    if (!last.qr) return;
    var n = last.qr.getModuleCount(), quiet = 4, scale = 10;
    var dim = (n + quiet * 2) * scale;
    var c = document.createElement('canvas');
    c.width = c.height = dim;
    var ctx = c.getContext('2d');
    ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, dim, dim);
    ctx.fillStyle = '#000';
    for (var r = 0; r < n; r++) {
      for (var col = 0; col < n; col++) {
        if (last.qr.isDark(r, col)) {
          ctx.fillRect((col + quiet) * scale, (r + quiet) * scale, scale, scale);
        }
      }
    }
    c.toBlob(function (b) {
      var url = URL.createObjectURL(b);
      var a = document.createElement('a');
      a.href = url; a.download = svgName().replace(/\.svg$/, '.png');
      document.body.appendChild(a); a.click();
      setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 1000);
    }, 'image/png');
  }

  /* ── decode side ────────────────────────────────────────────────────── */
  var FIELD_DOC = {
    acFormat: ['AC_Format', 'Must be "1" — any other value is invalid (SGP.22 §4.1).'],
    address: ['SM-DP+ Address', 'FQDN of the SM-DP+, ISO/IEC 18004 alphanumeric charset minus "$".'],
    matchingId: ['MatchingID (AC_Token)', 'Upper-case alphanumerics and "-"; MAY be zero-length.'],
    oid: ['SM-DP+ OID', 'Optional; the OID from CERT.DPauth.SIG.'],
    confirmationFlag: ['Confirmation Code Required', '"1" when the SM-DP+ requires a confirmation code, otherwise absent.'],
    ciPublicKey: ['CI Public Key indicator', 'Optional (v3.0+); selects an eSIM CA RootCA public key.'],
    deleteNotification: ['Delete Notification', 'Optional (v3.0+); only in a Device Change flow.'],
    ignored: ['Ignored trailing parameters', 'Beyond Table 8 — devices SHALL ignore these.']
  };

  function renderParsed(p, prefixNote) {
    var t = $('dec-fields');
    if (!t) return;
    var rows = '';
    Object.keys(FIELD_DOC).forEach(function (k) {
      var v = p[k];
      if (k === 'ignored') {
        if (!v || !v.length) return;
        v = v.join(' $ ');
      }
      var empty = (v === '' || v == null);
      rows += '<tr class="' + (empty ? 'lpa-empty' : '') + '">' +
        '<th>' + esc(FIELD_DOC[k][0]) + '</th>' +
        '<td><code>' + (empty ? '<span class="lpa-none">— empty —</span>' : esc(v)) + '</code></td>' +
        '<td class="lpa-doc">' + esc(FIELD_DOC[k][1]) + '</td></tr>';
    });
    t.innerHTML = rows;
    t.style.display = '';
    var extra = $('dec-extra');
    if (extra) {
      extra.innerHTML = 'QR mode required: <b>' + esc(p.qrMode) + '</b> · total ' +
        esc((p.value || '').length) + ' characters' + (prefixNote ? ' · ' + esc(prefixNote) : '');
    }
    renderMsgs($('dec-msgs'), p);
  }

  function decodeImage(file) {
    var img = new Image();
    var url = URL.createObjectURL(file);
    img.onload = function () {
      var c = $('dec-canvas');
      var max = 1200;
      var w = img.width, h = img.height;
      if (Math.max(w, h) > max) {
        var k = max / Math.max(w, h);
        w = Math.round(w * k); h = Math.round(h * k);
      }
      c.width = w; c.height = h;
      var ctx = c.getContext('2d', { willReadFrequently: true });
      ctx.drawImage(img, 0, 0, w, h);
      URL.revokeObjectURL(url);
      var data;
      try {
        data = ctx.getImageData(0, 0, w, h);
      } catch (e) {
        $('dec-msgs').innerHTML = '<div class="lpa-msg err">Cannot read that image in this browser.</div>';
        return;
      }
      var found = null;
      try { found = window.jsQR(data.data, w, h, { inversionAttempts: 'attemptBoth' }); } catch (e) { found = null; }
      if (!found) {
        $('dec-fields').style.display = 'none';
        $('dec-msgs').innerHTML = '<div class="lpa-msg err">No QR code found in that image. Try a tighter crop, more contrast, or a larger image.</div>';
        return;
      }
      var p = Q.parse(found.data);
      renderParsed(p, 'decoded from image');
    };
    img.onerror = function () {
      $('dec-msgs').innerHTML = '<div class="lpa-msg err">That file could not be read as an image.</div>';
    };
    img.src = url;
  }

  function decodeText(str) {
    if (!str.trim()) {
      $('dec-fields').style.display = 'none';
      $('dec-msgs').innerHTML = '';
      return;
    }
    renderParsed(Q.parse(str), 'parsed from text');
  }

  /* ── wiring ─────────────────────────────────────────────────────────── */
  function init() {
    ['f-addr', 'f-token', 'f-oid', 'f-ci', 'f-del'].forEach(function (id) {
      var el = $(id); if (el) el.addEventListener('input', rebuild);
    });
    ['f-conf', 'f-ecl'].forEach(function (id) {
      var el = $(id); if (el) el.addEventListener('change', rebuild);
    });

    var copy = $('copy-btn');
    if (copy) {
      copy.addEventListener('click', function () {
        var txt = last.value;
        function done() {
          copy.textContent = 'Copied';
          setTimeout(function () { copy.textContent = 'Copy'; }, 1400);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(txt).then(done, function () { fallbackCopy(txt); done(); });
        } else { fallbackCopy(txt); done(); }
      });
    }

    var svgBtn = $('dl-svg'), pngBtn = $('dl-png');
    if (svgBtn) svgBtn.addEventListener('click', function () { if (last.svg) dl(svgName(), 'image/svg+xml', last.svg); });
    if (pngBtn) pngBtn.addEventListener('click', downloadPng);

    // tabs
    var tabs = document.querySelectorAll('.lpa-tab');
    Array.prototype.forEach.call(tabs, function (t) {
      t.addEventListener('click', function () {
        Array.prototype.forEach.call(tabs, function (x) {
          x.classList.toggle('active', x === t);
          x.setAttribute('aria-selected', x === t ? 'true' : 'false');
        });
        var want = t.getAttribute('data-tab');
        ['build', 'decode'].forEach(function (name) {
          var sec = $('tab-' + name);
          if (sec) sec.hidden = (name !== want);
        });
      });
    });

    // decode inputs
    var file = $('qr-file');
    if (file) {
      file.addEventListener('change', function () { if (file.files && file.files[0]) decodeImage(file.files[0]); });
    }
    var paste = $('paste');
    if (paste) {
      paste.addEventListener('input', function () { decodeText(paste.value); });
    }
    var drop = $('drop');
    if (drop) {
      ['dragenter', 'dragover'].forEach(function (ev) {
        drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); });
      });
      ['dragleave', 'drop'].forEach(function (ev) {
        drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); });
      });
      drop.addEventListener('drop', function (e) {
        var f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
        if (f && /^image\//.test(f.type)) decodeImage(f);
      });
      // click the drop zone to open the file picker
      drop.addEventListener('click', function () { if (file) file.click(); });
    }

    // paste an image straight in (ctrl+V anywhere on the decode tab)
    document.addEventListener('paste', function (e) {
      var sec = $('tab-decode');
      if (!sec || sec.hidden) return;
      var items = (e.clipboardData && e.clipboardData.items) || [];
      for (var i = 0; i < items.length; i++) {
        if (items[i].type && items[i].type.indexOf('image') === 0) {
          var f = items[i].getAsFile();
          if (f) { decodeImage(f); e.preventDefault(); return; }
        }
      }
    });

    // pre-fill with the spec's own example so the page shows something real
    if ($('f-addr') && !$('f-addr').value) {
      $('f-addr').value = 'SMDP.EXAMPLE.COM';
      $('f-token').value = '04386-AGYFT-A74Y8-3F815';
    }
    rebuild();
  }

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.top = '-1000px';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) { /* ignore */ }
    ta.remove();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
}());
