#!/usr/bin/env node
/**
 * Tests for assets/js/lpa-qr.js. Run: node scripts/test_lpa_qr.js
 *
 * Covers: the six normative examples from SGP.22 v3.1 Table 8, build<->parse
 * round trips, conformance warnings, and a real encode -> rasterise -> jsQR
 * decode round trip (no browser needed).
 */
'use strict';
const path = require('path');
const LpaQr = require(path.join(__dirname, '..', 'assets', 'js', 'lpa-qr.js'));
const jsQR = require(path.join(__dirname, '..', 'assets', 'js', 'vendor', 'jsQR.js'));

let pass = 0, fail = 0;
function check(name, cond, detail) {
  if (cond) { pass++; console.log('  ok   ' + name); }
  else { fail++; console.log('  FAIL ' + name + (detail ? '\n         ' + detail : '')); }
}
function codes(list) { return list.map(x => x.code).join(','); }

/* ── 1. normative examples (SGP.22 v3.1 §4.1 examples) ─────────────────── */
const SPEC = [
  ['LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815',
    { oid: '', conf: '', ci: '' }],
  ['LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815$$1',
    { oid: '', conf: '1', ci: '' }],
  ['LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815$1.3.6.1.4.1.31746$1',
    { oid: '1.3.6.1.4.1.31746', conf: '1', ci: '' }],
  ['LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815$1.3.6.1.4.1.31746',
    { oid: '1.3.6.1.4.1.31746', conf: '', ci: '' }],
  ['LPA:1$SMDP.EXAMPLE.COM$$1.3.6.1.4.1.31746',
    { oid: '1.3.6.1.4.1.31746', conf: '', ci: '', token: '' }],
  ['LPA:1$SMDP.EXAMPLE.NET$KL14XA-8C7RLY$1.3.6.1.4.1.31746$$A14D8-971',
    { oid: '1.3.6.1.4.1.31746', conf: '', ci: 'A14D8-971' }],
];

console.log('\n1. SGP.22 Table 8 examples');
SPEC.forEach(([str, want], i) => {
  const r = LpaQr.parse(str);
  check('example ' + (i + 1) + ' parses clean', r.ok, 'errors: ' + codes(r.errors) + ' ' + JSON.stringify(r.errors));
  check('example ' + (i + 1) + ' fields', r.oid === want.oid && r.confirmationFlag === want.conf &&
        r.ciPublicKey === want.ci && r.hasPrefix === true &&
        (want.token === undefined || r.matchingId === want.token),
        `got oid=${r.oid} conf=${r.confirmationFlag} ci=${r.ciPublicKey} tok=${r.matchingId}`);
  check('example ' + (i + 1) + ' alphanumeric mode', r.qrMode === 'Alphanumeric', 'mode=' + r.qrMode);
});

/* ── 2. build -> parse round trip ──────────────────────────────────────── */
console.log('\n2. build -> parse round trip');
const BUILDS = [
  { address: 'SMDP.EXAMPLE.COM', matchingId: '04386-AGYFT-A74Y8-3F815' },
  { address: 'SMDP.EXAMPLE.COM', matchingId: '04386-AGYFT-A74Y8-3F815', confirmationRequired: true },
  { address: 'smdp.example.com', matchingId: 'abc123', oid: '1.3.6.1.4.1.31746', confirmationRequired: true },
  { address: 'SMDP.EXAMPLE.COM', matchingId: '', oid: '1.3.6.1.4.1.31746' },
  { address: 'SMDP.EXAMPLE.NET', matchingId: 'KL14XA-8C7RLY', oid: '1.3.6.1.4.1.31746', ciPublicKey: 'A14D8-971' },
  { address: 'LPA.EXAMPLE.COM', matchingId: 'X1', deleteNotification: 'A14D8-971' },
];
BUILDS.forEach((f, i) => {
  const b = LpaQr.build(f);
  const p = LpaQr.parse(b.value);
  check('build ' + (i + 1) + ' ok', b.ok, codes(b.errors));
  check('build ' + (i + 1) + ' round-trips', p.ok &&
        p.address === f.address &&
        p.matchingId === (f.matchingId || '') &&
        p.oid === (f.oid || '') &&
        p.confirmationFlag === (f.confirmationRequired ? '1' : '') &&
        p.ciPublicKey === (f.ciPublicKey || '') &&
        p.deleteNotification === (f.deleteNotification || ''),
        `built ${b.value} -> ${JSON.stringify({ a: p.address, t: p.matchingId, o: p.oid, c: p.confirmationFlag, ci: p.ciPublicKey, d: p.deleteNotification })}`);
});

/* ── 3. conformance checks ─────────────────────────────────────────────── */
console.log('\n3. conformance / negative cases');
let r;

r = LpaQr.parse('LPA:2$SMDP.EXAMPLE.COM$ABC');
check('AC_Format 2 is invalid', !r.ok && codes(r.errors).includes('AC_FORMAT'), JSON.stringify(r.errors));

r = LpaQr.parse('1$SMDP.EXAMPLE.COM$ABC');
check('missing LPA: prefix warns but parses', r.ok && codes(r.warnings).includes('PREFIX_MISSING'), codes(r.warnings));

r = LpaQr.parse('LPA:1$SMDP.EXAMPLE.COM$abc-def');
check('lower-case MatchingID warns', r.ok && codes(r.warnings).includes('TOKEN_CHARSET'), codes(r.warnings));

r = LpaQr.parse('LPA:1$SMDP.EXAMPLE.COM$ABC$1.3.6.1.4.1.31746$1');
check('OID + conf flag ok', r.ok && r.oid === '1.3.6.1.4.1.31746' && r.confirmationFlag === '1');

