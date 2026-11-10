# Vendored JS (self-hosted, no CDN)

These files are served from euicc.tech so the `/tools/lpa-qr/` page can run with
**zero external requests**. They are committed copies, not runtime dependencies.
nothing here is fetched from a package registry or CDN when the page loads.

| File | Upstream | Version | Licence |
|---|---|---|---|
| `qrcode-generator.js` | [kazuhikoarase/qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) (`js/qrcode.js`) | 1.4.4 | MIT |
| `jsQR.js` | [cozmo/jsQR](https://github.com/cozmo/jsQR) (`dist/jsQR.js`) | master @ 2026-11-09 | Apache-2.0 |

Both keep their upstream headers. To update, replace the file and re-run
`node scripts/test_lpa_qr.js`; the suite includes real encode → rasterise →
jsQR-decode round trips, so a broken swap fails loudly.

Why vendored rather than imported:

- **Privacy.** A CDN request leaks the visitor's IP and referrer to a third party on
  a page that handles activation codes. Self-hosting keeps the page self-contained.
- **Offline.** With the CSP below, the page keeps working after the network is cut.
- **Integrity.** Pinned bytes, reviewable in git, no supply-chain surprises.

The page sets `connect-src 'none'` and drops jQuery via `no_jquery: true`, so the
only resources it loads are same-origin CSS, fonts and these scripts.
