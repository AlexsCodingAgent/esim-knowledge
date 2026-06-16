---
layout: default
title: eUICC.tech — Simple
description: "Two paths into the eSIM RSP knowledge base: illustrated stories for newcomers, or technical deep dives for engineers."
---

<style>
  .simple-hero {
    max-width: 480px;
    margin: 3rem auto 2rem;
  }
  .simple-card {
    display: block;
    border-radius: 20px;
    padding: 40px 24px 36px;
    text-decoration: none;
    text-align: center;
    margin-bottom: 24px;
    transition: transform 0.2s;
  }
  .simple-card:hover {
    transform: translateY(-3px);
  }
  .simple-card svg {
    width: 100px;
    height: 100px;
    margin-bottom: 20px;
  }
  .simple-card h2 {
    margin: 0 0 8px;
    font-size: 1.5rem;
    color: #e8eef5;
  }
  .simple-card p {
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
</style>

<div class="simple-hero">

  <a href="docs/articles/kids/" class="simple-card card-illustrated">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
      <g transform="translate(50,48)">
        <path d="M0,2 L-38,-16 L-38,-38 L0,-20 Z" fill="#7c3aed" opacity="0.7"/>
        <path d="M0,2 L38,-16 L38,-38 L0,-20 Z" fill="#a78bfa" opacity="0.45"/>
        <path d="M0,0 L-32,-14 L-32,-34 L0,-20 Z" fill="#fbbf24" opacity="0.3"/>
        <path d="M0,0 L32,-14 L32,-34 L0,-20 Z" fill="#34d399" opacity="0.25"/>
        <line x1="0" y1="-38" x2="0" y2="4" stroke="#c4b5fd" stroke-width="2" opacity="0.7"/>
      </g>
      <circle cx="20" cy="18" r="2" fill="#fbbf24" opacity="0.6"/>
      <circle cx="82" cy="15" r="1.5" fill="#fbbf24" opacity="0.5"/>
      <circle cx="18" cy="80" r="1.8" fill="#fbbf24" opacity="0.5"/>
      <circle cx="85" cy="78" r="2" fill="#fbbf24" opacity="0.6"/>
    </svg>
    <h2>Illustrated, Simple</h2>
    <p>Stories, analogies, and emojis. The intuition before the technical detail.</p>
  </a>

  <a href="docs/articles/" class="simple-card card-technical">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
      <rect x="30" y="30" width="40" height="40" rx="6" fill="rgba(76,29,149,0.4)" stroke="#a78bfa" stroke-width="2"/>
      <text x="50" y="46" fill="white" font-family="system-ui,sans-serif" font-size="7" font-weight="600" text-anchor="middle">eUICC</text>
      <rect x="5" y="8" width="30" height="22" rx="5" fill="rgba(6,78,59,0.35)" stroke="#34d399" stroke-width="1.5"/>
      <text x="20" y="22" fill="white" font-family="system-ui,sans-serif" font-size="6" font-weight="600" text-anchor="middle">SM-DP+</text>
      <rect x="65" y="8" width="30" height="22" rx="5" fill="rgba(120,53,15,0.3)" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="80" y="22" fill="white" font-family="system-ui,sans-serif" font-size="6" font-weight="600" text-anchor="middle">SM-DS</text>
      <rect x="35" y="78" width="30" height="22" rx="5" fill="rgba(8,51,68,0.35)" stroke="#22d3ee" stroke-width="1.5"/>
      <text x="50" y="92" fill="white" font-family="system-ui,sans-serif" font-size="6" font-weight="600" text-anchor="middle">LPA</text>
      <line x1="35" y1="38" x2="20" y2="30" stroke="#34d399" stroke-width="1.2"/>
      <line x1="65" y1="38" x2="80" y2="30" stroke="#fbbf24" stroke-width="1.2"/>
      <line x1="50" y1="70" x2="50" y2="78" stroke="#22d3ee" stroke-width="1.2"/>
    </svg>
    <h2>Detailed and Technical</h2>
    <p>Spec-driven. Precise. For engineers and implementers.</p>
  </a>

</div>

<div align="center" style="margin: 2rem 0;">

[Back to full homepage →](/)

</div>
