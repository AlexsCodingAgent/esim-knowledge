---
layout: default
title: LPA Activation Code ⇄ QR
description: Build a GSMA SGP.22 activation code (LPA:1$…) and its QR image, or decode a QR back to fields — entirely in your browser, with no upload and no network traffic.
permalink: /tools/lpa-qr/
no_jquery: true
csp: "default-src 'self'; img-src 'self' data: blob:; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; font-src 'self' data:; connect-src 'none'; form-action 'none'; base-uri 'none'; object-src 'none'"
---

<style>
/* The theme paints its gradient on <body> only; this page's content is taller than
   body's box, so the canvas behind it defaults to white. Pin the root background. */
html { background: #0a1628; }
html[data-theme="light"] { background: #ffffff; }

/* ── LPA / QR tool — purple accent, works in both themes ──────────────── */
.lpa-tool {
  --purple: #8b5cf6;
  --purple-soft: rgba(139, 92, 246, 0.12);
  --edge: rgba(255, 255, 255, 0.12);
  --surface: rgba(255, 255, 255, 0.03);
  --ink: #c8d6e5;
  --ink-dim: #9aa8b6;
  max-width: 980px;
  margin: 0 auto;
}
[data-theme="light"] .lpa-tool {
  --edge: rgba(0, 0, 0, 0.12);
  --surface: #f7f8fa;
  --ink: #2d3748;
  --ink-dim: #5a6675;
  --purple: #6d28d9;
  --purple-soft: rgba(109, 40, 217, 0.09);
}

.lpa-privacy {
  display: flex;
  gap: 0.6rem;
  align-items: flex-start;
  border: 1px solid var(--purple);
  background: var(--purple-soft);
  border-radius: 8px;
  padding: 0.7rem 0.9rem;
  font-size: 0.88rem;
  line-height: 1.45;
  color: var(--ink);
  margin: 0 0 1.2rem;
}
.lpa-privacy b { color: var(--purple); }

.lpa-tabs {
  display: flex;
  gap: 0.4rem;
  border-bottom: 1px solid var(--edge);
  margin-bottom: 1.2rem;
  flex-wrap: wrap;
}
.lpa-tab {
  appearance: none;
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--ink-dim);
  font: inherit;
  font-size: 0.95rem;
  padding: 0.55rem 0.9rem;
  cursor: pointer;
}
.lpa-tab:hover { color: var(--ink); }
.lpa-tab.active {
  color: var(--purple);
  border-bottom-color: var(--purple);
  font-weight: 600;
}

.lpa-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 300px;
  gap: 1.5rem;
  align-items: start;
}
@media (max-width: 760px) {
  .lpa-grid { grid-template-columns: 1fr; }
}

.lpa-field { margin-bottom: 0.85rem; }
.lpa-field label {
  display: block;
  font-size: 0.78rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--ink-dim);
  margin-bottom: 0.3rem;
}
.lpa-field .hint {
  font-size: 0.75rem;
  color: var(--ink-dim);
  margin-top: 0.25rem;
  line-height: 1.4;
}
.lpa-field input[type="text"], .lpa-field select, .lpa-field textarea {
  width: 100%;
  box-sizing: border-box;
  background: var(--surface);
  border: 1px solid var(--edge);
  border-radius: 6px;
  color: var(--ink);
  font: inherit;
  font-size: 0.9rem;
  padding: 0.5rem 0.6rem;
}
.lpa-field input[type="text"]:focus, .lpa-field textarea:focus, .lpa-field select:focus {
  outline: none;
  border-color: var(--purple);
  box-shadow: 0 0 0 2px var(--purple-soft);
}
.lpa-inline { display: flex; gap: 0.5rem; align-items: center; }
.lpa-check { display: flex; gap: 0.45rem; align-items: center; font-size: 0.88rem; color: var(--ink); }

.lpa-adv {
  border: 1px dashed var(--edge);
  border-radius: 6px;
  padding: 0.6rem 0.75rem;
  margin: 0.9rem 0 0.4rem;
}
.lpa-adv summary {
  cursor: pointer;
  font-size: 0.8rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--ink-dim);
}
.lpa-adv[open] summary { margin-bottom: 0.7rem; }

