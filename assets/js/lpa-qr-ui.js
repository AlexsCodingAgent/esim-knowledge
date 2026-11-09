/*!
 * lpa-qr-ui.js — the whole tool: one input, one QR, one field table.
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

  var last = { value: '', svg: '', qr: null };

  /* ── the one input drives everything ────────────────────────────────── */
  function update(str) {
    var p = Q.parse(str);
    last.value = p.value || '';
    last.svg = '';
    last.qr = null;

    var qrBox = $('qr');
    if (p.ok) {
      try {
        last.qr = Q.encodeMatrix(p.value, 'M');
        last.svg = Q.toSVG(last.qr, { scale: 7, quiet: 4 });
        qrBox.innerHTML = last.svg;
      } catch (e) {
        qrBox.innerHTML = '<div class="none">' + esc(e.message) + '</div>';
      }
    } else {
      qrBox.innerHTML = '<div class="none">' + (str.trim() ? 'Not a valid code' : 'QR appears here') + '</div>';
    }

    renderFields(p, str.trim() !== '');
    renderMsgs(p, str.trim() !== '');
    var meta = $('meta');
    if (meta) {
      meta.textContent = p.ok
        ? 'Version ' + ((last.qr.getModuleCount() - 17) / 4) + ' · ' + p.value.length +
          ' characters · ' + p.qrMode.toLowerCase() + ' mode · EC M'
        : '';
    }
    var dl = $('dl');
    if (dl) dl.disabled = !p.ok;
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
        (v === '' || v == null ? '<span class="none">— empty —</span>' : '<code>' + esc(v) + '</code>') +
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
    if (!html) html = '<div class="msg ok">Valid — conformant activation code.</div>';
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
        $('msgs').innerHTML = '<div class="msg err">No QR code found in that image — try a tighter crop or a sharper photo.</div>';
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

  /* ── wiring ─────────────────────────────────────────────────────────── */
  function init() {
    var input = $('input');

    input.addEventListener('input', function () { update(input.value); });

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

    $('dl').addEventListener('click', function () {
      if (!last.svg) return;
      var blob = new Blob([last.svg], { type: 'image/svg+xml' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'lpa-' + (Q.parse(input.value).address || 'code').replace(/[^A-Za-z0-9.-]/g, '_') + '.svg';
      document.body.appendChild(a); a.click();
      setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 800);
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
    update(input.value);
  }

  function legacyCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.top = '-1000px';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); } catch (e) { /* ignore */ }
    ta.remove();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
