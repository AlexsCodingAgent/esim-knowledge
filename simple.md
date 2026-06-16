---
layout: default
title: eUICC.tech — Simple
description: "Two paths into the eSIM RSP knowledge base: illustrated stories for newcomers, or technical deep dives for engineers."
---

<style>
  .simple-hero {
    display: flex;
    gap: 28px;
    margin: 3rem 0 2rem;
    flex-wrap: wrap;
  }
  .simple-card {
    flex: 1;
    min-width: 280px;
    border-radius: 20px;
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
    padding: 48px 20px 32px;
    text-align: center;
  }
  .simple-card-art svg {
    width: 140px;
    height: 140px;
  }
  .simple-card-body {
    padding: 0 32px 40px;
    text-align: center;
  }
  .simple-card-body h2 {
    margin: 0 0 10px;
    font-size: 1.7rem;
    color: #e8eef5;
  }
  .simple-card-body p {
    margin: 0;
    font-size: 0.95rem;
    color: #8b949e;
    line-height: 1.5;
  }
  .card-illustrated {
    background: linear-gradient(160deg, #1e1045 0%, #0d1b2a 60%);
    border: 1px solid rgba(168,85,247,0.22);
  }
  .card-illustrated:hover {
    border-color: rgba(168,85,247,0.45);
  }
  .card-technical {
    background: linear-gradient(160deg, #0a1e34 0%, #0d1b2a 60%);
    border: 1px solid rgba(34,211,238,0.22);
  }
  .card-technical:hover {
    border-color: rgba(34,211,238,0.45);
  }

  @media (max-width: 640px) {
    .simple-hero { flex-direction: column; margin: 2rem 0 1rem; }
    .simple-card-art { padding: 36px 16px 24px; }
    .simple-card-art svg { width: 110px; height: 110px; }
    .simple-card-body { padding: 0 24px 32px; }
    .simple-card-body h2 { font-size: 1.4rem; }
  }
</style>

<div class="simple-hero">

  <!-- ILLUSTRATED CARD -->
  <a href="docs/articles/kids/" class="simple-card card-illustrated">
    <div class="simple-card-art">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140">
        <!-- Open book -->
        <g transform="translate(70,62)">
          <path d="M0,2 L-42,-18 L-42,-42 L0,-22 Z" fill="#7c3aed" opacity="0.7"/>
          <path d="M0,2 L42,-18 L42,-42 L0,-22 Z" fill="#a78bfa" opacity="0.45"/>
          <!-- Pages -->
          <path d="M0,0 L-36,-16 L-36,-38 L0,-22 Z" fill="#fbbf24" opacity="0.3"/>
          <path d="M0,0 L36,-16 L36,-38 L0,-22 Z" fill="#34d399" opacity="0.25"/>
          <path d="M0,-2 L-28,-15 L-28,-35 L0,-22 Z" fill="#f472b6" opacity="0.2"/>
          <!-- Spine -->
          <line x1="0" y1="-42" x2="0" y2="4" stroke="#c4b5fd" stroke-width="2.5" opacity="0.7"/>
        </g>
        <!-- Sparkles -->
        <circle cx="28" cy="22" r="2.5" fill="#fbbf24" opacity="0.7"/>
        <circle cx="115" cy="18" r="2" fill="#fbbf24" opacity="0.5"/>
        <circle cx="22" cy="100" r="2" fill="#fbbf24" opacity="0.5"/>
        <circle cx="118" cy="95" r="2.5" fill="#fbbf24" opacity="0.6"/>
        <circle cx="10" cy="58" r="1.8" fill="#fbbf24" opacity="0.4"/>
        <circle cx="128" cy="60" r="1.8" fill="#fbbf24" opacity="0.4"/>
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
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 140">
        <!-- Central eUICC chip -->
        <rect x="48" y="48" width="44" height="44" rx="6" fill="rgba(76,29,149,0.4)" stroke="#a78bfa" stroke-width="2"/>
        <text x="70" y="66" fill="white" font-family="system-ui,sans-serif" font-size="8" font-weight="600" text-anchor="middle">eUICC</text>
        <!-- Connected boxes orbit -->
        <rect x="12" y="14" width="36" height="28" rx="5" fill="rgba(6,78,59,0.35)" stroke="#34d399" stroke-width="1.5"/>
        <text x="30" y="32" fill="white" font-family="system-ui,sans-serif" font-size="7.5" font-weight="600" text-anchor="middle">SM-DP+</text>
        <rect x="92" y="14" width="36" height="28" rx="5" fill="rgba(120,53,15,0.3)" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="110" y="32" fill="white" font-family="system-ui,sans-serif" font-size="7.5" font-weight="600" text-anchor="middle">SM-DS</text>
        <rect x="52" y="105" width="36" height="28" rx="5" fill="rgba(8,51,68,0.35)" stroke="#22d3ee" stroke-width="1.5"/>
        <text x="70" y="123" fill="white" font-family="system-ui,sans-serif" font-size="7.5" font-weight="600" text-anchor="middle">LPA</text>
        <!-- Connector lines -->
        <line x1="50" y1="42" x2="30" y2="42" stroke="#34d399" stroke-width="1.2" fill="none"/>
        <line x1="90" y1="42" x2="110" y2="42" stroke="#fbbf24" stroke-width="1.2" fill="none"/>
        <line x1="70" y1="92" x2="70" y2="105" stroke="#22d3ee" stroke-width="1.2" fill="none"/>
        <line x1="48" y1="70" x2="30" y2="68" stroke="#34d399" stroke-width="1.2" fill="none"/>
        <line x1="92" y1="70" x2="110" y2="68" stroke="#fbbf24" stroke-width="1.2" fill="none"/>
      </svg>
    </div>
    <div class="simple-card-body">
      <h2>Detailed and Technical</h2>
      <p>Spec-driven. Precise. For engineers and implementers. Every GSMA eSIM specification explained in focused articles.</p>
    </div>
  </a>

</div>

<div align="center" style="margin: 2rem 0 1rem;">

[Back to full homepage →](/)

</div>