r = LpaQr.parse('LPA:1$SMDP.EXAMPLE.COM$ABC$3.1.1');
check('OID first arc >2 rejected', !r.ok && codes(r.errors).includes('OID_ARC1'), codes(r.errors));

r = LpaQr.parse('LPA:1$SMDP..EXAMPLE.COM$ABC');
check('empty label rejected', !r.ok && codes(r.errors).includes('ADDR_LABEL_EMPTY'), codes(r.errors));

r = LpaQr.parse('LPA:1$SMDP.EXAMPLE.COM$ABC$$2');
check('bad confirmation flag rejected', !r.ok && codes(r.errors).includes('CONF_FLAG'), codes(r.errors));

r = LpaQr.parse('LPA:1$SMDP.EXAMPLE.COM$ABCDE$1.3.6.1.4.1.31746$$$EXTRA$MORE');
check('extra trailing params are reported, not fatal', r.ok && codes(r.warnings).includes('EXTRA_FIELDS'),
      codes(r.warnings));

const long = LpaQr.build({ address: 'SMDP.EXAMPLE.COM', matchingId: 'A'.repeat(260) });
check('length cap warns at 255', codes(long.warnings).includes('LENGTH'), codes(long.warnings));

const lower = LpaQr.build({ address: 'smdp.example.com', matchingId: 'ABC' });
check('lower-case address -> byte mode warning', codes(lower.warnings).includes('BYTE_MODE'), codes(lower.warnings));

/* ── 4. real encode -> raster -> decode ────────────────────────────────── */
console.log('\n4. encode -> rasterise -> jsQR decode');

function raster(qr, scale) {
  const n = qr.getModuleCount();
  const quiet = 4;
  const dim = (n + quiet * 2) * scale;
  const buf = new Uint8ClampedArray(dim * dim * 4).fill(255);
  for (let y = 0; y < dim; y++) {
    for (let x = 0; x < dim; x++) {
      const mx = Math.floor(x / scale) - quiet;
      const my = Math.floor(y / scale) - quiet;
      const dark = mx >= 0 && my >= 0 && mx < n && my < n && qr.isDark(my, mx);
      const i = (y * dim + x) * 4;
      buf[i] = buf[i + 1] = buf[i + 2] = dark ? 0 : 255;
      buf[i + 3] = 255;
    }
  }
  return { buf, dim };
}

SPEC.forEach(([str], i) => {
  const qr = LpaQr.encodeMatrix(str, 'M');
  const { buf, dim } = raster(qr, 4);
  const dec = jsQR(buf, dim, dim);
  check('round trip ' + (i + 1) + ' decodes', dec && dec.data === str,
        dec ? 'got: ' + JSON.stringify(dec.data) + '\n         want: ' + JSON.stringify(str)
            : 'no QR found in raster');
});

// error-correction levels all produce a decodable code
['L', 'M', 'Q', 'H'].forEach(lvl => {
  const s = 'LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815';
  const qr = LpaQr.encodeMatrix(s, lvl);
  const { buf, dim } = raster(qr, 4);
  const dec = jsQR(buf, dim, dim);
  check('EC level ' + lvl + ' decodes', !!dec && dec.data === s, dec ? dec.data : 'no decode');
});

/* ── 5. renderer: EC choice, version maths, SVG accessibility ──────────── */
console.log('\n5. renderer');

const SHORT = 'LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815';
const LONG = 'LPA:1$SMDP.EXAMPLE.COM$' + 'A'.repeat(200);

check('short payload picks EC Q', LpaQr.pickEc(SHORT) === 'Q', LpaQr.pickEc(SHORT));
check('long payload picks EC M', LpaQr.pickEc(LONG) === 'M', LONG.length + ' chars -> ' + LpaQr.pickEc(LONG));

const qm = LpaQr.encodeMatrix(SHORT);
const n = qm.getModuleCount();
const v = LpaQr.version(qm);
check('version() matches the module count', v === (n - 17) / 4 && Number(v.toFixed(0)) === v, 'v' + v + ' n' + n);

const lbl = 'QR code for SMDP.EXAMPLE.COM';
const svg = LpaQr.toSVG(qm, { scale: 8, quiet: 4, label: lbl });
const want = (n + 8) * 8;
check('SVG is (modules + 2*quiet) * scale wide', svg.includes('width="' + want + '"') && svg.includes('height="' + want + '"'),
      'want ' + want + ' got ' + (/width="(\d+)"/.exec(svg) || [])[1]);
check('SVG carries an accessible name',
      svg.includes('role="img"') && svg.includes('aria-label="' + lbl + '"') && svg.includes('<title>' + lbl + '</title>'));
check('SVG escapes markup in the label',
      LpaQr.toSVG(qm, { label: 'A & B "q"' }).includes('aria-label="A &amp; B &quot;q&quot;"'));

let refused = false;
try { LpaQr.toCanvas(qm); } catch (e) { refused = /document/.test(e.message); }
check('toCanvas refuses without a document', refused);

const dqr = LpaQr.encodeMatrix(SHORT);
const dr = raster(dqr, 4);
const ddec = jsQR(dr.buf, dr.dim, dr.dim);
check('default EC round trip decodes to the same payload', !!ddec && ddec.data === SHORT, ddec ? ddec.data : 'no decode');

console.log('\n' + (fail === 0 ? 'ALL PASS' : 'FAILURES') + `: ${pass} passed, ${fail} failed\n`);
process.exit(fail === 0 ? 0 : 1);
