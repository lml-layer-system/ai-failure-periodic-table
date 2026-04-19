"""Generate index.html — visual AI Failure Periodic Table. Run: python scripts/generate_visual.py"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).parent.parent
DATA = ROOT / "data" / "failures.json"
OUT  = ROOT / "index.html"

GROUP_COLORS = {
    "EPISTEMIC":    {"bg": "#1e3a5f", "accent": "#3B82F6", "light": "#93C5FD"},
    "AGENTIC":      {"bg": "#3d1f0a", "accent": "#F97316", "light": "#FED7AA"},
    "ADVERSARIAL":  {"bg": "#3d0a0a", "accent": "#EF4444", "light": "#FCA5A5"},
    "ALIGNMENT":    {"bg": "#2d1f4a", "accent": "#8B5CF6", "light": "#C4B5FD"},
    "ARCHITECTURAL":{"bg": "#0a2d1f", "accent": "#10B981", "light": "#6EE7B7"},
    "DOMAIN":       {"bg": "#3d2d00", "accent": "#F59E0B", "light": "#FDE68A"},
    "GOVERNANCE":   {"bg": "#1e2533", "accent": "#94A3B8", "light": "#CBD5E1"},
}

GROUP_ICONS = {
    "EPISTEMIC": "🧠", "AGENTIC": "🤖", "ADVERSARIAL": "⚔️",
    "ALIGNMENT": "🎯", "ARCHITECTURAL": "🏗️", "DOMAIN": "🔬", "GOVERNANCE": "⚖️",
}

def symbol(failure_id):
    """Extract short symbol from ID like EPIS-STRUCT-HALL-001 → STRUCT"""
    parts = failure_id.split("-")
    # Remove first (group prefix) and last (number) parts
    middle = parts[1:-1]
    if not middle:
        return parts[0][:6]
    s = middle[0][:6]
    if len(middle) > 1:
        s += "-" + middle[1][:4]
    return s

def short_name(name):
    """First 2 words, max 14 chars"""
    words = name.split()
    result = words[0] if words else name
    if len(words) > 1 and len(result) + len(words[1]) < 13:
        result += " " + words[1]
    return result[:14]

def load_data():
    with open(DATA) as f:
        d = json.load(f)
    groups = {g["code"]: g for g in d["groups"]}
    by_group = {g: [] for g in groups}
    for i, failure in enumerate(d["failures"]):
        failure["_sym"] = symbol(failure["id"])
        failure["_short"] = short_name(failure["name"])
        failure["_num"] = i + 1
        by_group[failure["group"]].append(failure)
    return groups, by_group, d["failures"]

def escape_js(s):
    return json.dumps(str(s) if s else "")

def build_html(groups, by_group, all_failures):
    # Build compact JS data payload (only what modal needs)
    js_data = {}
    for f in all_failures:
        refs = f.get("references") or []
        # Normalize case_studies: keep only dict entries, cap at 3
        raw_cs = f.get("case_studies") or []
        cs = [c for c in raw_cs if isinstance(c, dict)][:3]
        js_data[f["id"]] = {
            "name": f["name"],
            "group": f["group"],
            "mechanism": f.get("mechanism", ""),
            "forbidden": f.get("forbidden", ""),
            "severity": f["severity"],
            "examples": f.get("examples", ""),
            "mitigation": f.get("mitigation", ""),
            "case_studies": cs,
            "references": refs[:4],  # cap at 4
            "keywords": (f.get("keywords") or [])[:8],
            "mit_domain": f.get("mit_domain", ""),
            "ms_agentic_category": f.get("ms_agentic_category", ""),
        }

    cells_html = []
    for gcode, ginfo in groups.items():
        color = GROUP_COLORS[gcode]
        icon = GROUP_ICONS[gcode]
        failures = by_group[gcode]
        cells_html.append(f"""
  <section class="group-section" id="group-{gcode}" style="--accent:{color['accent']};--bg:{color['bg']};--light:{color['light']}">
    <div class="group-header">
      <span class="group-icon">{icon}</span>
      <div class="group-meta">
        <span class="group-name">{gcode}</span>
        <span class="group-subname">{ginfo['name'].split('(')[0].strip()}</span>
        <span class="group-count">{len(failures)} classes</span>
      </div>
      <div class="group-invariant">{ginfo['invariant']}</div>
    </div>
    <div class="cells-grid">""")
        for f in failures:
            crit = "critical" if f["severity"] == "CRITICAL" else ""
            sym = f["_sym"]
            short = f["_short"]
            num = f["_num"]
            fid = f["id"]
            cells_html.append(f"""      <div class="cell {crit}" data-id="{fid}" data-group="{gcode}" title="{f['name']}" onclick="showModal('{fid}')">
        <span class="cell-num">{num}</span>
        {('<span class="crit-badge">!</span>' if crit else '')}
        <span class="cell-sym">{sym}</span>
        <span class="cell-name">{short}</span>
      </div>""")
        cells_html.append("    </div>\n  </section>")

    cells_str = "\n".join(cells_html)
    js_data_str = json.dumps(js_data, ensure_ascii=False)
    total = len(all_failures)
    critical = sum(1 for f in all_failures if f["severity"] == "CRITICAL")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Failure Periodic Table — {total} Classes</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0d1117;color:#e6edf3;font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh}}
a{{color:#58a6ff}}

/* Header */
.header{{background:linear-gradient(135deg,#161b22 0%,#0d1117 100%);border-bottom:1px solid #30363d;padding:24px 32px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}}
.header-left h1{{font-size:1.6rem;font-weight:700;color:#f0f6fc;letter-spacing:-0.5px}}
.header-left p{{color:#8b949e;font-size:.85rem;margin-top:4px}}
.stats{{display:flex;gap:24px}}
.stat{{text-align:center}}
.stat-num{{font-size:1.5rem;font-weight:700;color:#58a6ff}}
.stat-label{{font-size:.7rem;color:#8b949e;text-transform:uppercase;letter-spacing:.5px}}

/* Search */
.search-bar{{padding:16px 32px;background:#161b22;border-bottom:1px solid #30363d;display:flex;align-items:center;gap:12px}}
.search-bar input{{flex:1;background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:10px 16px;color:#e6edf3;font-size:.9rem;outline:none;transition:.2s}}
.search-bar input:focus{{border-color:#58a6ff;box-shadow:0 0 0 3px rgba(88,166,255,.1)}}
.search-bar input::placeholder{{color:#484f58}}
#search-count{{color:#8b949e;font-size:.8rem;white-space:nowrap}}

/* Legend */
.legend{{padding:8px 32px;background:#161b22;border-bottom:1px solid #30363d;display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.legend-item{{display:flex;align-items:center;gap:6px;font-size:.75rem;color:#8b949e}}
.legend-dot{{width:10px;height:10px;border-radius:2px}}
.legend-crit{{width:10px;height:10px;border-radius:2px;background:#EF4444;border:1px solid #ff6b6b}}

/* Main */
.main{{padding:24px 32px;display:flex;flex-direction:column;gap:20px}}

/* Group section */
.group-section{{border-radius:12px;border:1px solid color-mix(in srgb,var(--accent) 25%,transparent);background:color-mix(in srgb,var(--bg) 60%,#0d1117);overflow:hidden}}
.group-header{{display:flex;align-items:flex-start;gap:16px;padding:16px 20px;background:color-mix(in srgb,var(--accent) 12%,transparent);border-bottom:1px solid color-mix(in srgb,var(--accent) 20%,transparent)}}
.group-icon{{font-size:1.8rem;line-height:1}}
.group-meta{{flex:0 0 auto}}
.group-name{{display:block;font-size:1rem;font-weight:700;color:var(--light)}}
.group-subname{{display:block;font-size:.75rem;color:#8b949e;margin-top:2px}}
.group-count{{display:inline-block;margin-top:4px;font-size:.7rem;padding:2px 8px;border-radius:999px;background:color-mix(in srgb,var(--accent) 20%,transparent);color:var(--light)}}
.group-invariant{{margin-left:auto;font-size:.75rem;color:#8b949e;font-style:italic;max-width:300px;text-align:right}}

/* Cells grid */
.cells-grid{{display:flex;flex-wrap:wrap;gap:6px;padding:16px 20px}}

/* Cell */
.cell{{
  width:80px;height:88px;border-radius:8px;
  border:1px solid color-mix(in srgb,var(--accent) 30%,transparent);
  background:color-mix(in srgb,var(--accent) 8%,#0d1117);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  cursor:pointer;position:relative;padding:4px;
  transition:all .15s ease;text-align:center;
}}
.cell:hover{{
  border-color:var(--accent);
  background:color-mix(in srgb,var(--accent) 20%,#0d1117);
  transform:translateY(-2px);
  box-shadow:0 4px 12px color-mix(in srgb,var(--accent) 30%,transparent);
  z-index:1;
}}
.cell.critical{{
  border-color:#EF4444;
  background:color-mix(in srgb,#EF4444 12%,#0d1117);
  box-shadow:0 0 8px rgba(239,68,68,.2);
}}
.cell.critical:hover{{
  background:color-mix(in srgb,#EF4444 25%,#0d1117);
  box-shadow:0 4px 16px rgba(239,68,68,.4);
}}
.cell.hidden{{opacity:.15;pointer-events:none}}
.cell.highlighted{{
  border-color:var(--accent) !important;
  background:color-mix(in srgb,var(--accent) 25%,#0d1117) !important;
  box-shadow:0 0 12px color-mix(in srgb,var(--accent) 50%,transparent) !important;
}}
.cell-num{{font-size:.55rem;color:#484f58;position:absolute;top:5px;left:6px}}
.crit-badge{{position:absolute;top:4px;right:5px;font-size:.55rem;color:#EF4444;font-weight:700}}
.cell-sym{{font-size:.75rem;font-weight:700;color:var(--light);line-height:1.2;word-break:break-all;max-width:70px}}
.cell.critical .cell-sym{{color:#FCA5A5}}
.cell-name{{font-size:.55rem;color:#8b949e;margin-top:3px;line-height:1.2;max-width:72px}}

/* Modal */
.modal-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.75);z-index:100;display:none;align-items:center;justify-content:center;padding:20px}}
.modal-overlay.open{{display:flex}}
.modal{{background:#161b22;border:1px solid #30363d;border-radius:16px;max-width:680px;width:100%;max-height:85vh;overflow-y:auto;position:relative}}
.modal-header{{padding:24px 28px 16px;border-bottom:1px solid #30363d;position:sticky;top:0;background:#161b22;z-index:1}}
.modal-header h2{{font-size:1.1rem;color:#f0f6fc;font-weight:700}}
.modal-id{{font-size:.75rem;color:#8b949e;font-family:monospace;margin-top:2px}}
.modal-badges{{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}}
.badge{{font-size:.7rem;padding:3px 10px;border-radius:999px;font-weight:600}}
.badge-group{{background:color-mix(in srgb,var(--accent) 20%,transparent);color:var(--light)}}
.badge-crit{{background:rgba(239,68,68,.2);color:#FCA5A5;border:1px solid rgba(239,68,68,.4)}}
.badge-std{{background:rgba(148,163,184,.1);color:#94A3B8}}
.modal-close{{position:absolute;top:20px;right:20px;background:none;border:1px solid #30363d;color:#8b949e;width:28px;height:28px;border-radius:6px;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center}}
.modal-close:hover{{background:#30363d;color:#e6edf3}}
.modal-body{{padding:20px 28px 28px}}
.field{{margin-bottom:16px}}
.field-label{{font-size:.7rem;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.8px;margin-bottom:6px}}
.field-value{{font-size:.875rem;color:#e6edf3;line-height:1.6}}
.field-value.mono{{font-family:monospace;font-size:.8rem;color:#79c0ff}}
.refs-list{{display:flex;flex-direction:column;gap:4px}}
.ref-item{{font-size:.78rem;color:#8b949e;padding:6px 10px;background:#0d1117;border-radius:6px;border-left:3px solid #30363d;line-height:1.4}}
.keywords-list{{display:flex;flex-wrap:wrap;gap:6px}}
.kw-badge{{font-size:.7rem;padding:2px 8px;border-radius:4px;background:#21262d;color:#8b949e;font-family:monospace}}
.mitigation-box{{background:color-mix(in srgb,var(--accent) 10%,#0d1117);border:1px solid color-mix(in srgb,var(--accent) 30%,transparent);border-radius:8px;padding:10px 14px;font-size:.875rem;color:var(--light);line-height:1.5}}
.cs-list{{display:flex;flex-direction:column;gap:8px}}
.cs-card{{background:#0d1117;border-radius:8px;padding:10px 14px;border-left:3px solid color-mix(in srgb,var(--accent) 50%,transparent)}}
.cs-title{{font-size:.82rem;font-weight:600;color:#e6edf3;margin-bottom:4px}}
.cs-meta{{font-size:.73rem;color:#8b949e;display:flex;gap:10px;flex-wrap:wrap;margin-bottom:4px}}
.cs-outcome{{font-size:.78rem;color:#8b949e;line-height:1.4}}

/* Footer */
.footer{{text-align:center;padding:24px;color:#484f58;font-size:.78rem;border-top:1px solid #21262d}}
.footer a{{color:#58a6ff;text-decoration:none}}

@media(max-width:700px){{
  .main{{padding:12px 12px}}
  .cells-grid{{gap:4px;padding:10px 12px}}
  .cell{{width:68px;height:76px}}
  .group-invariant{{display:none}}
  .header{{padding:16px}}
}}
</style>
</head>
<body>

<header class="header">
  <div class="header-left">
    <h1>⚛ AI Failure Periodic Table</h1>
    <p>A shared vocabulary for AI safety — every known failure mode, classified.</p>
  </div>
  <div class="stats">
    <div class="stat"><div class="stat-num">{total}</div><div class="stat-label">Classes</div></div>
    <div class="stat"><div class="stat-num">7</div><div class="stat-label">Dimensions</div></div>
    <div class="stat"><div class="stat-num">{critical}</div><div class="stat-label">Critical</div></div>
  </div>
</header>

<div class="search-bar">
  <input type="text" id="search" placeholder="Search failure classes, mechanisms, keywords…" oninput="doSearch(this.value)" autocomplete="off">
  <span id="search-count">{total} classes</span>
</div>

<div class="legend">
  <span style="color:#8b949e;font-size:.75rem;font-weight:600">LEGEND:</span>
  {"".join(f'<span class="legend-item"><span class="legend-dot" style="background:{GROUP_COLORS[g]["accent"]}"></span>{g}</span>' for g in GROUP_COLORS)}
  <span class="legend-item"><span class="legend-crit"></span>CRITICAL severity</span>
  <span style="margin-left:auto;font-size:.72rem;color:#484f58">Click any element to inspect</span>
</div>

<main class="main">
{cells_str}
</main>

<footer class="footer">
  <a href="https://github.com/lml-layer-system/ai-failure-periodic-table" target="_blank">github.com/lml-layer-system/ai-failure-periodic-table</a>
  &nbsp;·&nbsp; v1.4.21 &nbsp;·&nbsp; Sources: 2026 frontier system cards, peer-reviewed safety literature
</footer>

<div class="modal-overlay" id="modal" onclick="closeModalOutside(event)">
  <div class="modal" id="modal-inner">
    <div class="modal-header">
      <button class="modal-close" onclick="closeModal()">✕</button>
      <h2 id="m-name"></h2>
      <div class="modal-id" id="m-id"></div>
      <div class="modal-badges" id="m-badges"></div>
    </div>
    <div class="modal-body">
      <div class="field"><div class="field-label">Mechanism</div><div class="field-value" id="m-mechanism"></div></div>
      <div class="field" id="m-forbidden-wrap"><div class="field-label">Forbidden Invariant</div><div class="field-value mono" id="m-forbidden"></div></div>
      <div class="field" id="m-examples-wrap"><div class="field-label">Example</div><div class="field-value" id="m-examples"></div></div>
      <div class="field" id="m-mitigation-wrap"><div class="field-label">Structural Mitigation</div><div class="mitigation-box" id="m-mitigation"></div></div>
      <div class="field" id="m-cs-wrap"><div class="field-label">Case Studies</div><div class="cs-list" id="m-cs"></div></div>
      <div class="field" id="m-refs-wrap"><div class="field-label">References</div><div class="refs-list" id="m-refs"></div></div>
      <div class="field" id="m-kw-wrap"><div class="field-label">Keywords</div><div class="keywords-list" id="m-kw"></div></div>
      <div class="field" id="m-mit-wrap"><div class="field-label">MIT Domain</div><div class="field-value" id="m-mit"></div></div>
      <div class="field" id="m-msag-wrap"><div class="field-label">MS Agentic Category</div><div class="field-value" id="m-msag"></div></div>
    </div>
  </div>
</div>

<script>
const DATA = {js_data_str};
const ACCENTS = {json.dumps({g: GROUP_COLORS[g]['accent'] for g in GROUP_COLORS})};

function showModal(id) {{
  const d = DATA[id];
  if (!d) return;
  const m = document.getElementById('modal');
  const accent = ACCENTS[d.group] || '#58a6ff';
  document.getElementById('modal-inner').style.setProperty('--accent', accent);
  document.getElementById('modal-inner').style.setProperty('--light', accent);
  document.getElementById('m-name').textContent = d.name;
  document.getElementById('m-id').textContent = id;
  const badges = document.getElementById('m-badges');
  badges.innerHTML = `<span class="badge badge-group" style="--accent:${{accent}};--light:${{accent}}">${{d.group}}</span>` +
    (d.severity === 'CRITICAL' ? '<span class="badge badge-crit">⚠ CRITICAL</span>' : '<span class="badge badge-std">STANDARD</span>');
  document.getElementById('m-mechanism').textContent = d.mechanism || '—';
  const fw = document.getElementById('m-forbidden-wrap');
  if (d.forbidden) {{ fw.style.display=''; document.getElementById('m-forbidden').textContent = d.forbidden; }}
  else fw.style.display = 'none';
  const ew = document.getElementById('m-examples-wrap');
  if (d.examples) {{ ew.style.display=''; document.getElementById('m-examples').textContent = d.examples; }}
  else ew.style.display = 'none';
  const mw = document.getElementById('m-mitigation-wrap');
  if (d.mitigation) {{ mw.style.display=''; document.getElementById('m-mitigation').textContent = d.mitigation; }}
  else mw.style.display = 'none';
  const csw = document.getElementById('m-cs-wrap');
  const csEl = document.getElementById('m-cs');
  if (d.case_studies && d.case_studies.length) {{
    csw.style.display='';
    csEl.innerHTML = d.case_studies.map(c => {{
      const sys = c.system ? `<span>${{c.system}}</span>` : '';
      const dt = c.date ? `<span>${{c.date}}</span>` : '';
      const src = c.source ? `<span><a href="${{c.source}}" target="_blank" rel="noopener">source</a></span>` : '';
      return `<div class="cs-card">
        <div class="cs-title">${{c.title||''}}</div>
        <div class="cs-meta">${{sys}}${{dt}}${{src}}</div>
        <div class="cs-outcome">${{c.outcome||''}}</div>
      </div>`;
    }}).join('');
  }} else csw.style.display = 'none';
  const rw = document.getElementById('m-refs-wrap');
  const refsEl = document.getElementById('m-refs');
  if (d.references && d.references.length) {{
    rw.style.display='';
    refsEl.innerHTML = d.references.map(r => `<div class="ref-item">${{r}}</div>`).join('');
  }} else rw.style.display = 'none';
  const kw = document.getElementById('m-kw-wrap');
  const kwEl = document.getElementById('m-kw');
  if (d.keywords && d.keywords.length) {{
    kw.style.display='';
    kwEl.innerHTML = d.keywords.map(k => `<span class="kw-badge">${{k}}</span>`).join('');
  }} else kw.style.display = 'none';
  const mitw = document.getElementById('m-mit-wrap');
  if (d.mit_domain) {{ mitw.style.display=''; document.getElementById('m-mit').textContent = d.mit_domain; }}
  else mitw.style.display = 'none';
  const msagw = document.getElementById('m-msag-wrap');
  if (d.ms_agentic_category) {{ msagw.style.display=''; document.getElementById('m-msag').textContent = d.ms_agentic_category; }}
  else msagw.style.display = 'none';
  m.classList.add('open');
  document.body.style.overflow = 'hidden';
}}

function closeModal() {{
  document.getElementById('modal').classList.remove('open');
  document.body.style.overflow = '';
}}

function closeModalOutside(e) {{
  if (e.target === document.getElementById('modal')) closeModal();
}}

document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeModal(); }});

function doSearch(q) {{
  q = q.toLowerCase().trim();
  const cells = document.querySelectorAll('.cell');
  let visible = 0;
  cells.forEach(cell => {{
    const id = cell.dataset.id;
    const d = DATA[id];
    if (!q) {{
      cell.classList.remove('hidden','highlighted');
      visible++;
      return;
    }}
    const haystack = [id, d.name, d.mechanism, d.examples, d.mitigation||'', ...(d.keywords||[])].join(' ').toLowerCase();
    if (haystack.includes(q)) {{
      cell.classList.remove('hidden');
      cell.classList.add('highlighted');
      visible++;
    }} else {{
      cell.classList.add('hidden');
      cell.classList.remove('highlighted');
    }}
  }});
  document.getElementById('search-count').textContent = q ? `${{visible}} match${{visible===1?'':'es'}}` : `{total} classes`;
}}
</script>
</body>
</html>"""

if __name__ == "__main__":
    groups, by_group, all_failures = load_data()
    html = build_html(groups, by_group, all_failures)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written: {OUT}")
    print(f"  {len(all_failures)} classes | {len(html):,} bytes")
