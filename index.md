---
layout: default
title: eUICC.tech
description: "Comprehensive technical knowledge base covering 12 GSMA eSIM RSP specifications — SGP.02, SGP.22, SGP.32 and more. 84+ articles on eSIM architecture, profile download, IoT provisioning, and conformance testing."
---

<div align="center">

<h1>eUICC.tech</h1>

<h3>Deep Dives Into GSMA eSIM Remote SIM Provisioning</h3>

*84 articles · 12 specifications · 83 illustrated guides · Built from primary source GSMA specs*

</div>

eUICC.tech is a technical reference for engineers, testers, and implementers working with GSMA eSIM specifications. If you need to understand how Remote SIM Provisioning (RSP) works — the eUICC architecture, profile download flows, certificate hierarchies, or conformance testing requirements — the answers are here, sourced from the primary GSMA documents.

The site covers the full eSIM ecosystem: consumer RSP (SGP.22) for phones and wearables, IoT provisioning (SGP.32) for headless devices, M2M push-model architecture (SGP.02), and manufacturing-time profile loading (SGP.41 IFPP). Supporting specs on EID numbering (SGP.29), test infrastructure (SGP.23), EUICC security evaluation (SGP.25), and test certificates (SGP.26) are also covered in depth.

Every article links to specific sections of the corresponding GSMA specification, so you can verify claims and dig deeper. No vendor marketing, no platform lock-in — just the protocols as specified.

---

<style>
  .home-cards {
    max-width: 480px;
    margin: 2rem auto;
  }
  .home-card {
    display: block;
    border-radius: 20px;
    padding: 40px 24px 36px;
    text-decoration: none;
    text-align: center;
    margin-bottom: 24px;
    transition: transform 0.2s;
  }
  .home-card:hover {
    transform: translateY(-3px);
  }
  .home-card svg {
    width: 100px;
    height: 100px;
    margin-bottom: 20px;
  }
  .home-card h2 {
    margin: 0 0 8px;
    font-size: 1.5rem;
    color: #e8eef5;
  }
  .home-card p {
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

<div class="home-cards">

  <a href="docs/articles/kids/" class="home-card card-illustrated">
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

  <a href="docs/articles/" class="home-card card-technical">
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

---

## What's Inside

- **[SGP.22 v2.7](docs/articles/sgp22/)** : Consumer eSIM RSP: 12 articles

- **[SGP.22 v3.x](docs/articles/sgp22-v3/)** : Unified RSP (the fork) : 12 articles

- **[SGP.32 / SGP.31](docs/articles/sgp32/)** : IoT eSIM: 12 articles

- **[SGP.02 v4.2](docs/articles/sgp02/)** : M2M eSIM (legacy push model) : 12 articles

- **[SGP.41](docs/articles/sgp41/)** : In-Factory Profile Provisioning: 5 articles

- **[SGP.29](docs/articles/sgp29/)** : EID Definition & Assignment: 5 articles

- **[SGP.23 / SGP.23-1](docs/articles/sgp23/)** : RSP Conformance Testing: 10 articles

- **[SGP.33-3](docs/articles/sgp33-3/)** : eIM Test Specification: 5 articles

- **[SGP.25](docs/articles/sgp25/)** : eUICC Protection Profile: 5 articles

- **[SGP.26](docs/articles/sgp26/)** : RSP Test Certificates: 5 articles

---

## Quick Start

**New to eSIM?** Start with the [Guided Path](docs/articles/sgp22/00-sgp22-overview) : 7 articles that take you from zero to understanding the full RSP architecture.

**Prefer stories?** Jump to the [Illustrated Edition](docs/articles/kids/) : every concept explained through analogies, emojis, and illustrations.

**Need a specific spec?** Browse the [full article index](docs/articles/) or search by topic.

**Quick lookup?** Try the [Glossary](docs/glossary) for 60+ terms defined.

---

<div align="center">

*Sources: GSMA SGP.02 v4.2 · SGP.22 v2.7 · SGP.22 v3.1 · SGP.23 v1.16 · SGP.23-1 v3.1.3 · SGP.25 v2.1 · SGP.26 v3.0.2 · SGP.29 v1.1 · SGP.31 v1.3 · SGP.32 v1.3 · SGP.33-3 v1.2 · SGP.41 v1.0*

<a href="/docs/glossary">Glossary</a> · <a href="/docs/prerequisites">Prerequisites</a> · <a href="/docs/standards-map">Standards Map</a> · <a href="/ai">AI Index</a> · <a href="/careers">Jobs</a>

</div>
