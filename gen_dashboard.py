#!/usr/bin/env python3
"""
Generates a self-contained Jira epic dashboard HTML file.

Usage:
    python gen_dashboard.py --output PATH [--data-dir DIR] [--jira-url URL]

Arguments:
    --output PATH      Where to write the HTML file (required)
    --data-dir DIR     Directory containing epics_clean_Q*.json files (default: /tmp)
    --jira-url URL     Base URL for Jira issue links (default: https://pointdigitalfinance.atlassian.net)

The script auto-discovers all epics_clean_Q{N}_{YYYY}.json files in --data-dir,
sorts them chronologically (Q1-Q4 within each year), and embeds them in the HTML.

Charts:
  - Per-Team Breakdown: one mini-chart per team showing Feature vs Tech Debt for both quarters
  - Monthly Timeline: epics completed per month, Q_A vs Q_B
  - Feature vs Tech Debt Split: stacked bars per team, both quarters
  All chart bars are clickable and open Jira filtered to those exact epics via JQL.
"""
import argparse
import glob
import json
import os
import re
import sys


EXCLUDE_STATUSES = {
    'closed - will not do',
    'closed - duplicate',
    "won't do",
    "won't fix",
}


def parse_quarter_key(filename):
    """Extract (year, quarter_num) from filename like epics_clean_Q1_2026.json."""
    m = re.search(r'epics_clean_(Q(\d))_(\d{4})\.json', os.path.basename(filename))
    if not m:
        return None
    return int(m.group(3)), int(m.group(2)), m.group(1) + '_' + m.group(3)


def load_quarters(data_dir):
    """Discover and load all quarter JSON files, sorted chronologically."""
    pattern = os.path.join(data_dir, 'epics_clean_Q*.json')
    files = glob.glob(pattern)
    if not files:
        print(f"ERROR: No epics_clean_Q*.json files found in {data_dir}", file=sys.stderr)
        sys.exit(1)

    parsed = []
    for f in files:
        result = parse_quarter_key(f)
        if result:
            year, qnum, qkey = result
            parsed.append((year, qnum, qkey, f))
    parsed.sort(key=lambda x: (x[0], x[1]))

    quarters_order = []
    quarters_data = {}
    quarters_label = {}

    for year, qnum, qkey, filepath in parsed:
        with open(filepath) as fh:
            raw = json.load(fh)
        valid = [e for e in raw if e.get('status', '').lower() not in EXCLUDE_STATUSES]
        quarters_order.append(qkey)
        quarters_data[qkey] = valid
        quarters_label[qkey] = f'Q{qnum} {year}'

    return quarters_order, quarters_data, quarters_label


def build_html(quarters_order, quarters_data, quarters_label, jira_url):
    """Build the complete self-contained HTML string."""

    # Build JS data block (unquoted keys for JS object literal)
    js_lines = []
    for q in quarters_order:
        js_lines.append(f'  {q}: {json.dumps(quarters_data[q], separators=(",", ":"))}')
    js_data = 'const ALL_EPICS = {\n' + ',\n'.join(js_lines) + '\n};'

    def make_options(selected_key):
        opts = []
        for q in quarters_order:
            sel = ' selected' if q == selected_key else ''
            opts.append(f'<option value="{q}"{sel}>{quarters_label[q]}</option>')
        return '\n      '.join(opts)

    default_a = quarters_order[-2] if len(quarters_order) >= 2 else quarters_order[0]
    default_b = quarters_order[-1]
    options_a = make_options(default_a)
    options_b = make_options(default_b)

    quarter_labels_js = json.dumps(quarters_label)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Jira Epic Dashboard — Quarter Comparison</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f0f2f5;color:#1e293b;font-size:14px;}}
