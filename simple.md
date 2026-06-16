---
layout: default
title: eUICC.tech — Simple
description: "Two paths into the eSIM RSP knowledge base: illustrated stories for newcomers, or technical deep dives for engineers."
---

<style>
  .simple-hero {
    display: flex;
    gap: 24px;
    margin: 2rem 0;
    flex-wrap: wrap;
  }
  .simple-card {
    flex: 1;
    min-width: 280px;
    border-radius: 16px;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    text-decoration: none;
    display: block;
  }
  .simple-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  }
  .simple-card-art {
    width: 100%;
    padding: 40px 20px 20px;
    text-align: center;
  }
  .simple-card-art svg {
    width: 100%;
    max-width: 340px;
    height: auto;
  }
  .simple-card-body {
    padding: 0 28px 36px;
    text-align: center;
  }
  .simple-card-body h2 {
    margin: 0 0 8px;
    font-size: 1.6rem;
    color: #e8eef5;
  }
  .simple-card-body p {
    margin: 0;
    font-size: 0.95rem;
    color: #8b949e;
    line-height: 1.5;
  }
  .card-illustrated {
    background: linear-gradient(160deg, #1a1040 0%, #0d1b2a 60%);
    border: 1px solid rgba(168,85,247,0.25);
  }
  .card-illustrated:hover {
    border-color: rgba(168,85,247,0.5);
  }
  .card-technical {
    background: linear-gradient(160deg, #0a1a2e 0%, #0d1b2a 60%);
    border: 1px solid rgba(34,211,238,0.25);
  }
  .card-technical:hover {
    border-color: rgba(34,211,238,0.5);
  }

  @media (max-width: 640px) {
    .simple-hero { flex-direction: column; }
    .simple-card-art { padding: 28px 16px 12px; }
    .simple-card-art svg { max-width: 260px; }
    .simple-card-body { padding: 0 20px 28px; }
    .simple-card-body h2 { font-size: 1.35rem; }
  }
</style>

<div class="simple-hero">

  <!-- ILLUSTRATED CARD -->
  <a href="docs/articles/kids/" class="simple-card card-illustrated">
    <div class="simple-card-art">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 260">
        <!-- Open book with colorful pages -->
        <g transform="translate(170,150)">
          <!-- Book cover (left) -->
          <path d="M-2,20 L-130,0 L-130,-30 L-2,-10 Z" fill="#7c3aed" opacity="0.7"/>
          <path d="M-2,20 L-130,0 L-130,-30 L-2,-10 Z" fill="none" stroke="#a78bfa" stroke-width="1.2"/>
          <!-- Book cover (right) -->
          <path d="M2,20 L130,0 L130,-30 L2,-10 Z" fill="#a78bfa" opacity="0.5"/>
          <path d="M2,20 L130,0 L130,-30 L2,-10 Z" fill="none" stroke="#c4b5fd" stroke-width="1.2"/>
          <!-- Floating pages (left) -->
          <path d="M-2,16 L-120,-3 L-120,-28 L-2,-11 Z" fill="#fbbf24" opacity="0.35">
            <animateTransform attributeName="transform" type="translate" values="0,0;0,-2;0,0" dur="3s" repeatCount="indefinite"/>
          </path>
          <!-- Floating pages (right) -->
          <path d="M2,16 L120,-3 L120,-28 L2,-11 Z" fill="#34d399" opacity="0.3">
            <animateTransform attributeName="transform" type="translate" values="0,0;0,-3;0,0" dur="3.5s" repeatCount="indefinite"/>
          </path>
          <!-- More pages -->
          <path d="M-2,13 L-110,-5 L-110,-26 L-2,-12 Z" fill="#f472b6" opacity="0.25">
            <animateTransform attributeName="transform" type="translate" values="0,0;0,-1.5;0,0" dur="4s" repeatCount="indefinite"/>
          </path>
          <!-- Center spine glow -->
          <line x1="0" y1="-30" x2="0" y2="22" stroke="#a78bfa" stroke-width="2" opacity="0.8"/>
          <!-- Spine highlight -->
          <line x1="0" y1="-30" x2="0" y2="22" stroke="#c4b5fd" stroke-width="1" opacity="0.4"/>
        </g>
        <!-- Stars/sparkles around the book -->
        <g fill="#fbbf24" opacity="0.8">
          <circle cx="60" cy="55" r="2">
            <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2s" repeatCount="indefinite"/>
          </circle>
          <circle cx="280" cy="45" r="1.8">
            <animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.5s" repeatCount="indefinite"/>
          </circle>
          <circle cx="45" cy="160" r="1.5">
            <animate attributeName="opacity" values="0.9;0.3;0.9" dur="1.8s" repeatCount="indefinite"/>
          </circle>
          <circle cx="295" cy="170" r="2.2">
            <animate attributeName="opacity" values="0.2;0.8;0.2" dur="3s" repeatCount="indefinite"/>
          </circle>
          <circle cx="20" cy="100" r="1.5">
            <animate attributeName="opacity" values="0.5;1;0.5" dur="2.2s" repeatCount="indefinite"/>
          </circle>
          <circle cx="320" cy="110" r="1.7">
            <animate attributeName="opacity" values="0.8;0.1;0.8" dur="2.8s" repeatCount="indefinite"/>
          </circle>
        </g>
        <!-- Title text -->
        <text x="170" y="245" fill="#e8eef5" font-family="system-ui,sans-serif" font-size="12" font-weight="500" text-anchor="middle" letter-spacing="1">ILLUSTRATED &middot; SIMPLE</text>
      </svg>
    </div>
    <div class="simple-card-body">
      <h2>Illustrated, Simple</h2>
      <p>Stories, analogies, and emojis. For visual learners, newcomers, or anyone who wants the intuition before the technical detail.</p>
    </div>
  </a>

  <!-- TECHNICAL CARD -->
  <a href="docs/articles/" class="simple-card card-technical">
    <div class="simple-card-art">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 260">
        <!-- Architecture diagram: clean boxes + arrows -->
        <g transform="translate(170,20)">
          <!-- Top box: eUICC -->
          <rect x="-60" y="0" width="120" height="44" rx="8" fill="rgba(76,29,149,0.35)" stroke="#a78bfa" stroke-width="1.5"/>
          <text x="0" y="27" fill="white" font-family="system-ui,sans-serif" font-size="12" font-weight="600" text-anchor="middle">eUICC</text>
        </g>
        <g transform="translate(170,80)">
          <!-- SM-DP+ (left) -->
          <rect x="-155" y="0" width="130" height="44" rx="8" fill="rgba(6,78,59,0.35)" stroke="#34d399" stroke-width="1.5"/>
          <text x="-90" y="27" fill="white" font-family="system-ui,sans-serif" font-size="12" font-weight="600" text-anchor="middle">SM-DP+</text>
          <!-- SM-DS (right) -->
          <rect x="25" y="0" width="130" height="44" rx="8" fill="rgba(120,53,15,0.3)" stroke="#fbbf24" stroke-width="1.5"/>
          <text x="90" y="27" fill="white" font-family="system-ui,sans-serif" font-size="12" font-weight="600" text-anchor="middle">SM-DS</text>
        </g>
        <g transform="translate(170,145)">
          <!-- LPA / Device -->
          <rect x="-60" y="0" width="120" height="44" rx="8" fill="rgba(8,51,68,0.35)" stroke="#22d3ee" stroke-width="1.5"/>
          <text x="0" y="27" fill="white" font-family="system-ui,sans-serif" font-size="12" font-weight="600" text-anchor="middle">LPA</text>
        </g>
        <!-- Connecting lines (arrows between boxes) -->
        <!-- eUICC to SM-DP+ -->
        <line x1="140" y1="64" x2="105" y2="100" stroke="#34d399" stroke-width="1.5" fill="none"/>
        <polygon points="118,98 105,100 113,92" fill="#34d399"/>
        <!-- eUICC to SM-DS -->
        <line x1="200" y1="64" x2="235" y2="100" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
        <polygon points="222,92 235,100 227,98" fill="#fbbf24"/>
        <!-- SM-DP+ to LPA -->
        <line x1="105" y1="124" x2="140" y2="165" stroke="#34d399" stroke-width="1.5" fill="none"/>
        <polygon points="138,153 140,167 127,157" fill="#34d399"/>
        <!-- SM-DS to LPA -->
        <line x1="235" y1="124" x2="200" y2="165" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
        <polygon points="202,153 200,167 213,157" fill="#fbbf24"/>
        <!-- eUICC to LPA (direct, dashed) -->
        <line x1="170" y1="64" x2="170" y2="145" stroke="#64748b" stroke-width="1" stroke-dasharray="4,3" fill="none"/>
        <!-- Label: "SGP.22" -->
        <text x="85" y="95" fill="#34d399" font-family="system-ui,sans-serif" font-size="9" opacity="0.7">ES9+</text>
        <text x="250" y="95" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="9" opacity="0.7">ES11</text>
        <text x="95" y="158" fill="#34d399" font-family="system-ui,sans-serif" font-size="9" opacity="0.7">ES8+</text>
        <text x="223" y="158" fill="#fbbf24" font-family="system-ui,sans-serif" font-size="9" opacity="0.7">ES12</text>
        <!-- Subtle pulse on connecting lines -->
        <circle cx="170" cy="105" r="3" fill="#64748b" opacity="0.3">
          <animate attributeName="opacity" values="0.3;0;0.3" dur="2s" repeatCount="indefinite"/>
        </circle>
        <!-- Title text -->
        <text x="170" y="245" fill="#e8eef5" font-family="system-ui,sans-serif" font-size="12" font-weight="500" text-anchor="middle" letter-spacing="1">DETAILED &middot; TECHNICAL</text>
      </svg>
    </div>
    <div class="simple-card-body">
      <h2>Detailed and Technical</h2>
      <p>Spec-driven. Precise. For engineers and implementers. Every GSMA eSIM specification explained in focused articles.</p>
    </div>
  </a>

</div>

---

<div align="center" style="margin: 3rem 0 1rem;">

[Back to full homepage →](/)

</div>