.lpa-preview {
  margin-top: 1rem;
  border: 1px solid var(--edge);
  border-radius: 6px;
  background: var(--surface);
  padding: 0.6rem 0.7rem;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.82rem;
  word-break: break-all;
  line-height: 1.55;
  color: var(--ink);
}
.lpa-dollar { color: var(--purple); font-weight: 700; }
.lpa-preview .lpa-part { color: var(--ink); }

.lpa-qr-panel {
  border: 1px solid var(--edge);
  border-radius: 8px;
  background: #fff;
  padding: 0.75rem;
  text-align: center;
}
.lpa-qr-panel svg { width: 100%; height: auto; max-width: 260px; display: block; margin: 0 auto; }
.lpa-qr-empty {
  color: #6b7280;
  font-size: 0.82rem;
  padding: 3rem 0.5rem;
}
.lpa-qr-meta {
  font-size: 0.72rem;
  color: var(--ink-dim);
  margin-top: 0.5rem;
  line-height: 1.4;
}
.lpa-dl { display: flex; gap: 0.5rem; justify-content: center; margin-top: 0.7rem; flex-wrap: wrap; }

.lpa-btn {
  appearance: none;
  border: 1px solid var(--purple);
  background: var(--purple-soft);
  color: var(--purple);
  border-radius: 6px;
  font: inherit;
  font-size: 0.82rem;
  padding: 0.4rem 0.75rem;
  cursor: pointer;
}
.lpa-btn:hover { background: var(--purple); color: #fff; }
.lpa-btn.ghost {
  border-color: var(--edge);
  background: transparent;
  color: var(--ink-dim);
}
.lpa-btn.ghost:hover { border-color: var(--purple); color: var(--purple); background: var(--purple-soft); }

.lpa-msg {
  font-size: 0.83rem;
  line-height: 1.45;
  padding: 0.5rem 0.65rem;
  border-radius: 6px;
  margin-top: 0.45rem;
  border-left: 3px solid;
  color: var(--ink);
}
.lpa-msg b { font-family: ui-monospace, monospace; font-size: 0.75rem; letter-spacing: 0.02em; }
.lpa-msg.err { border-color: #ef4444; background: rgba(239, 68, 68, 0.08); }
.lpa-msg.warn { border-color: #f59e0b; background: rgba(245, 158, 11, 0.08); }
.lpa-msg.ok { border-color: #22c55e; background: rgba(34, 197, 94, 0.08); }

.lpa-drop {
  border: 1px dashed var(--edge);
  border-radius: 8px;
  padding: 1.3rem 1rem;
  text-align: center;
  cursor: pointer;
  color: var(--ink-dim);
  font-size: 0.86rem;
  margin-bottom: 0.9rem;
}
.lpa-drop.over { border-color: var(--purple); background: var(--purple-soft); color: var(--ink); }
.lpa-drop b { color: var(--purple); }

.lpa-dec-table { width: 100%; border-collapse: collapse; margin-top: 1rem; font-size: 0.85rem; }
.lpa-dec-table th {
  text-align: left;
  font-weight: 600;
  color: var(--ink-dim);
  font-size: 0.78rem;
  padding: 0.45rem 0.6rem 0.45rem 0;
  vertical-align: top;
  width: 190px;
  border-bottom: 1px solid var(--edge);
}
.lpa-dec-table td { padding: 0.45rem 0.6rem 0.45rem 0; border-bottom: 1px solid var(--edge); vertical-align: top; color: var(--ink); }
.lpa-dec-table td code { word-break: break-all; }
.lpa-dec-table .lpa-doc { color: var(--ink-dim); font-size: 0.78rem; line-height: 1.4; }
.lpa-none { color: var(--ink-dim); font-style: italic; }

.lpa-format { margin-top: 2rem; border-top: 1px solid var(--edge); padding-top: 1rem; }
.lpa-format summary { cursor: pointer; color: var(--purple); font-size: 0.9rem; }
.lpa-format pre {
  background: var(--surface);
  border: 1px solid var(--edge);
  border-radius: 6px;
  padding: 0.8rem;
  overflow-x: auto;
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--ink);
}
.lpa-format table { width: 100%; border-collapse: collapse; font-size: 0.82rem; margin-top: 0.6rem; }
.lpa-format th, .lpa-format td { text-align: left; padding: 0.35rem 0.6rem 0.35rem 0; border-bottom: 1px solid var(--edge); vertical-align: top; }
.lpa-format th { color: var(--ink-dim); font-weight: 600; font-size: 0.76rem; text-transform: uppercase; letter-spacing: 0.04em; }
</style>

<div class="lpa-tool">

  <div class="lpa-privacy">
    <span aria-hidden="true">🔒</span>
    <span><b>Runs entirely in your browser.</b> The activation code — including the MatchingID — is never
    uploaded, logged, or sent anywhere. This page loads one static file and then makes
    <b>zero network requests</b>: the encoder and decoder are served from this site, there is no CDN,
    no analytics and no telemetry, and a <code>Content-Security-Policy</code> with
    <code>connect-src 'none'</code> makes any outgoing request impossible. Turn off your network
    after the page loads and the tool keeps working.</span>
  </div>

  <div class="lpa-tabs" role="tablist">
    <button class="lpa-tab active" data-tab="build" role="tab" aria-selected="true">Build → QR</button>
    <button class="lpa-tab" data-tab="decode" role="tab" aria-selected="false">QR / string → fields</button>
  </div>

  <section id="tab-build">
    <div class="lpa-grid">
      <div>
        <div class="lpa-field">
          <label for="f-addr">SM-DP+ Address (FQDN)</label>
          <input type="text" id="f-addr" spellcheck="false" autocapitalize="characters"
                 placeholder="SMDP.EXAMPLE.COM">
          <div class="hint">Upper-case alphanumerics and <code>- . / : % * +</code> (the ISO/IEC 18004
            alphanumeric set, minus <code>$</code>).</div>
        </div>

        <div class="lpa-field">
          <label for="f-token">MatchingID / AC_Token</label>
          <input type="text" id="f-token" spellcheck="false" autocapitalize="characters"
                 placeholder="04386-AGYFT-A74Y8-3F815">
          <div class="hint">Upper-case <code>0-9 A-Z</code> and <code>-</code>. May be empty if the
            SM-DP+ identifies the order another way.</div>
        </div>

        <div class="lpa-check" style="margin:0.9rem 0;">
          <input type="checkbox" id="f-conf">
          <label for="f-conf" style="text-transform:none;letter-spacing:0;font-size:0.88rem;color:var(--ink);margin:0;">
            Confirmation code required</label>
        </div>

        <details class="lpa-adv">
          <summary>Advanced parameters (SGP.22 v3)</summary>
          <div class="lpa-field">
            <label for="f-oid">SM-DP+ OID</label>
            <input type="text" id="f-oid" spellcheck="false" placeholder="1.3.6.1.4.1.31746">
            <div class="hint">From <code>CERT.DPauth.SIG</code>. Leave blank when unused.</div>
          </div>
          <div class="lpa-field">
            <label for="f-ci">CI Public Key indicator</label>
            <input type="text" id="f-ci" spellcheck="false" placeholder="e.g. 1">
            <div class="hint">v3.0+ indicator selecting an eSIM CA RootCA key.</div>
          </div>
          <div class="lpa-field">
            <label for="f-del">Delete Notification for Device Change</label>
            <input type="text" id="f-del" spellcheck="false" placeholder="leave blank">
            <div class="hint">Only valid in a Device Change flow (§4.1.3).</div>
          </div>
        </details>

        <div class="lpa-field" style="margin-top:0.9rem;">
          <label for="f-ecl">QR error correction</label>
          <select id="f-ecl">
            <option value="L">L — 7% (smallest symbol)</option>
            <option value="M" selected>M — 15% (recommended for activation codes)</option>
            <option value="Q">Q — 25%</option>
            <option value="H">H — 30% (largest)</option>
          </select>
          <div class="hint">SGP.22 does not mandate a level; M is the usual choice for printed
            activation codes. All four are generated here.</div>
        </div>

        <div class="lpa-preview" id="lpa-str" aria-live="polite"></div>
        <div class="lpa-inline" style="margin-top:0.5rem;">
          <button class="lpa-btn ghost" id="copy-btn" type="button">Copy</button>
        </div>

        <div id="build-msgs" aria-live="polite"></div>
      </div>

      <div>
        <div class="lpa-qr-panel">
          <div id="qr-holder"></div>
          <div class="lpa-qr-meta" id="qr-meta"></div>
        </div>
        <div class="lpa-dl" id="dl-wrap">
          <button class="lpa-btn" id="dl-svg" type="button">Download SVG</button>
          <button class="lpa-btn" id="dl-png" type="button">Download PNG</button>
        </div>
      </div>
    </div>
  </section>

  <section id="tab-decode" hidden>
    <div class="lpa-drop" id="drop">
      <b>Drop a QR image here</b>, click to choose a file, or paste an image with Ctrl/⌘+V.<br>
      <span style="font-size:0.78rem;">Decoding happens on this device — the image is never uploaded.</span>
      <input type="file" id="qr-file" accept="image/*" style="display:none;">
    </div>

    <div class="lpa-field">
      <label for="paste">…or paste an LPA string</label>
      <textarea id="paste" rows="2" spellcheck="false"
                placeholder="LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815"></textarea>
    </div>

    <table class="lpa-dec-table" id="dec-fields" style="display:none;"></table>
    <div class="lpa-qr-meta" id="dec-extra"></div>
    <div id="dec-msgs" aria-live="polite"></div>
    <canvas id="dec-canvas" style="display:none;"></canvas>
  </section>

  <details class="lpa-format">
    <summary>Activation Code format — SGP.22 v3.1 §4.1, Table 8</summary>
    <pre>QR payload = "LPA:" + Activation Code

Activation Code =
    "1"                       AC_Format  (any other value is invalid)
  $ SM-DP+ Address            FQDN, ISO/IEC 18004 alphanumeric set minus "$"
  $ AC_Token                  MatchingID — upper-case 0-9 A-Z and "-"; MAY be empty
  [ $ SM-DP+ OID ]            from CERT.DPauth.SIG
  [ $ "1" ]                   Confirmation Code Required flag
  [ $ CI Public Key indicator ]
  [ $ Delete Notification ]   Device Change only</pre>
    <table>
      <tr><th>Rule</th><th>Detail</th></tr>
      <tr><td>Prefix</td><td>A QR payload <b>shall</b> be prefixed with <code>LPA:</code>. Manual entry may omit it.</td></tr>
      <tr><td>Empty optionals</td><td>Skipping a middle parameter still needs its <code>$</code> — e.g. OID + confirmation with no CI key is <code>…$1.3.6.1.4.1.31746$1</code>.</td></tr>
      <tr><td>Length</td><td>Max 255 characters, unless a Delete Notification is present.</td></tr>
      <tr><td>Forward compatibility</td><td>Parameters beyond Table 8 <b>shall be ignored</b> by the device — this tool lists them rather than rejecting the code.</td></tr>
      <tr><td>Encoding</td><td>Because both AC_Format and the MatchingID are upper-case, a conformant code fits QR <b>alphanumeric mode</b> (§4.1.1 notes this explicitly). Non-conformant lower-case input forces byte mode, which this tool flags.</td></tr>
    </table>
  </details>

</div>

<script src="{{ '/assets/js/vendor/qrcode-generator.js' | relative_url }}"></script>
<script src="{{ '/assets/js/vendor/jsQR.js' | relative_url }}"></script>
<script src="{{ '/assets/js/lpa-qr.js' | relative_url }}"></script>
<script src="{{ '/assets/js/lpa-qr-ui.js' | relative_url }}"></script>
