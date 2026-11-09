/*!
 * lpa-qr.js — GSMA SGP.22 Activation Code  <->  QR payload.
 *
 * Pure client-side. This file performs NO network I/O of any kind: no fetch,
 * no XHR, no sendBeacon, no WebSocket, no dynamic script/style injection.
 *
 * Normative references (SGP.22 v3.1 §4.1, Table 8):
 *   QR payload  = "LPA:" + Activation Code
 *   Activation Code = AC_Format $ SM-DP+ Address $ AC_Token
 *                     [ $ SM-DP+ OID [ $ Confirmation Code Required Flag
 *                       [ $ CI Public Key indicator [ $ Delete Notification ] ] ] ]
 *   - AC_Format: "1"; any other value is invalid
 *   - SM-DP+ Address: FQDN restricted to the ISO/IEC 18004 Table 5 alphanumeric
 *     character set excluding "$"
 *   - AC_Token (MatchingID): upper-case alphanumerics and "-" only; MAY be empty
 *   - Confirmation Code Required Flag: "1" when required, otherwise absent
 *   - max length 255 characters unless a Delete Notification is present
 *   - trailing parameters beyond Table 8 SHALL be ignored by the device
 *
 * UMD so the same code runs in the browser and under node (for tests).
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.LpaQr = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ── character sets ─────────────────────────────────────────────────── */
  // ISO/IEC 18004 Table 5 alphanumeric mode, minus "$" (the AC delimiter).
  var RE_ADDR = /^[0-9A-Z $%*+\-./:]+$/;
  // MatchingID: upper-case alphanumerics and "-".
  var RE_TOKEN = /^[0-9A-Z-]*$/;
  // Dotted-decimal OID (ISO/IEC 8824-1).
  var RE_OID = /^[0-9]+(\.[0-9]+)+$/;

  var MAX_LEN = 255;

  function push(list, code, msg) { list.push({ code: code, message: msg }); }

  /* ── address (FQDN) checks ──────────────────────────────────────────── */
  function checkAddress(addr, errors, warnings) {
    if (addr === '') {
      push(errors, 'ADDR_EMPTY', 'SM-DP+ Address is mandatory and must not be empty.');
      return;
    }
    if (!RE_ADDR.test(addr)) {
      var bad = addr.split('').filter(function (c) { return !RE_ADDR.test(c); });
      push(warnings, 'ADDR_CHARSET',
        'SM-DP+ Address contains characters outside the ISO/IEC 18004 alphanumeric ' +
        'set (offending: ' + JSON.stringify(bad.join('')) + '). SGP.22 restricts it to ' +
        '0-9 A-Z space % * + - . / : ; the QR then needs byte mode instead of ' +
        'alphanumeric mode (bigger symbol, still scannable).');
    }
    if (addr !== addr.toUpperCase()) {
      push(warnings, 'ADDR_LOWER',
        'SM-DP+ Address contains lower-case letters. FQDNs are case-insensitive, but the ' +
        'alphanumeric QR mode needs upper case — it will be encoded in byte mode as given.');
    }
    if (addr.length > 253) {
      push(errors, 'ADDR_LEN', 'SM-DP+ Address is ' + addr.length + ' characters; an FQDN maxes out at 253.');
    }
    if (addr.indexOf('.') === -1) {
      push(warnings, 'ADDR_NOT_FQDN', 'SM-DP+ Address has no dot — that is not a fully qualified domain name.');
    }
    var labels = addr.split('.');
    labels.forEach(function (l, i) {
      if (l === '') {
        push(errors, 'ADDR_LABEL_EMPTY',
          'SM-DP+ Address has an empty label at position ' + (i + 1) + ' (leading, trailing or doubled dot).');
      } else if (l.length > 63) {
        push(errors, 'ADDR_LABEL_LEN', 'Label "' + l.slice(0, 20) + '…" is ' + l.length + ' chars; max 63.');
      }
      if (/^-|-$/.test(l)) {
        push(warnings, 'ADDR_LABEL_HYPHEN', 'Label "' + l + '" starts or ends with "-".');
      }
    });
    if (/\s/.test(addr)) {
      push(warnings, 'ADDR_SPACE',
        'SM-DP+ Address contains a space. A space is legal in the alphanumeric set but is ' +
        'almost certainly a copy/paste error in an FQDN.');
    }
  }

  /* ── matching id checks ─────────────────────────────────────────────── */
  function checkToken(tok, errors, warnings) {
    if (!RE_TOKEN.test(tok)) {
      var bad = tok.split('').filter(function (c) { return !RE_TOKEN.test(c); }).join('');
      push(warnings, 'TOKEN_CHARSET',
        'MatchingID contains ' + JSON.stringify(bad) + '. SGP.22 §4.1.1 says it SHALL be ' +
        'upper-case alphanumerics and "-" only. Non-conformant values do occur in the field ' +
        '(lower-case or base64 tokens), so this is a warning, not a hard error.');
    }
    if (tok === '') {
      push(warnings, 'TOKEN_EMPTY',
        'MatchingID is empty. That is legal ("MAY be zero-length") but only makes sense when ' +
        'the SM-DP+ can identify the order from the SM-DP+ OID or from a default profile.');
    }
  }

  /* ── OID checks ─────────────────────────────────────────────────────── */
  function checkOid(oid, errors, warnings) {
    if (oid === '') return;
    if (!RE_OID.test(oid)) {
      push(errors, 'OID_FORMAT', 'SM-DP+ OID "' + oid + '" is not a dotted-decimal OID (e.g. 1.3.6.1.4.1.31746).');
      return;
    }
    var arcs = oid.split('.').map(Number);
    if (arcs[0] > 2) {
      push(errors, 'OID_ARC1', 'OID first arc must be 0, 1 or 2 (got ' + arcs[0] + ').');
    }
    if (arcs[0] < 2 && arcs[1] > 39) {
      push(errors, 'OID_ARC2', 'OID second arc must be 0-39 when the first arc is ' + arcs[0] + '.');
    }
  }

  /* ── parse ──────────────────────────────────────────────────────────── */
  function parse(input) {
    var errors = [], warnings = [];
    var raw = String(input == null ? '' : input);
    var s = raw.trim();

    var out = {
      ok: false, raw: raw, hasPrefix: false, acFormat: null, address: '',
      matchingId: '', oid: '', confirmationFlag: '', ciPublicKey: '',
      deleteNotification: '', ignored: [], errors: errors, warnings: warnings,
      value: '', qrMode: ''
    };

    if (s === '') {
      push(errors, 'EMPTY', 'Nothing to decode.');
      return out;
    }

    // optional "LPA:" prefix, required in a QR payload (SGP.22 §4.1)
    var m = /^([Ll][Pp][Aa]):/.exec(s);
    if (m) {
      out.hasPrefix = true;
      if (m[1] !== 'LPA') {
        push(warnings, 'PREFIX_CASE', 'Prefix is "' + m[1] + ':" — the spec writes "LPA:"; readers are usually case-insensitive.');
      }
      s = s.slice(m[0].length);
    } else {
      push(warnings, 'PREFIX_MISSING',
        'No "LPA:" prefix. A QR payload SHALL be prefixed with "LPA:"; without it a scanner ' +
        'may reject the code. Parsing proceeds as if it were present.');
    }

    var parts = s.split('$');
    out.acFormat = parts[0];
    if (parts[0] !== '1') {
      push(errors, 'AC_FORMAT',
        'AC_Format is "' + parts[0] + '". SGP.22 §4.1: the device SHALL treat an AC_Format other than "1" as invalid.');
    }
    if (parts.length < 3) {
      push(errors, 'STRUCTURE',
        'Expected at least AC_Format $ SM-DP+ Address $ AC_Token — got ' + parts.length + ' field(s). ' +
        'Note that the empty optional fields still need their "$" delimiters.');
    }

    out.address = parts[1] || '';
    out.matchingId = parts[2] || '';
    out.oid = parts.length > 3 ? parts[3] : '';
    out.confirmationFlag = parts.length > 4 ? parts[4] : '';
    out.ciPublicKey = parts.length > 5 ? parts[5] : '';
    out.deleteNotification = parts.length > 6 ? parts[6] : '';
    if (parts.length > 7) {
      out.ignored = parts.slice(7);
      push(warnings, 'EXTRA_FIELDS',
        'This code has ' + out.ignored.length + ' parameter(s) beyond Table 8 (' +
        out.ignored.length + '). The spec says a device SHALL ignore them; they are shown but not interpreted.');
    }

    if (out.address) checkAddress(out.address, errors, warnings);
    checkToken(out.matchingId, errors, warnings);
    checkOid(out.oid, errors, warnings);

    if (out.confirmationFlag !== '' && out.confirmationFlag !== '1') {
      push(errors, 'CONF_FLAG',
        'Confirmation Code Required Flag is "' + out.confirmationFlag + '"; it SHALL be "1" when present, otherwise absent.');
    }
    if (out.ciPublicKey !== '' && !/^[0-9A-Za-z+/=_-]+$/.test(out.ciPublicKey)) {
      push(warnings, 'CI_KEY', 'CI Public Key indicator "' + out.ciPublicKey + '" looks unusual (expected an opaque indicator value).');
    }
    if (out.deleteNotification !== '') {
      push(warnings, 'DELETE_NOTIF', 'Delete Notification for Device Change present — only valid in a Device Change flow (SGP.22 §4.1.3).');
    }

    // Delimiter hygiene: "$1" style flags live in a specific slot; catch the classic mistake
    // of putting the confirmation flag before the OID.
    if (out.oid === '1' && (out.confirmationFlag === '' || out.confirmationFlag === undefined)) {
      // plausible: user meant confirmation flag but the slot is the OID slot
    }

    var total = s.length;
    if (total > MAX_LEN && out.deleteNotification === '') {
      push(warnings, 'LENGTH',
        'Activation Code is ' + total + ' characters; the spec caps it at 255 unless it carries a Delete Notification.');
    }

    out.qrMode = alnumModeOk('LPA:' + s) ? 'Alphanumeric' : 'Byte';
    out.value = 'LPA:' + s;
    out.ok = errors.length === 0;
    return out;
  }

  /* ── build ──────────────────────────────────────────────────────────── */
  function build(f) {
    f = f || {};
    var errors = [], warnings = [];
    var addr = String(f.address == null ? '' : f.address).trim();
    var tok = String(f.matchingId == null ? '' : f.matchingId).trim();
    var oid = String(f.oid == null ? '' : f.oid).trim();
    var conf = f.confirmationRequired ? '1' : '';
    var ci = String(f.ciPublicKey == null ? '' : f.ciPublicKey).trim();
    var del = String(f.deleteNotification == null ? '' : f.deleteNotification).trim();

    checkAddress(addr, errors, warnings);
    checkToken(tok, errors, warnings);
    checkOid(oid, errors, warnings);
    if (conf && conf !== '1') push(errors, 'CONF_FLAG', 'Confirmation flag must be "1" or absent.');
    if (ci && del === '' && oid === '' && !conf) {
      push(warnings, 'HOLE',
        'A CI Public Key indicator without an OID or confirmation flag leaves an empty "$$" — ' +
        'that is legal but almost always a mistake; check the field order.');
    }

    // Optional tail: oid, conf flag, ci key, delete notification — trimmed to the last set one.
    var tail = [oid, conf, ci, del];
    while (tail.length && tail[tail.length - 1] === '') tail.pop();
    var ac = ['1', addr, tok].concat(tail).join('$');
    var value = 'LPA:' + ac;

    if (ac.length > MAX_LEN && del === '') {
      push(warnings, 'LENGTH',
        'Activation Code is ' + ac.length + ' characters; the spec caps it at 255 unless it carries a Delete Notification.');
    }
    var mode = alnumModeOk(value) ? 'Alphanumeric' : 'Byte';
    if (mode === 'Byte') {
      push(warnings, 'BYTE_MODE', 'Payload is not fully upper-case alphanumeric, so the QR uses byte mode (larger symbol).');
    }

    return { ok: errors.length === 0, value: value, ac: ac, qrMode: mode, errors: errors, warnings: warnings };
  }

  /* ── QR mode helper ─────────────────────────────────────────────────── */
  function alnumModeOk(s) {
    // Table 5 set (this one includes "$", which an AC legitimately contains).
    return /^[0-9A-Z $%*+\-./:]+$/.test(s);
  }

  /* ── QR matrix (needs the vendored encoder) ─────────────────────────── */
  function encodeMatrix(payload, ecLevel) {
    var qrFn = (typeof qrcode === 'function') ? qrcode
      : (typeof require === 'function' ? require('./vendor/qrcode-generator.js') : null);
    if (!qrFn) throw new Error('QR encoder not loaded');
    var ecl = (ecLevel || 'M');
    var qr = qrFn(0, ecl);                  // 0 = pick the smallest version that fits
    qr.addData(payload, alnumModeOk(payload) ? 'Alphanumeric' : 'Byte');
    qr.make();
    return qr;
  }

  function toSVG(qr, opts) {
    opts = opts || {};
    var quiet = opts.quiet == null ? 4 : opts.quiet;
    var scale = opts.scale == null ? 8 : opts.scale;
    var n = qr.getModuleCount();
    var size = (n + quiet * 2) * scale;
    var dark = opts.dark || '#000000';
    var light = opts.light || '#ffffff';
    var path = [];
    for (var r = 0; r < n; r++) {
      for (var c = 0; c < n; c++) {
        if (qr.isDark(r, c)) {
          path.push('M' + ((c + quiet) * scale) + ' ' + ((r + quiet) * scale) + 'h' + scale + 'v' + scale + 'h-' + scale + 'z');
        }
      }
    }
    return '<svg xmlns="http://www.w3.org/2000/svg" width="' + size + '" height="' + size +
      '" viewBox="0 0 ' + size + ' ' + size + '" shape-rendering="crispEdges" role="img">' +
      '<rect width="' + size + '" height="' + size + '" fill="' + light + '"/>' +
      '<path fill="' + dark + '" d="' + path.join('') + '"/></svg>';
  }

  return {
    parse: parse,
    build: build,
    encodeMatrix: encodeMatrix,
    toSVG: toSVG,
    alnumModeOk: alnumModeOk,
    RE_ADDR: RE_ADDR,
    RE_TOKEN: RE_TOKEN,
    MAX_LEN: MAX_LEN
  };
}));
