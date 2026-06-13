---
layout: default
title: eSIM Ecosystem Jobs
description: Browse software engineering and technical roles across the eSIM ecosystem — G+D, Thales, Idemia, 1NCE, KORE, Soracom, and more.
permalink: /careers/
---

<style>
/* Careers page — dark theme, consistent with Midnight */
.careers-wrap {
  max-width: 960px;
  margin: 0 auto;
}
.careers-header {
  margin-bottom: 1.5rem;
}
.careers-header h1 {
  color: #c8d6e5;
  margin-bottom: 0.25rem;
}
.careers-header p {
  color: #8b949e;
  font-size: 0.95rem;
  margin: 0;
}
.careers-filters {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
}
.careers-filters input,
.careers-filters select {
  background: #0d1b2a;
  border: 1px solid #1b3a5c;
  color: #c8d6e5;
  padding: 0.5rem 0.75rem;
  border-radius: 4px;
  font-size: 0.9rem;
  font-family: inherit;
  outline: none;
}
.careers-filters input:focus,
.careers-filters select:focus {
  border-color: #5dade2;
}
.careers-filters input {
  flex: 1 1 200px;
  min-width: 180px;
}
.careers-filters select {
  min-width: 140px;
}
.filter-toggle {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: #85c1e9;
  font-size: 0.85rem;
  cursor: pointer;
  padding: 0.5rem 0;
  user-select: none;
}
.filter-toggle input[type="checkbox"] {
  accent-color: #5dade2;
}
.careers-count {
  color: #8b949e;
  font-size: 0.85rem;
  margin-bottom: 1rem;
}
.job-card {
  background: #0d1b2a;
  border: 1px solid #1b3a5c;
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin-bottom: 0.75rem;
  transition: border-color 0.15s;
}
.job-card:hover {
  border-color: #5dade2;
}
.job-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.job-title {
  color: #5dade2;
  font-weight: 600;
  font-size: 1.05rem;
  text-decoration: none;
}
.job-title:hover {
  text-decoration: underline;
}
.job-company {
  color: #c8d6e5;
  font-size: 0.85rem;
  font-weight: 500;
}
.job-meta {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 0.5rem;
  font-size: 0.8rem;
  color: #8b949e;
}
.job-meta span {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}
.job-tag {
  display: inline-block;
  background: rgba(93, 173, 226, 0.1);
  border: 1px solid rgba(93, 173, 226, 0.2);
  color: #85c1e9;
  padding: 0.15rem 0.5rem;
  border-radius: 3px;
  font-size: 0.75rem;
}
.no-results {
  text-align: center;
  color: #8b949e;
  padding: 3rem 1rem;
}
.careers-footer {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #1b3a5c;
  font-size: 0.8rem;
  color: #8b949e;
}
.careers-footer a {
  color: #5dade2;
}
</style>

<div class="careers-wrap" markdown="0">

<div class="careers-header">
  <h1>eSIM Ecosystem Jobs</h1>
  <p>Software engineering and technical roles across the eSIM industry — last updated 13 June 2026.</p>
</div>

<div class="careers-filters">
  <input type="text" id="jobSearch" placeholder="Search by title, company, or keyword..." oninput="filterJobs()">
  <select id="companyFilter" onchange="filterJobs()">
    <option value="">All Companies</option>
  </select>
  <select id="countryFilter" onchange="filterJobs()">
    <option value="">All Countries</option>
  </select>
  <label class="filter-toggle" title="Only show jobs discovered in the latest refresh">
    <input type="checkbox" id="newFilter" onchange="filterJobs()"> 🆕 Recently Added
  </label>
  <select id="sortOrder" onchange="filterJobs()">
    <option value="newest" selected>Newest First</option>
    <option value="oldest">Oldest First</option>
  </select>
</div>

<div class="careers-count" id="jobCount"></div>

<div id="jobList"></div>

<div class="careers-footer">
  Data scraped from public career portals. <a href="https://euicc.tech">eUICC.tech</a> &middot; Not affiliated with any listed company.
</div>

</div>

<script>
let JOBS = [];

async function init() {
  try {
    const resp = await fetch('/assets/data/jobs.json');
    JOBS = await resp.json();
  } catch (e) {
    document.getElementById('jobList').innerHTML = '<div class="no-results">Could not load job data. Try again later.</div>';
    return;
  }

  // Populate company filter
  const companies = [...new Set(JOBS.map(j => j.company).filter(Boolean))].sort();
  const cSelect = document.getElementById('companyFilter');
  companies.forEach(c => {
    const opt = document.createElement('option');
    opt.value = c;
    opt.textContent = c;
    cSelect.appendChild(opt);
  });

  // Populate country filter
  const countries = [...new Set(JOBS.map(j => j.country).filter(Boolean))].sort();
  const ccSelect = document.getElementById('countryFilter');
  countries.forEach(c => {
    const opt = document.createElement('option');
    opt.value = c;
    opt.textContent = c;
    ccSelect.appendChild(opt);
  });

  filterJobs();
}

function filterJobs() {
  const query = document.getElementById('jobSearch').value.toLowerCase().trim();
  const company = document.getElementById('companyFilter').value;
  const country = document.getElementById('countryFilter').value;
  const newOnly = document.getElementById('newFilter').checked;
  const sortOrder = document.getElementById('sortOrder').value;

  let filtered = JOBS.filter(j => {
    if (company && j.company !== company) return false;
    if (country && j.country !== country) return false;
    if (newOnly && !j.new) return false;
    if (query) {
      const txt = (j.title + ' ' + j.company + ' ' + j.department + ' ' + j.teaser + ' ' + (j.city || '')).toLowerCase();
      if (!txt.includes(query)) return false;
    }
    return true;
  });

  // Sort by date
  filtered.sort((a, b) => {
    const da = a.date || '', db = b.date || '';
    return sortOrder === 'newest' ? db.localeCompare(da) : da.localeCompare(db);
  });

  document.getElementById('jobCount').textContent = `Showing ${filtered.length} of ${JOBS.length} positions`;

  const list = document.getElementById('jobList');
  if (filtered.length === 0) {
    list.innerHTML = '<div class="no-results">No positions match your filters.</div>';
    return;
  }

  list.innerHTML = filtered.map(j => {
    const location = [j.city, j.country].filter(Boolean).join(', ') || 'Remote / Various';
    const deptTag = j.department ? `<span class="job-tag">${esc(j.department)}</span>` : '';
    const scheduleTag = j.schedule ? `<span class="job-tag">${esc(j.schedule)}</span>` : '';
    const date = j.date ? j.date.substring(0, 10) : '';

    return `<div class="job-card">
      <div class="job-card-header">
        <div>
          <a class="job-title" href="${esc(j.url || '#')}" target="_blank" rel="noopener">${esc(j.title)}</a>
          <div class="job-company">${esc(j.company)}</div>
        </div>
        <div>${deptTag} ${scheduleTag}</div>
      </div>
      <div class="job-meta">
        <span>📍 ${esc(location)}</span>
        ${date ? `<span>📅 ${date}</span>` : ''}
        ${j.employment ? `<span>💼 ${esc(j.employment)}</span>` : ''}
      </div>
    </div>`;
  }).join('');
}

function esc(s) {
  if (!s) return '';
  const div = document.createElement('div');
  div.textContent = s;
  return div.innerHTML;
}

document.addEventListener('DOMContentLoaded', init);
</script>
