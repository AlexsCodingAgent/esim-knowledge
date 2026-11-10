/*!
 * lpa-qr-ui.js: the whole tool. One input, one QR, one field table.
 *
 * Zero network: no fetch/XHR/WebSocket/sendBeacon, no remote resources.
 * Encode and decode both happen in this tab.
 */
(function () {
  'use strict';
  var Q = window.LpaQr;
  if (!Q) return;

  var $ = function (id) { return document.getElementById(id); };
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  var last = { value: '', svg: '', qr: null, ec: 'M' };

  /* ── the one input drives everything ────────────────────────────────── */
  function update(str) {
    var p = Q.parse(str);
    last.value = p.value || '';
    last.svg = '';
    last.qr = null;

    var qrBox = $('qr');
    if (p.ok) {
      try {
        last.ec = Q.pickEc(p.value);
        last.qr = Q.encodeMatrix(p.value, last.ec);
        last.svg = Q.toSVG(last.qr, {
          scale: 8,
          quiet: 4,
          label: 'QR code for activation code on ' + (p.address || 'the SM-DP+')
        });
        qrBox.innerHTML = last.svg;
        qrBox.classList.add('can-zoom');
        qrBox.setAttribute('role', 'button');
        qrBox.setAttribute('tabindex', '0');
        qrBox.setAttribute('aria-label', 'Enlarge the QR code');
        qrBox.setAttribute('aria-expanded', zoomOpen ? 'true' : 'false');
        if (zoomOpen) renderZoom();
      } catch (e) {
        qrBox.innerHTML = '<div class="none">' + esc(e.message) + '</div>';
      }
    } else {
      qrBox.innerHTML = '<div class="none">' + (str.trim() ? 'Not a valid code' : 'QR appears here') + '</div>';
      qrBox.classList.remove('can-zoom');
      qrBox.removeAttribute('role');
      qrBox.removeAttribute('tabindex');
      qrBox.removeAttribute('aria-label');
      qrBox.removeAttribute('aria-expanded');
      closeZoom();
    }

    renderFields(p, str.trim() !== '');
    renderMsgs(p, str.trim() !== '');
    var meta = $('meta');
    if (meta) {
      if (p.ok) {
        meta.innerHTML =
          '<span>Version ' + Q.version(last.qr) + ' · ' + p.value.length + ' characters</span>' +
          '<span>' + p.qrMode + ' mode · EC ' + last.ec + '</span>';
      } else {
        meta.textContent = '';
      }
    }
    ['dl', 'dlpng'].forEach(function (id) {
      var b = $(id);
      if (b) b.disabled = !p.ok;
    });
  }

  /* ── field table: mandatory rows always, optional rows only when set ── */
  var ROWS = [
    ['acFormat', 'AC_Format', true],
    ['address', 'SM-DP+ address', true],
    ['matchingId', 'MatchingID', true],
    ['oid', 'SM-DP+ OID', false],
    ['confirmationFlag', 'Confirmation code', false],
    ['ciPublicKey', 'CI public key', false],
    ['deleteNotification', 'Delete notification', false]
  ];

  function renderFields(p, touched) {
    var t = $('fields');
    if (!touched) { t.innerHTML = ''; t.hidden = true; return; }
    var html = '';
    ROWS.forEach(function (r) {
      var v = p[r[0]];
      if (!r[2] && (v === '' || v == null)) return;
      if (r[0] === 'confirmationFlag' && v === '1') v = 'required';
      html += '<tr><th>' + esc(r[1]) + '</th><td>' +
        (v === '' || v == null ? '<span class="none">(empty)</span>' : '<code>' + esc(v) + '</code>') +
        '</td></tr>';
    });
    if (p.ignored && p.ignored.length) {
      html += '<tr><th>Ignored</th><td><code>' + esc(p.ignored.join(' $ ')) + '</code></td></tr>';
    }
    t.innerHTML = html;
    t.hidden = false;
  }

  function renderMsgs(p, touched) {
    var el = $('msgs');
    if (!touched) { el.innerHTML = ''; return; }
    var html = '';
    p.errors.forEach(function (e) { html += '<div class="msg err">' + esc(e.message) + '</div>'; });
    p.warnings.forEach(function (w) { html += '<div class="msg warn">' + esc(w.message) + '</div>'; });
    if (!html) html = '<div class="msg ok">Valid. Conformant activation code.</div>';
    el.innerHTML = html;
  }

  /* ── decode an image dropped / pasted / chosen ──────────────────────── */
  function decodeImage(file) {
    var img = new Image();
    var url = URL.createObjectURL(file);
    img.onload = function () {
      var max = 1400, w = img.width, h = img.height;
      if (Math.max(w, h) > max) {
        var k = max / Math.max(w, h);
        w = Math.round(w * k); h = Math.round(h * k);
      }
      var c = document.createElement('canvas');
      c.width = w; c.height = h;
      var ctx = c.getContext('2d', { willReadFrequently: true });
      ctx.drawImage(img, 0, 0, w, h);
      URL.revokeObjectURL(url);
      var hit = null;
      try { hit = window.jsQR(ctx.getImageData(0, 0, w, h).data, w, h, { inversionAttempts: 'attemptBoth' }); }
      catch (e) { hit = null; }
      if (!hit) {
        $('msgs').innerHTML = '<div class="msg err">No QR code found in that image. Try a tighter crop or a sharper photo.</div>';
        return;
      }
      var input = $('input');
      input.value = hit.data;
      update(hit.data);
    };
    img.onerror = function () {
      $('msgs').innerHTML = '<div class="msg err">That file is not a readable image.</div>';
    };
    img.src = url;
  }

  /* ── textarea grows to fit the code, up to a cap ────────────────────── */
  function autoGrow() {
    var ta = $('input');
    if (!ta) return;
    var max = 200;
    ta.style.height = 'auto';
    ta.style.height = Math.min(ta.scrollHeight, max) + 'px';
    ta.style.overflowY = ta.scrollHeight > max ? 'auto' : 'hidden';
  }

  /* ── the six Table 8 cases, one click each ──────────────────────────── */
  var EXAMPLES = [
    ['basic', 'LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815'],
    ['confirmation code', 'LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815$$1'],
    ['OID + flag', 'LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815$1.3.6.1.4.1.31746$1'],
    ['no MatchingID', 'LPA:1$SMDP.EXAMPLE.COM$$1.3.6.1.4.1.31746'],
    ['CI public key', 'LPA:1$SMDP.EXAMPLE.NET$KL14XA-8C7RLY$1.3.6.1.4.1.31746$$A14D8-971']
  ];

  function buildExamples() {
    var host = $('examples');
    if (!host) return;
    EXAMPLES.forEach(function (ex) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'lpa-chip';
      b.textContent = ex[0];
      b.title = ex[1];
      b.addEventListener('click', function () {
        var ta = $('input');
        ta.value = ex[1];
        ta.focus();
        update(ex[1]);
        autoGrow();
      });
      host.appendChild(b);
    });
  }

  /* ── enlarge: scanning a 240px symbol off a laptop screen is a lottery ─ */
  var zoomOpen = false;

  function renderZoom() {
    var slot = $('zoom-qr');
    if (slot) slot.innerHTML = last.svg;
  }

  function openZoom() {
    if (!last.svg) return;
    var z = $('zoom');
    if (!z) return;
    zoomOpen = true;
    renderZoom();
    z.classList.add('open');
    z.setAttribute('aria-hidden', 'false');
    var box = $('qr');
    if (box) box.setAttribute('aria-expanded', 'true');
  }

  function closeZoom() {
    var z = $('zoom');
    zoomOpen = false;
    if (!z) return;
    z.classList.remove('open');
    z.setAttribute('aria-hidden', 'true');
    var box = $('qr');
    if (box && box.getAttribute('role') === 'button') box.setAttribute('aria-expanded', 'false');
  }

  /* ── wiring ─────────────────────────────────────────────────────────── */
  function init() {
    var input = $('input');

    input.addEventListener('input', function () { update(input.value); autoGrow(); });

    // enlarge the symbol in place, for scanning off the screen
    var qrBox = $('qr');
    if (qrBox) {
      qrBox.addEventListener('click', openZoom);
      qrBox.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openZoom(); }
      });
    }
    var zoom = $('zoom');
    if (zoom) zoom.addEventListener('click', closeZoom);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && zoomOpen) closeZoom();
    });

    var copy = $('copy');
    copy.addEventListener('click', function () {
      if (!last.value) return;
      var done = function () {
        copy.textContent = 'Copied';
        setTimeout(function () { copy.textContent = 'Copy'; }, 1200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(last.value).then(done, function () { legacyCopy(last.value); done(); });
      } else { legacyCopy(last.value); done(); }
    });

    // explicit affordance for the reverse direction: pick a file
    var pick = $('pick'), file = $('file');
    if (pick && file) {
      pick.addEventListener('click', function () { file.click(); });
      file.addEventListener('change', function () {
        if (file.files && file.files[0]) decodeImage(file.files[0]);
        file.value = '';
      });
    }

    $('dl').addEventListener('click', function () {
      if (!last.svg) return;
      saveBlob(new Blob([last.svg], { type: 'image/svg+xml' }), fileName('svg'));
    });

    // PNG matters more than SVG in practice: a phone gallery, a chat app or a
    // ticket system will not take an SVG, and 1024px keeps the modules whole.
    $('dlpng').addEventListener('click', function () {
      if (!last.qr) return;
      try {
        var canvas = Q.toCanvas(last.qr, { px: 1024, quiet: 4 });
        if (canvas.toBlob) {
          canvas.toBlob(function (blob) { if (blob) saveBlob(blob, fileName('png')); }, 'image/png');
        } else {
          saveBlob(dataUrlToBlob(canvas.toDataURL('image/png')), fileName('png'));
        }
      } catch (e) {
        $('msgs').innerHTML = '<div class="msg err">' + esc(e.message) + '</div>';
      }
    });

    // whole page is a drop target for QR images
    ['dragenter', 'dragover'].forEach(function (ev) {
      document.addEventListener(ev, function (e) { e.preventDefault(); document.body.classList.add('dropping'); });
    });
    ['dragleave', 'drop'].forEach(function (ev) {
      document.addEventListener(ev, function (e) { e.preventDefault(); document.body.classList.remove('dropping'); });
    });
    document.addEventListener('drop', function (e) {
      var f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
      if (f && /^image\//.test(f.type)) decodeImage(f);
    });

    // paste: an image decodes, text just lands in the box
    document.addEventListener('paste', function (e) {
      var items = (e.clipboardData && e.clipboardData.items) || [];
      for (var i = 0; i < items.length; i++) {
        if (items[i].type && items[i].type.indexOf('image') === 0) {
          var f = items[i].getAsFile();
          if (f) { decodeImage(f); e.preventDefault(); return; }
        }
      }
    });

    if (!input.value) input.value = 'LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815';
    buildExamples();
    update(input.value);
    autoGrow();
  }

  function legacyCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.top = '-1000px';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); } catch (e) { /* ignore */ }
    ta.remove();
  }

  /* ── file naming / saving ───────────────────────────────────────────── */
  function fileName(ext) {
    var p = Q.parse(($('input') || {}).value || '');
    var addr = (p.address || 'code').replace(/[^A-Za-z0-9.-]/g, '_').slice(0, 60);
    return 'lpa-' + addr + '.' + ext;
  }

  function saveBlob(blob, name) {
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = name;
    a.rel = 'noopener';
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 800);
  }

  function dataUrlToBlob(dataUrl) {
    var parts = dataUrl.split(',');
    var mime = /:(.*?);/.exec(parts[0])[1];
    var bin = atob(parts[1]);
    var bytes = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    return new Blob([bytes], { type: mime });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
