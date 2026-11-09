---
layout: default
title: LPA Activation Code ⇄ QR
description: Paste a GSMA SGP.22 activation code to get its QR image, or drop a QR image to read the code back. Runs entirely in your browser — nothing is uploaded.
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

.lpa-actions {
  display: flex;
  gap: 0.6rem;
  align-items: center;
  margin: 0.75rem 0 1.15rem;
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
  font-size: 0.75rem;
  color: var(--dim);
  padding-left: 0.6rem;
  border-left: 1px solid var(--edge);
}

.lpa-out {
  display: grid;
  grid-template-columns: 240px minmax(0, 1fr);
  gap: 1.4rem;
  align-items: start;
}
@media (max-width: 700px) {
  .lpa-out { grid-template-columns: 1fr; }
  .lpa-qr { order: -1; }
}

.lpa-qr {
  background: #fff;
  border-radius: 8px;
  padding: 0.6rem;
  text-align: center;
  min-height: 120px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.lpa-qr svg { width: 100%; height: auto; display: block; }
.lpa-qr .none { color: #9ca3af; font-size: 0.78rem; padding: 2rem 0.4rem; }

.lpa table { width: 100%; border-collapse: collapse; font-size: 0.84rem; }
.lpa th {
  text-align: left;
  font-weight: 500;
  color: var(--dim);
  font-size: 0.76rem;
  text-transform: uppercase;
  letter-spacing: 0.03em;
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

  <p class="lpa-note">
    <b>Paste an activation code</b> to get its QR — or <b>drop a QR image anywhere on this page</b>
    (or paste one) to read it back.
    Everything happens in this tab: no upload, no analytics, no network requests, enforced by
    <code>connect-src 'none'</code>. Works offline once loaded.
  </p>

  <textarea id="input" spellcheck="false" autocomplete="off" autocapitalize="characters"
            aria-label="LPA activation code"></textarea>

  <div class="lpa-actions">
    <button id="copy" type="button">Copy</button>
    <button id="dl" type="button">Download SVG</button>
    <span class="lpa-meta" id="meta"></span>
  </div>

  <div class="lpa-out">
    <div class="lpa-qr" id="qr"><div class="none">QR appears here</div></div>
    <table id="fields" hidden></table>
  </div>

  <div class="lpa-msgs" id="msgs" aria-live="polite"></div>

  <details class="lpa-spec">
    <summary>Format — SGP.22 v3.1 §4.1, Table 8</summary>
    <pre>LPA:1$&lt;SM-DP+ FQDN&gt;$&lt;MatchingID&gt;[ $&lt;SM-DP+ OID&gt; [ $1 [ $&lt;CI public key&gt; ] ] ]</pre>
    <p>
      <b>AC_Format</b> must be <code>1</code>. The <b>FQDN</b> uses the QR alphanumeric
      character set minus <code>$</code>; the <b>MatchingID</b> is upper-case
      <code>0-9 A-Z</code> and <code>-</code>, and may be empty. Skipping a middle parameter keeps its
      <code>$</code> (<code>…$OID$$CI</code>). Max 255 characters. Because the fields are upper-case,
      a conformant code encodes in QR <b>alphanumeric mode</b> — lower-case input forces byte mode,
      which the tool warns about. Parameters beyond the five above must be ignored by the device, so
      they are shown but not interpreted.
    </p>
  </details>

</div>

<script src="{{ '/assets/js/vendor/qrcode-generator.js' | relative_url }}"></script>
<script src="{{ '/assets/js/vendor/jsQR.js' | relative_url }}"></script>
<script src="{{ '/assets/js/lpa-qr.js' | relative_url }}"></script>
<script src="{{ '/assets/js/lpa-qr-ui.js' | relative_url }}"></script>
