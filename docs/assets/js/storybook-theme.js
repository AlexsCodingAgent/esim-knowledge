/**
 * Theme toggle for eUICC.tech storybooks.
 * Injects toggle button + light-mode CSS overrides.
 * Self-contained — no external dependencies.
 *
 * Add to storybook <head>:
 *   <script src="../../assets/js/storybook-theme.js"></script>
 */
(function() {
  // ── Light-mode CSS overrides (minified, injected at runtime) ──
  var LIGHT_CSS = [
    '[data-theme="light"] body{background:#fff!important;color:#2d3748!important}',
    '[data-theme="light"] body{background:linear-gradient(#f7f8fa,#fff) fixed!important}',
    '[data-theme="light"] .book{background:transparent}',
    '[data-theme="light"] .page{background:transparent}',
    '[data-theme="light"] .page-cover{background:linear-gradient(135deg,#f7f8fa 0%,#fff 50%,#f7f8fa 100%)!important}',
    '[data-theme="light"] h1{color:#1a202c!important}',
    '[data-theme="light"] h2{color:#4a5568!important}',
    '[data-theme="light"] h3{color:#2b6cb0!important}',
    '[data-theme="light"] .story-text{color:#2d3748!important}',
    '[data-theme="light"] .story-text em{color:#2b6cb0!important}',
    '[data-theme="light"] .story-text strong{color:#1a202c!important}',
    '[data-theme="light"] .page-num{color:#a0aec0!important}',
    '[data-theme="light"] .nav a{background:rgba(0,0,0,.06)!important;color:#2b6cb0!important}',
    '[data-theme="light"] .nav a:hover{background:rgba(0,0,0,.1)!important}',
    '[data-theme="light"] div[style*="position:fixed"][style*="top:0"]{background:rgba(255,255,255,.92)!important;border-bottom:1px solid rgba(0,0,0,.08)!important}',
    '[data-theme="light"] div[style*="position:fixed"][style*="top:0"] span{color:#718096!important}',
    '[data-theme="light"] div[style*="position:fixed"][style*="top:0"] a{color:#2b6cb0!important}',
    '[data-theme="light"] .illustration svg{filter:brightness(1.05)}',
    '[data-theme="light"] div[style*="position:fixed"][style*="bottom:1rem"] a{background:rgba(0,0,0,.06)!important;color:#2b6cb0!important}',
    '[data-theme="light"] div[style*="position:fixed"][style*="bottom:1rem"] a:hover{background:rgba(0,0,0,.1)!important}'
  ].join('\n');

  var STORAGE_KEY = 'euicc-theme';
  var TOGGLE_HTML = '<button id="theme-toggle" aria-label="Toggle light/dark mode" title="Toggle theme" style="position:fixed;top:0.75rem;right:3.5rem;z-index:1000;background:rgba(93,173,226,0.1);border:1px solid rgba(93,173,226,0.2);border-radius:50%;width:38px;height:38px;font-size:1.1rem;cursor:pointer;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);color:inherit;line-height:1">☀️</button>';

  function getSaved() {
    try { return localStorage.getItem(STORAGE_KEY); } catch(e) { return null; }
  }

  function getSystem() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) return 'light';
    return 'dark';
  }

  function apply(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    var btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.textContent = theme === 'light' ? 'Dark' : 'Light';
      btn.setAttribute('aria-label', theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
      if (theme === 'light') {
        btn.style.background = 'rgba(0,0,0,0.06)';
        btn.style.borderColor = 'rgba(0,0,0,0.12)';
      } else {
        btn.style.background = 'rgba(93,173,226,0.1)';
        btn.style.borderColor = 'rgba(93,173,226,0.2)';
      }
    }

    // Inject or remove light-mode CSS
    var styleEl = document.getElementById('storybook-light-theme');
    if (theme === 'light') {
      if (!styleEl) {
        styleEl = document.createElement('style');
        styleEl.id = 'storybook-light-theme';
        styleEl.textContent = LIGHT_CSS;
        document.head.appendChild(styleEl);
      }
    } else {
      if (styleEl) styleEl.remove();
    }
  }

  function toggle() {
    var current = document.documentElement.getAttribute('data-theme') || 'dark';
    var next = current === 'light' ? 'dark' : 'light';
    apply(next);
    try { localStorage.setItem(STORAGE_KEY, next); } catch(e) {}
  }

  // Init on DOM ready
  function init() {
    // Inject toggle button
    document.body.insertAdjacentHTML('beforeend', TOGGLE_HTML);
    document.getElementById('theme-toggle').addEventListener('click', toggle);

    // Apply saved or system theme
    var saved = getSaved();
    var theme = saved || getSystem();
    apply(theme);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