header{{background:linear-gradient(135deg,#0f4c9e 0%,#1a6fd6 100%);color:#fff;padding:20px 28px;display:flex;align-items:center;gap:16px;}}
header h1{{font-size:20px;font-weight:700;letter-spacing:-.3px;}}
header p{{font-size:12px;opacity:.8;margin-top:2px;}}
.controls{{background:#fff;border-bottom:1px solid #e2e8f0;padding:14px 28px;display:flex;align-items:center;gap:24px;flex-wrap:wrap;}}
.ctrl-group{{display:flex;align-items:center;gap:8px;}}
.ctrl-group label{{font-size:12px;font-weight:600;color:#64748b;text-transform:uppercase;letter-spacing:.5px;}}
select.q-select{{padding:6px 10px;border:1px solid #cbd5e1;border-radius:6px;font-size:13px;background:#fff;cursor:pointer;color:#1e293b;}}
.vs-badge{{background:#e2e8f0;color:#64748b;font-size:11px;font-weight:700;padding:3px 8px;border-radius:12px;}}
.type-tabs{{display:flex;gap:4px;background:#f1f5f9;padding:3px;border-radius:8px;}}
.type-tab{{padding:5px 14px;border:none;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;background:transparent;color:#64748b;transition:all .15s;}}
.type-tab.active{{background:#fff;color:#1e293b;box-shadow:0 1px 3px rgba(0,0,0,.12);}}
.main{{padding:20px 28px;display:flex;flex-direction:column;gap:20px;}}
.stats-row{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;}}
.stat-card{{background:#fff;border-radius:10px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.06);}}
.stat-card .lbl{{font-size:11px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px;}}
.stat-card .val{{font-size:26px;font-weight:700;line-height:1;}}
.stat-card .sub{{font-size:11px;color:#94a3b8;margin-top:4px;}}
.stat-card.a .val{{color:#2563eb;}}
.stat-card.b .val{{color:#ea580c;}}
.stat-card.feat .val{{color:#16a34a;}}
.stat-card.td .val{{color:#9333ea;}}
.charts-row{{display:grid;grid-template-columns:1fr 1fr;gap:16px;}}
@media(max-width:900px){{.charts-row{{grid-template-columns:1fr;}}}}
.card{{background:#fff;border-radius:10px;padding:20px;box-shadow:0 1px 3px rgba(0,0,0,.06);}}
.card h2{{font-size:13px;font-weight:700;color:#475569;margin-bottom:16px;text-transform:uppercase;letter-spacing:.4px;}}
.card .card-subtitle{{font-size:11px;font-weight:400;color:#94a3b8;text-transform:none;letter-spacing:0;margin-left:8px;}}
.chart-wrap{{overflow-x:auto;}}
svg text{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;}}
.legend{{display:flex;gap:16px;font-size:11px;color:#64748b;margin-top:10px;flex-wrap:wrap;}}
.legend-dot{{width:10px;height:10px;border-radius:2px;display:inline-block;margin-right:4px;vertical-align:middle;}}
/* Per-team mini charts */
.team-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;}}
.team-mini{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:14px;}}
.team-mini-title{{font-size:12px;font-weight:700;color:#334155;margin-bottom:10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}}
.team-mini-legend{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px;font-size:10px;color:#64748b;}}
.drill-hint{{font-size:10px;color:#94a3b8;margin-top:4px;font-style:italic;}}
/* Main table */
table{{width:100%;border-collapse:collapse;font-size:12px;}}
thead th{{background:#f8fafc;padding:8px 10px;text-align:left;font-size:11px;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:.4px;border-bottom:2px solid #e2e8f0;cursor:pointer;user-select:none;white-space:nowrap;}}
thead th:hover{{background:#f1f5f9;}}
thead th .sort-arrow{{display:inline-block;margin-left:4px;opacity:.4;font-size:9px;}}
thead th.sorted .sort-arrow{{opacity:1;}}
tbody tr:hover{{background:#f8fafc;}}
tbody td{{padding:7px 10px;border-bottom:1px solid #f1f5f9;vertical-align:top;}}
.badge{{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.3px;}}
.badge-a{{background:#dbeafe;color:#1d4ed8;}}
.badge-b{{background:#fff7ed;color:#c2410c;}}
.badge-feat{{background:#dcfce7;color:#15803d;}}
.badge-td{{background:#f3e8ff;color:#7e22ce;}}
.no-data{{color:#94a3b8;font-style:italic;padding:20px 0;text-align:center;}}
.clickable-bar{{cursor:pointer;}}
.clickable-bar:hover{{opacity:.8;}}
#tooltip{{position:fixed;pointer-events:none;background:rgba(15,23,42,.92);color:#fff;font-size:11px;padding:7px 11px;border-radius:6px;display:none;z-index:999;max-width:240px;line-height:1.5;}}
</style>
</head>
<body>
<div id="tooltip"></div>
<header>
  <div>
    <h1>📊 Jira Epic Dashboard</h1>
    <p>Quarter-over-quarter epic completion · Click any bar to open in Jira</p>
  </div>
</header>
<div class="controls">
  <div class="ctrl-group">
    <label>Compare</label>
    <select class="q-select" id="selA" onchange="refresh()">
      {options_a}
    </select>
    <span class="vs-badge">VS</span>
    <select class="q-select" id="selB" onchange="refresh()">
      {options_b}
    </select>
  </div>
  <div class="ctrl-group">
    <label>Type</label>
    <div class="type-tabs">
      <button class="type-tab active" data-type="all" onclick="setType('all')">All</button>
      <button class="type-tab" data-type="Feature" onclick="setType('Feature')">Feature</button>
      <button class="type-tab" data-type="Tech Debt" onclick="setType('Tech Debt')">Tech Debt</button>
    </div>
  </div>
</div>
<div class="main">
  <div class="stats-row" id="statsRow"></div>

  <!-- Per-team breakdown: one mini chart per team -->
  <div class="card">
    <h2>Per-Team Breakdown <span class="card-subtitle" id="perTeamSubtitle"></span></h2>
    <p class="drill-hint" style="margin-bottom:12px;">Click any bar to open those epics in Jira</p>
    <div class="team-grid" id="perTeamGrid"></div>
    <div class="legend" id="perTeamLegend"></div>
  </div>

  <!-- Monthly timeline + type split side by side -->
  <div class="charts-row">
    <div class="card">
      <h2>Monthly Timeline</h2>
      <p class="drill-hint" style="margin-bottom:8px;">Click any bar to open in Jira</p>
      <div class="chart-wrap" id="monthChart"></div>
      <div class="legend" id="monthLegend"></div>
    </div>
    <div class="card">
      <h2>Feature vs Tech Debt Split</h2>
      <p class="drill-hint" style="margin-bottom:8px;">Click any bar to open in Jira</p>
      <div class="chart-wrap" id="typeChart"></div>
      <div class="legend" id="typeLegend"></div>
    </div>
  </div>

  <!-- Epic table -->
  <div class="card">
    <h2>Epic Details <span id="tableCount" style="font-size:11px;font-weight:400;color:#94a3b8;text-transform:none;letter-spacing:0;"></span></h2>
    <table id="epicTable">
      <thead>
        <tr>
          <th onclick="doSort('key')">Key <span class="sort-arrow">↕</span></th>
          <th onclick="doSort('project_name')">Team <span class="sort-arrow">↕</span></th>
          <th onclick="doSort('summary')">Summary <span class="sort-arrow">↕</span></th>
          <th onclick="doSort('type')">Type <span class="sort-arrow">↕</span></th>
          <th onclick="doSort('assignee')">Assignee <span class="sort-arrow">↕</span></th>
          <th onclick="doSort('resdate')">Resolved <span class="sort-arrow">↕</span></th>
          <th>Quarter</th>
        </tr>
      </thead>
      <tbody id="epicTbody"></tbody>
    </table>
  </div>
</div>

<script>
{js_data}

const QUARTER_LABELS = {quarter_labels_js};
const JIRA_URL = '{jira_url}';
const COL_A = '#2563eb', COL_B = '#ea580c';
const COL_FA = '#3b82f6', COL_TDA = '#818cf8', COL_FB = '#f97316', COL_TDB = '#fbbf24';
let sortKey = 'resdate', sortDir = 1, activeType = 'all';

// ─── JQL drill-down registry ───────────────────────────────────────────────
// Each chart bar registers its epic keys here; clicking opens Jira with those keys.
let _jqlMap = {{}};
let _jqlCnt = 0;

function _reg(keys, tipLabel) {{
  const id = 'b' + (_jqlCnt++);
  _jqlMap[id] = {{ keys, tipLabel }};
  return id;
}}

function drillDown(id) {{
  const d = _jqlMap[id];
  if (!d || !d.keys.length) return;
  const keyList = d.keys.map(k => '"' + k + '"').join(',');
  const jql = 'issueKey in (' + keyList + ') ORDER BY resolutiondate ASC';
  window.open(JIRA_URL + '/issues/?jql=' + encodeURIComponent(jql), '_blank');
}}

// ─── Helpers ───────────────────────────────────────────────────────────────
const tip = document.getElementById('tooltip');
function showTip(e, html) {{ tip.style.display = 'block'; tip.innerHTML = html; moveTip(e); }}
function moveTip(e) {{ tip.style.left = (e.clientX + 14) + 'px'; tip.style.top = (e.clientY - 10) + 'px'; }}
function hideTip() {{ tip.style.display = 'none'; }}

function abbrev(name) {{
  return (name || '?')
    .replace('Customer Engagement', 'CE')
    .replace('QA Automation  Dashboard', 'QA Auto')
    .replace('QA Automation Dashboard', 'QA Auto')
    .replace('Decisioning', 'DEC')
    .replace('Growth', 'GRO')
    .replace('Security', 'SEC')
    .replace('Servicing', 'SVCG')
    .replace('Rapid Response', 'RARE')
    .replace('Workflow', 'WF')
    .replace('Analytics', 'AN')
    .replace('AWS Migration Project', 'AMP')
    .replace('Feather AI Voice Agents', 'FAV')
    .replace('AI CX Team', 'ACT');
}}

function setType(t) {{
  activeType = t;
  document.querySelectorAll('.type-tab').forEach(b => b.classList.toggle('active', b.dataset.type === t));
  refresh();
}}

function getData(qKey) {{
  const raw = ALL_EPICS[qKey] || [];
  return activeType === 'all' ? raw : raw.filter(e => e.type === activeType);
}}

function countBy(arr, key) {{
  const m = {{}};
  arr.forEach(e => {{ const k = e[key] || '?'; m[k] = (m[k] || 0) + 1; }});
  return m;
}}

// ─── SVG bar primitive ────────────────────────────────────────────────────
function svgBar(x, y, w, h, fill, jqlId, tipHtml) {{
  const safeH = Math.max(2, h);
  const safeY = y - (safeH - h); // keep bottom aligned
  const events = jqlId
    ? ` onclick="drillDown('${{jqlId}}')" onmouseenter="showTip(event,'${{tipHtml.replace(/'/g,'&#39;')}}')" onmouseleave="hideTip()" onmousemove="moveTip(event)" class="clickable-bar"`
    : ` onmouseenter="showTip(event,'${{tipHtml.replace(/'/g,'&#39;')}}')" onmouseleave="hideTip()" onmousemove="moveTip(event)"`;
  return `<rect x="${{x}}" y="${{safeY}}" width="${{w}}" height="${{safeH}}" fill="${{fill}}" rx="2"${{events}}/>`;
}}

// ─── Stats summary ────────────────────────────────────────────────────────
function updateStats(dA, dB, lA, lB) {{
  const fA = dA.filter(e => e.type === 'Feature').length, tdA = dA.filter(e => e.type === 'Tech Debt').length;
  const fB = dB.filter(e => e.type === 'Feature').length, tdB = dB.filter(e => e.type === 'Tech Debt').length;
  const delta = dB.length - dA.length, sign = delta >= 0 ? '+' : '';
  document.getElementById('statsRow').innerHTML = `
    <div class="stat-card a"><div class="lbl">${{lA}}</div><div class="val">${{dA.length}}</div><div class="sub">F:${{fA}} · TD:${{tdA}}</div></div>
    <div class="stat-card b"><div class="lbl">${{lB}}</div><div class="val">${{dB.length}}</div><div class="sub">F:${{fB}} · TD:${{tdB}}</div></div>
    <div class="stat-card feat"><div class="lbl">Features</div><div class="val">${{fA + fB}}</div><div class="sub">${{lA}}:${{fA}} · ${{lB}}:${{fB}}</div></div>
    <div class="stat-card td"><div class="lbl">Tech Debt</div><div class="val">${{tdA + tdB}}</div><div class="sub">${{lA}}:${{tdA}} · ${{lB}}:${{tdB}}</div></div>
    <div class="stat-card"><div class="lbl">Change</div><div class="val" style="color:${{delta >= 0 ? '#16a34a' : '#dc2626'}}">${{sign}}${{delta}}</div><div class="sub">${{lA}} → ${{lB}}</div></div>`;
}}

// ─── Per-team mini charts ─────────────────────────────────────────────────
function buildPerTeamCharts(qA, qB, lA, lB) {{
  const rawA = ALL_EPICS[qA] || [], rawB = ALL_EPICS[qB] || [];
  // Collect all teams across both quarters
  const teamSet = new Set([...rawA, ...rawB].map(e => e.project_name || '?'));
  const teams = [...teamSet].sort();

  document.getElementById('perTeamSubtitle').textContent = `(${{teams.length}} teams)`;
  document.getElementById('perTeamLegend').innerHTML =
    `<span><span class="legend-dot" style="background:${{COL_FA}}"></span>${{lA}} Feature</span>
     <span><span class="legend-dot" style="background:${{COL_TDA}}"></span>${{lA}} Tech Debt</span>
     <span><span class="legend-dot" style="background:${{COL_FB}}"></span>${{lB}} Feature</span>
     <span><span class="legend-dot" style="background:${{COL_TDB}}"></span>${{lB}} Tech Debt</span>`;

  const grid = document.getElementById('perTeamGrid');
  grid.innerHTML = '';

  teams.forEach(team => {{
    const tA = rawA.filter(e => e.project_name === team);
    const tB = rawB.filter(e => e.project_name === team);
    const fAarr = tA.filter(e => e.type === 'Feature');
    const tdAarr = tA.filter(e => e.type === 'Tech Debt');
    const fBarr = tB.filter(e => e.type === 'Feature');
    const tdBarr = tB.filter(e => e.type === 'Tech Debt');

    const fA = fAarr.length, tdA = tdAarr.length;
    const fB = fBarr.length, tdB = tdBarr.length;
    const maxV = Math.max(1, fA + tdA, fB + tdB);

    // Mini SVG: 4 bars per team
    // Layout: [FA][TDA]  gap  [FB][TDB]
    const bW = 26, gap = 3, grpGap = 14;
    const padL = 8, padT = 10, padB = 24;
    const W = padL + 2 * (bW * 2 + gap) + grpGap + padL;
    const H = 100;
    const botY = H - padB;
    const scaleH = v => (botY - padT) * v / maxV;

    const idFA = _reg(fAarr.map(e => e.key), `${{lA}} Feature: ${{fA}} epics`);
    const idTDA = _reg(tdAarr.map(e => e.key), `${{lA}} Tech Debt: ${{tdA}} epics`);
    const idFB = _reg(fBarr.map(e => e.key), `${{lB}} Feature: ${{fB}} epics`);
    const idTDB = _reg(tdBarr.map(e => e.key), `${{lB}} Tech Debt: ${{tdB}} epics`);

    let bars = '';
    // Q_A group
    const xFA = padL;
    const xTDA = padL + bW + gap;
    bars += svgBar(xFA, botY - scaleH(fA), bW, scaleH(fA), COL_FA, fA > 0 ? idFA : null,
      `${{lA}} Feature: ${{fA}} epic${{fA !== 1 ? 's' : ''}}`);
    bars += svgBar(xTDA, botY - scaleH(tdA), bW, scaleH(tdA), COL_TDA, tdA > 0 ? idTDA : null,
      `${{lA}} Tech Debt: ${{tdA}} epic${{tdA !== 1 ? 's' : ''}}`);

    // Q_B group
    const xFB = padL + bW * 2 + gap + grpGap;
    const xTDB = xFB + bW + gap;
    bars += svgBar(xFB, botY - scaleH(fB), bW, scaleH(fB), COL_FB, fB > 0 ? idFB : null,
      `${{lB}} Feature: ${{fB}} epic${{fB !== 1 ? 's' : ''}}`);
    bars += svgBar(xTDB, botY - scaleH(tdB), bW, scaleH(tdB), COL_TDB, tdB > 0 ? idTDB : null,
      `${{lB}} Tech Debt: ${{tdB}} epic${{tdB !== 1 ? 's' : ''}}`);

    // Separator line between quarter groups
    const sepX = padL + bW * 2 + gap + grpGap / 2;
    const separator = `<line x1="${{sepX}}" y1="${{padT}}" x2="${{sepX}}" y2="${{botY}}" stroke="#e2e8f0" stroke-dasharray="3,2"/>`;

    // X-axis labels
    const midA = padL + bW + gap / 2;
    const midB = xFB + bW + gap / 2;
    const lbls = `<text x="${{midA}}" y="${{H - 10}}" text-anchor="middle" font-size="9" fill="#94a3b8">${{lA}}</text>
                  <text x="${{midB}}" y="${{H - 10}}" text-anchor="middle" font-size="9" fill="#94a3b8">${{lB}}</text>`;

    // Gridline at max
    const grid_svg = `<line x1="${{padL}}" y1="${{padT}}" x2="${{W - padL}}" y2="${{padT}}" stroke="#f1f5f9"/>
      <text x="${{padL - 2}}" y="${{padT + 4}}" text-anchor="end" font-size="8" fill="#cbd5e1">${{maxV}}</text>`;

    const div = document.createElement('div');
    div.className = 'team-mini';
    div.innerHTML = `
      <div class="team-mini-title" title="${{team}}">${{team}}</div>
      <svg width="${{W}}" height="${{H}}">${{grid_svg}}${{separator}}${{bars}}${{lbls}}</svg>
      <div class="team-mini-legend">
        <span><b style="color:#2563eb">${{fA + tdA}}</b> ${{lA}}</span>
        <span><b style="color:#ea580c">${{fB + tdB}}</b> ${{lB}}</span>
      </div>`;
    grid.appendChild(div);
  }});
}}

// ─── Monthly timeline chart ────────────────────────────────────────────────
function buildMonthChart(dA, dB, lA, lB) {{
  const all = [...dA.map(e => ({{...e, _q: 'A'}})), ...dB.map(e => ({{...e, _q: 'B'}}))];
  if (!all.length) {{ document.getElementById('monthChart').innerHTML = '<div class="no-data">No data</div>'; return; }}

  // Group epics by month and quarter
  const monthMap = {{}};
  all.forEach(e => {{
    if (!e.resdate) return;
    const m = e.resdate.slice(0, 7);
    if (!monthMap[m]) monthMap[m] = {{ A: [], B: [] }};
    monthMap[m][e._q].push(e);
  }});
  const mKeys = Object.keys(monthMap).sort();
  if (!mKeys.length) {{ document.getElementById('monthChart').innerHTML = '<div class="no-data">No data</div>'; return; }}

  const maxV = Math.max(1, ...mKeys.map(m => Math.max(monthMap[m].A.length, monthMap[m].B.length)));
  const cW = 22, gap = 4, gW = cW * 2 + gap + 12;
  const padL = 36, padR = 10, padT = 10, padB = 36;
  const W = padL + mKeys.length * gW + padR, H = 180;
  const botY = H - padB;
  const scaleY = v => padT + (botY - padT) * (1 - v / maxV);

  let bars = '', labels = '', grid = '';
  for (let i = 0; i <= 4; i++) {{
    const v = Math.round(maxV * i / 4), y = scaleY(v);
    grid += `<line x1="${{padL}}" y1="${{y}}" x2="${{W - padR}}" y2="${{y}}" stroke="#e2e8f0"/>`;
    grid += `<text x="${{padL - 4}}" y="${{y + 4}}" text-anchor="end" font-size="9" fill="#94a3b8">${{v}}</text>`;
  }}

  mKeys.forEach((m, i) => {{
    const x = padL + i * gW;
    const arrA = monthMap[m].A, arrB = monthMap[m].B;
    const va = arrA.length, vb = arrB.length;

    const idA = _reg(arrA.map(e => e.key), `${{lA}} ${{m}}: ${{va}} epic${{va !== 1 ? 's' : ''}}`);
    const idB = _reg(arrB.map(e => e.key), `${{lB}} ${{m}}: ${{vb}} epic${{vb !== 1 ? 's' : ''}}`);

    bars += svgBar(x, scaleY(va), cW, botY - scaleY(va), COL_A, va > 0 ? idA : null,
      `${{lA}} ${{m}}: ${{va}} epic${{va !== 1 ? 's' : ''}}. Click to open in Jira`);
    bars += svgBar(x + cW + gap, scaleY(vb), cW, botY - scaleY(vb), COL_B, vb > 0 ? idB : null,
      `${{lB}} ${{m}}: ${{vb}} epic${{vb !== 1 ? 's' : ''}}. Click to open in Jira`);

    const parts = m.split('-'), lbl = parts[1] + '/' + parts[0].slice(2);
    labels += `<text x="${{x + cW}}" y="${{H - padB + 14}}" text-anchor="middle" font-size="9" fill="#64748b">${{lbl}}</text>`;
    if (i % 2 === 0) labels += `<text x="${{x + cW}}" y="${{H - padB + 24}}" text-anchor="middle" font-size="8.5" fill="#94a3b8">${{parts[0]}}</text>`;
  }});

  document.getElementById('monthChart').innerHTML =
    `<svg width="${{W}}" height="${{H}}" style="min-width:${{W}}px">${{grid}}${{bars}}${{labels}}</svg>`;
  document.getElementById('monthLegend').innerHTML =
    `<span><span class="legend-dot" style="background:${{COL_A}}"></span>${{lA}}</span>
     <span><span class="legend-dot" style="background:${{COL_B}}"></span>${{lB}}</span>`;
}}

// ─── Feature vs Tech Debt stacked chart (per team) ────────────────────────
function buildTypeChart(qA, qB, lA, lB) {{
  const rawA = ALL_EPICS[qA] || [], rawB = ALL_EPICS[qB] || [];
  const teamMap = {{}};
  [...rawA, ...rawB].forEach(e => {{
    const t = e.project_name || '?';
    if (!teamMap[t]) teamMap[t] = {{ fA: [], tdA: [], fB: [], tdB: [] }};
  }});
  rawA.forEach(e => {{
    const t = e.project_name || '?';
    if (e.type === 'Feature') teamMap[t].fA.push(e); else teamMap[t].tdA.push(e);
  }});
  rawB.forEach(e => {{
    const t = e.project_name || '?';
    if (e.type === 'Feature') teamMap[t].fB.push(e); else teamMap[t].tdB.push(e);
  }});

  const teams = Object.keys(teamMap).sort((a, b) => {{
    const ta = teamMap[a], tb = teamMap[b];
    return (tb.fA.length + tb.tdA.length + tb.fB.length + tb.tdB.length) -
           (ta.fA.length + ta.tdA.length + ta.fB.length + ta.tdB.length);
  }}).slice(0, 14);

  if (!teams.length) {{ document.getElementById('typeChart').innerHTML = '<div class="no-data">No data</div>'; return; }}

  const maxV = Math.max(1, ...teams.map(t => {{
    const m = teamMap[t];
    return Math.max(m.fA.length + m.tdA.length, m.fB.length + m.tdB.length);
  }}));

  const bW = 24, gap = 4, gW = bW * 2 + gap + 14;
  const padL = 120, padR = 20, padT = 10, padB = 30;
  const W = padL + teams.length * gW + padR, H = 200;
  const botY = H - padB;
  const scaleY = v => padT + (botY - padT) * (1 - v / maxV);

  let bars = '', labels = '', grid = '';
  for (let i = 0; i <= 4; i++) {{
    const v = Math.round(maxV * i / 4), y = scaleY(v);
    grid += `<line x1="${{padL}}" y1="${{y}}" x2="${{W - padR}}" y2="${{y}}" stroke="#e2e8f0"/>`;
    grid += `<text x="${{padL - 6}}" y="${{y + 4}}" text-anchor="end" font-size="10" fill="#94a3b8">${{v}}</text>`;
  }}

  teams.forEach((t, i) => {{
    const m = teamMap[t], x = padL + i * gW;
    const totalA = m.fA.length + m.tdA.length, totalB = m.fB.length + m.tdB.length;

    if (totalA > 0) {{
      // Feature portion (bottom of stack)
      const idFA = _reg(m.fA.map(e => e.key), `${{lA}} ${{t}} Feature: ${{m.fA.length}}`);
      bars += svgBar(x, scaleY(m.fA.length), bW, botY - scaleY(m.fA.length), COL_FA,
        m.fA.length > 0 ? idFA : null,
        `${{abbrev(t)}} ${{lA}} Feature: ${{m.fA.length}}. Click to open in Jira`);
      // Tech Debt portion (top of stack = stacked above Feature)
      if (m.tdA.length > 0) {{
        const idTDA = _reg(m.tdA.map(e => e.key), `${{lA}} ${{t}} Tech Debt: ${{m.tdA.length}}`);
        bars += svgBar(x, scaleY(totalA), bW, scaleY(m.fA.length) - scaleY(totalA), COL_TDA,
          idTDA, `${{abbrev(t)}} ${{lA}} Tech Debt: ${{m.tdA.length}}. Click to open in Jira`);
      }}
    }} else {{
      bars += `<rect x="${{x}}" y="${{botY - 2}}" width="${{bW}}" height="2" fill="#e2e8f0" rx="1"/>`;
    }}

    if (totalB > 0) {{
      const idFB = _reg(m.fB.map(e => e.key), `${{lB}} ${{t}} Feature: ${{m.fB.length}}`);
      bars += svgBar(x + bW + gap, scaleY(m.fB.length), bW, botY - scaleY(m.fB.length), COL_FB,
        m.fB.length > 0 ? idFB : null,
        `${{abbrev(t)}} ${{lB}} Feature: ${{m.fB.length}}. Click to open in Jira`);
      if (m.tdB.length > 0) {{
        const idTDB = _reg(m.tdB.map(e => e.key), `${{lB}} ${{t}} Tech Debt: ${{m.tdB.length}}`);
        bars += svgBar(x + bW + gap, scaleY(totalB), bW, scaleY(m.fB.length) - scaleY(totalB), COL_TDB,
          idTDB, `${{abbrev(t)}} ${{lB}} Tech Debt: ${{m.tdB.length}}. Click to open in Jira`);
      }}
    }} else {{
      bars += `<rect x="${{x + bW + gap}}" y="${{botY - 2}}" width="${{bW}}" height="2" fill="#e2e8f0" rx="1"/>`;
    }}

    labels += `<text x="${{x + bW}}" y="${{H - padB + 16}}" text-anchor="middle" font-size="9.5" fill="#64748b">${{abbrev(t)}}</text>`;
  }});

  document.getElementById('typeChart').innerHTML =
    `<svg width="${{W}}" height="${{H}}" style="min-width:${{W}}px">${{grid}}${{bars}}${{labels}}</svg>`;
  document.getElementById('typeLegend').innerHTML =
    `<span><span class="legend-dot" style="background:${{COL_FA}}"></span>${{lA}} Feature</span>
     <span><span class="legend-dot" style="background:${{COL_TDA}}"></span>${{lA}} Tech Debt</span>
     <span><span class="legend-dot" style="background:${{COL_FB}}"></span>${{lB}} Feature</span>
     <span><span class="legend-dot" style="background:${{COL_TDB}}"></span>${{lB}} Tech Debt</span>`;
}}

// ─── Epic table ────────────────────────────────────────────────────────────
let tableRows = [];
function buildTable(dA, dB, lA, lB, qA, qB) {{
  tableRows = [
    ...dA.map(e => ({{...e, _q: 'A', _ql: lA, _qkey: qA}})),
    ...dB.map(e => ({{...e, _q: 'B', _ql: lB, _qkey: qB}}))
  ];
  renderTable();
}}

function renderTable() {{
  const sorted = [...tableRows].sort((a, b) => {{
    const av = a[sortKey] || '', bv = b[sortKey] || '';
    return av < bv ? -sortDir : av > bv ? sortDir : 0;
  }});
  document.getElementById('tableCount').textContent = `(${{sorted.length}} epics)`;
  document.getElementById('epicTbody').innerHTML = sorted.map(e => `
    <tr>
      <td><a href="${{JIRA_URL}}/browse/${{e.key}}" target="_blank" style="color:#2563eb;text-decoration:none;font-weight:600;">${{e.key}}</a></td>
      <td>${{e.project_name || ''}}</td>
      <td style="max-width:280px;">${{e.summary || ''}}</td>
      <td><span class="badge ${{e.type === 'Feature' ? 'badge-feat' : 'badge-td'}}">${{e.type || '?'}}</span></td>
      <td>${{e.assignee === 'Unassigned' ? '<span style="color:#94a3b8">—</span>' : (e.assignee || '')}}</td>
      <td>${{e.resdate || ''}}</td>
      <td><span class="badge ${{e._q === 'A' ? 'badge-a' : 'badge-b'}}">${{e._ql}}</span></td>
    </tr>`).join('');
  document.querySelectorAll('thead th').forEach(th => {{
    const fn = th.onclick ? th.onclick.toString() : '';
    th.classList.toggle('sorted', fn.includes(`'${{sortKey}}'`));
  }});
}}

function doSort(key) {{ if (sortKey === key) sortDir *= -1; else {{ sortKey = key; sortDir = 1; }} renderTable(); }}

// ─── Main refresh ──────────────────────────────────────────────────────────
function refresh() {{
  // Reset JQL registry so IDs don't accumulate across refreshes
  _jqlMap = {{}};
  _jqlCnt = 0;

  const qA = document.getElementById('selA').value;
  const qB = document.getElementById('selB').value;
  const dA = getData(qA), dB = getData(qB);
  const lA = QUARTER_LABELS[qA], lB = QUARTER_LABELS[qB];

  updateStats(dA, dB, lA, lB);
  buildPerTeamCharts(qA, qB, lA, lB);
  buildMonthChart(dA, dB, lA, lB);
  buildTypeChart(qA, qB, lA, lB);
  buildTable(dA, dB, lA, lB, qA, qB);
}}

refresh();
</script>
</body>
</html>"""

    return html


def main():
    parser = argparse.ArgumentParser(description='Generate Jira epic dashboard HTML')
    parser.add_argument('--output', required=True, help='Output HTML file path')
    parser.add_argument('--data-dir', default='/tmp', help='Directory with epics_clean_Q*.json files')
    parser.add_argument('--jira-url', default='https://pointdigitalfinance.atlassian.net',
                        help='Base Jira URL for issue links')
    args = parser.parse_args()

    print(f"Loading quarter data from {args.data_dir}...")
    quarters_order, quarters_data, quarters_label = load_quarters(args.data_dir)

    print(f"Found quarters: {', '.join(quarters_label[q] for q in quarters_order)}")
    for q in quarters_order:
        print(f"  {quarters_label[q]}: {len(quarters_data[q])} valid epics")

    print(f"\nGenerating HTML...")
    html = build_html(quarters_order, quarters_data, quarters_label, args.jira_url)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, 'w') as f:
        f.write(html)

    size = os.path.getsize(args.output)
    print(f"Written: {args.output} ({size:,} bytes)")


if __name__ == '__main__':
    main()
