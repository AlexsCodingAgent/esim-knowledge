---
layout: default
title: LPA Activation Code ⇄ QR
description: Paste a GSMA SGP.22 activation code to get its QR image, or drop a QR image to read the code back. Runs entirely in your browser. Nothing is uploaded.
permalink: /tools/lpa-qr/
no_jquery: true
csp: "default-src 'self'; img-src 'self' data: blob:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; font-src 'self' data:; connect-src 'none'; form-action 'none'; base-uri 'none'; object-src 'none'"
---

<style>
/* The theme paints its gradient on <body> only; this page is taller than body's
   box, so pin the root background or the canvas behind it shows white. */
html { background: #0a1628; }
html[data-theme="light"] { background: #fff; }

.lpa {
  --purple: #8b5cf6;
  --purple-soft: rgba(139, 92, 246, 0.12);
  --edge: rgba(255, 255, 255, 0.14);
  --ink: #c8d6e5;
  --dim: #9aa8b6;
  max-width: 880px;
  margin: 0 auto;
}
[data-theme="light"] .lpa {
  --purple: #6d28d9;
  --purple-soft: rgba(109, 40, 217, 0.09);
  --edge: rgba(0, 0, 0, 0.14);
  --ink: #2d3748;
  --dim: #5a6675;
}
.lpa * { box-sizing: border-box; }

.lpa-title {
  font-size: 1.25rem;
  line-height: 1.3;
  margin: 0 0 0.9rem;
  letter-spacing: 0.01em;
  color: #e8eef5;
}
[data-theme="light"] .lpa-title { color: #1a202c; }

.lpa-note {
  font-size: 0.82rem;
  color: var(--dim);
  margin: 0 0 1rem;
  padding-left: 0.75rem;
  border-left: 2px solid var(--purple);
  line-height: 1.5;
}
.lpa-note b { color: var(--ink); font-weight: 600; }

.lpa textarea {
  width: 100%;
  min-height: 3.4rem;
  resize: vertical;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--edge);
  border-radius: 8px;
  color: var(--ink);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.9rem;
  line-height: 1.55;
  padding: 0.7rem 0.8rem;
}
[data-theme="light"] .lpa textarea { background: #fbfbfd; }
.lpa textarea:focus {
  outline: none;
  border-color: var(--purple);
  box-shadow: 0 0 0 2px var(--purple-soft);
}

.lpa-field { margin-bottom: 0.25rem; }

.lpa-label {
  display: block;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--dim);
  margin-bottom: 0.35rem;
}

.lpa-subactions {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  margin: 0.7rem 0 0.9rem;
  flex-wrap: wrap;
}
.lpa button {
  font: inherit;
  font-size: 0.8rem;
  padding: 0.35rem 0.7rem;
  border-radius: 6px;
  border: 1px solid var(--purple);
  background: var(--purple-soft);
  color: var(--purple);
  cursor: pointer;
}
.lpa button:hover:not(:disabled) { background: var(--purple); color: #fff; }
.lpa button:disabled { opacity: 0.4; cursor: default; }
.lpa-meta {
  font-size: 0.72rem;
  color: var(--dim);
  margin-top: 0.55rem;
  line-height: 1.5;
}
.lpa-meta span { display: block; }

.lpa-qractions {
  display: flex;
  gap: 0.35rem;
  margin-top: 0.7rem;
  width: 100%;
}
.lpa-qractions button { flex: 1; min-width: 0; }

.lpa-out {
  margin-top: 1.5rem;
  padding-top: 1.2rem;
  border-top: 1px solid var(--edge);
  display: grid;
  grid-template-columns: 270px minmax(0, 1fr);
  gap: 2.2rem;
  align-items: start;
}
@media (max-width: 700px) {
  .lpa-out { grid-template-columns: 1fr; }
  .lpa-result { max-width: 340px; margin: 0 auto; }
}

.lpa-result .lpa-label,
.lpa-fields .lpa-label { margin-bottom: 0.4rem; }

.lpa-qr {
  background: #fff;
  border-radius: 8px;
  padding: 0.6rem;
  text-align: center;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.lpa-qr svg { width: 100%; height: auto; display: block; }
[data-theme="light"] .lpa-qr { border: 1px solid rgba(0, 0, 0, 0.12); }
.lpa-qr .none { color: #9ca3af; font-size: 0.78rem; padding: 2.6rem 0.4rem; }

.lpa table { width: 100%; border-collapse: collapse; font-size: 0.84rem; }
.lpa th {
  text-align: left;
  font-weight: 500;
  color: var(--dim);
  font-size: 0.76rem;
  padding: 0.4rem 0.8rem 0.4rem 0;
  white-space: nowrap;
  vertical-align: top;
  border-bottom: 1px solid var(--edge);
}
.lpa td {
  padding: 0.4rem 0 0.4rem 0;
  border-bottom: 1px solid var(--edge);
  color: var(--ink);
  word-break: break-all;
}
.lpa td code { font-size: 0.82rem; }
.lpa .none { color: var(--dim); font-style: italic; }

.lpa-msgs { margin-top: 1rem; }
.lpa .msg {
  font-size: 0.81rem;
  line-height: 1.45;
  padding: 0.4rem 0.6rem;
  border-radius: 5px;
  border-left: 3px solid;
  margin-bottom: 0.4rem;
  color: var(--ink);
}
.lpa .msg.err { border-color: #ef4444; background: rgba(239, 68, 68, 0.09); }
.lpa .msg.warn { border-color: #f59e0b; background: rgba(245, 158, 11, 0.09); }
.lpa .msg.ok { border-color: #22c55e; background: rgba(34, 197, 94, 0.09); }

body.dropping .lpa textarea { border-color: var(--purple); border-style: dashed; }

/* the whole viewport becomes the drop target, visibly */
.drop-veil {
  position: fixed;
  inset: 0;
  z-index: 100;
  display: none;
  align-items: center;
  justify-content: center;
  background: rgba(6, 14, 26, 0.86);
  border: 3px dashed #8b5cf6;
  color: #fff;
  font-size: 0.95rem;
  pointer-events: none;
}
body.dropping .drop-veil { display: flex; }

/* spec examples: one click loads a Table 8 case */
.lpa-examples {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem;
  margin: 0.15rem 0 0.9rem;
  font-size: 0.75rem;
  color: var(--ink);
}
.lpa .lpa-chip {
  font: inherit;
  font-size: 0.72rem;
  padding: 0.18rem 0.55rem;
  border-radius: 999px;
  border: 1px solid var(--edge);
  background: rgba(255, 255, 255, 0.03);
  color: var(--ink);
  cursor: pointer;
}
[data-theme="light"] .lpa .lpa-chip { background: #fbfbfd; }
.lpa .lpa-chip:hover {
  border-color: var(--purple);
  color: var(--purple);
  background: var(--purple-soft);
}
.lpa button:focus-visible,
.lpa .lpa-chip:focus-visible {
  outline: 2px solid var(--purple);
  outline-offset: 2px;
}

/* the symbol opens at scannable size for a second device */
.lpa-qr.can-zoom { cursor: zoom-in; }
.lpa-zoom {
  position: fixed;
  inset: 0;
  z-index: 95;
  display: none;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.9rem;
  padding: 4vmin;
  background: rgba(4, 10, 20, 0.93);
}
.lpa-zoom.open { display: flex; }
.lpa-zoom .card {
  background: #fff;
  border-radius: 12px;
  padding: 1.1rem;
  width: min(88vmin, 720px);
}
.lpa-zoom .card svg { width: 100%; height: auto; display: block; }
.lpa-zoom .hint { font-size: 0.76rem; color: rgba(255, 255, 255, 0.72); }

.lpa-spec { margin-top: 2rem; padding-top: 0.9rem; border-top: 1px solid var(--edge); }
.lpa-spec summary { cursor: pointer; font-size: 0.84rem; color: var(--purple); }
.lpa-spec pre {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--edge);
  border-radius: 6px;
  padding: 0.7rem 0.8rem;
  overflow-x: auto;
  font-size: 0.76rem;
  line-height: 1.5;
  color: var(--ink);
}
[data-theme="light"] .lpa-spec pre { background: #fbfbfd; }
.lpa-spec p { font-size: 0.82rem; color: var(--dim); line-height: 1.55; }
</style>

<div class="lpa">

  <h1 class="lpa-title">LPA activation code <span aria-hidden="true">&#8646;</span> QR</h1>

  <p class="lpa-note">
    <b>Paste an activation code</b> to get its QR, or <b>drop a QR image anywhere on this page</b>
    (or paste one) to read it back. Download the symbol as <b>PNG</b> for a phone or <b>SVG</b> for print.
    Everything happens in this tab: no upload, no analytics, no network requests, enforced by
    <code>connect-src 'none'</code>. Works offline once loaded.
  </p>

  <div class="lpa-field">
    <label class="lpa-label" for="input">Activation code</label>
    <textarea id="input" spellcheck="false" autocomplete="off" autocapitalize="characters"
              placeholder="LPA:1$SM-DP+ address$MatchingID"></textarea>
    <div class="lpa-subactions">
      <button id="copy" type="button">Copy code</button>
      <button id="pick" type="button">Read a QR image</button>
      <input id="file" type="file" accept="image/*" hidden>
    </div>
    <div class="lpa-examples" id="examples"><span>Try an example:</span></div>
  </div>

  <div class="lpa-msgs" id="msgs" aria-live="polite"></div>

  <div class="lpa-out">
    <div class="lpa-result">
      <span class="lpa-label" id="qr-label">QR</span>
      <div class="lpa-qr" id="qr" aria-labelledby="qr-label"><div class="none">QR appears here</div></div>
      <div class="lpa-qractions">
        <button id="dlpng" type="button" disabled>PNG</button>
        <button id="dl" type="button" disabled>SVG</button>
      </div>
      <div class="lpa-meta" id="meta"></div>
    </div>
    <div class="lpa-fields">
      <span class="lpa-label" id="fields-label">Decoded fields</span>
      <table id="fields" aria-labelledby="fields-label" hidden></table>
    </div>
  </div>

  <details class="lpa-spec">
    <summary>Format: SGP.22 v3.1 §4.1, Table 8</summary>
    <pre>LPA:1$&lt;SM-DP+ FQDN&gt;$&lt;MatchingID&gt;[ $&lt;SM-DP+ OID&gt; [ $1 [ $&lt;CI public key&gt; ] ] ]</pre>
    <p>
      <b>AC_Format</b> must be <code>1</code>. The <b>FQDN</b> uses the QR alphanumeric
      character set minus <code>$</code>; the <b>MatchingID</b> is upper-case
      <code>0-9 A-Z</code> and <code>-</code>, and may be empty. Skipping a middle parameter keeps its
      <code>$</code> (<code>…$OID$$CI</code>). Max 255 characters. Because the fields are upper-case,
      a conformant code encodes in QR <b>alphanumeric mode</b>; lower-case input forces byte mode,
      which the tool warns about. Parameters beyond the five above must be ignored by the device, so
      they are shown but not interpreted.
    </p>
  </details>

  <div class="lpa-zoom" id="zoom" role="dialog" aria-modal="true" aria-label="Enlarged QR code" aria-hidden="true">
    <div class="card" id="zoom-qr"></div>
    <div class="hint">Click anywhere or press Esc to close</div>
  </div>

</div>

<div class="drop-veil">Drop the QR image to read it back</div>

<script src="{{ '/assets/js/vendor/qrcode-generator.js' | relative_url }}"></script>
<script src="{{ '/assets/js/vendor/jsQR.js' | relative_url }}"></script>
<script src="{{ '/assets/js/lpa-qr.js' | relative_url }}"></script>
<script src="{{ '/assets/js/lpa-qr-ui.js' | relative_url }}"></script>
