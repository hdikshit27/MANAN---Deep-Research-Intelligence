import streamlit as st
import time
import sys
import os

# ── Page config — must be first Streamlit call ─────────────────────────────────
st.set_page_config(
    page_title="MANAN — Deep Research AI",
    page_icon="🔵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL CSS  —  cross-browser safe, no backdrop-filter, no -webkit-only props
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Source+Code+Pro:wght@400;500;600&display=swap');

:root {
    --blue-core:   #0044cc;
    --blue-bright: #2266ff;
    --blue-mid:    #0055ee;
    --blue-dim:    #003399;
    --blue-glow:   rgba(0,80,220,0.18);
    --blue-faint:  rgba(0,80,220,0.07);
    --s0: #0a0a0a;
    --s1: #111111;
    --s2: #181818;
    --s3: #202020;
    --border:     rgba(255,255,255,0.08);
    --border-blue: rgba(0,80,220,0.35);
    --tp: #eef1ff;
    --ts: #8898b8;
    --tm: #3a4260;
    --fd: 'Orbitron','Courier New',monospace;
    --fb: 'Rajdhani','Trebuchet MS',sans-serif;
    --fm: 'Source Code Pro','Courier New',monospace;
    --r-sm: 8px; --r-md: 12px; --r-lg: 18px;
    --tr: all 0.25s ease;
}

*, *::before, *::after { -webkit-box-sizing: border-box; box-sizing: border-box; }

#MainMenu, header, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stHeader"] { display:none !important; visibility:hidden !important; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > section,
[data-testid="stMain"] {
    background-color: var(--s0) !important;
    color: var(--tp) !important;
    font-family: var(--fb) !important;
}

[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 75% 55% at 50% -5%,  rgba(0,60,200,0.24) 0%, transparent 65%),
        radial-gradient(ellipse 55% 40% at 50% 48%,  rgba(0,50,180,0.10) 0%, transparent 70%),
        radial-gradient(ellipse 80% 30% at 50% 105%, rgba(0,40,160,0.09) 0%, transparent 60%) !important;
}

.block-container {
    max-width: 780px !important;
    padding-top: 0 !important;
    padding-bottom: 3rem !important;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
    margin: 0 auto !important;
}

::-webkit-scrollbar            { width:5px; height:5px; }
::-webkit-scrollbar-track      { background:var(--s1); }
::-webkit-scrollbar-thumb      { background:var(--blue-dim); border-radius:3px; }
::-webkit-scrollbar-thumb:hover{ background:var(--blue-mid); }

/* ── Hero ───────────────────────────────────────── */
.mn-hero {
    text-align:center;
    padding:4.5rem 1rem 2.5rem;
    -webkit-animation: fadeUp .55s ease both;
    animation:         fadeUp .55s ease both;
}

.mn-eyebrow {
    display:inline-block;
    font-family:var(--fm); font-size:.68rem;
    letter-spacing:.22em; text-transform:uppercase;
    color:var(--blue-bright);
    border:1px solid var(--border-blue);
    padding:.3rem .9rem; border-radius:4px;
    margin-bottom:1.8rem;
    background:var(--blue-faint);
}

.mn-title {
    font-family:var(--fd); font-weight:900;
    font-size:clamp(3.8rem,14vw,7.5rem);
    line-height:1; letter-spacing:.12em;
    color:var(--blue-bright);
    text-shadow:
        0 0 20px rgba(40,120,255,.7),
        0 0 60px rgba(0,80,220,.45),
        0 0 120px rgba(0,60,200,.25);
    margin-bottom:1.1rem;
}

.mn-tagline {
    font-family:var(--fd); font-weight:400;
    font-size:clamp(.8rem,2.5vw,1.05rem);
    letter-spacing:.18em; text-transform:uppercase;
    color:var(--ts); margin-bottom:.9rem;
}

.mn-desc {
    font-family:var(--fb); font-weight:300;
    font-size:1.05rem; color:var(--tm);
    max-width:500px; margin:0 auto;
    line-height:1.75; letter-spacing:.02em;
}

/* ── Divider ────────────────────────────────────── */
.mn-divider {
    height:1px; border:none;
    background: -webkit-linear-gradient(left,transparent,var(--border-blue),transparent);
    background:    linear-gradient(to right,transparent,var(--border-blue),transparent);
    margin:2rem 0;
}

/* ── Input card ─────────────────────────────────── */
.mn-input-wrap {
    background:var(--s1);
    border:1px solid var(--border);
    border-radius:var(--r-lg);
    padding:2rem 2rem 1.5rem;
    margin-bottom:2rem; position:relative;
    -webkit-animation: fadeUp .55s .12s ease both;
    animation:         fadeUp .55s .12s ease both;
}

.mn-input-wrap::before {
    content:''; position:absolute;
    top:0;left:0;right:0;height:2px;
    border-radius:var(--r-lg) var(--r-lg) 0 0;
    background:-webkit-linear-gradient(left,transparent,var(--blue-mid),transparent);
    background:   linear-gradient(to right,transparent,var(--blue-mid),transparent);
}

.mn-label {
    font-family:var(--fm); font-size:.68rem;
    letter-spacing:.2em; text-transform:uppercase;
    color:var(--blue-bright); margin-bottom:.7rem;
}

/* text input */
[data-testid="stTextInput"] label { display:none !important; }
[data-testid="stTextInput"] > div > div { border:none !important; padding:0 !important; }

[data-testid="stTextInput"] input {
    background:var(--s2) !important;
    border:1px solid rgba(255,255,255,.1) !important;
    border-radius:var(--r-md) !important;
    color:var(--tp) !important;
    font-family:var(--fb) !important;
    font-size:1.1rem !important; font-weight:500 !important;
    letter-spacing:.03em !important;
    padding:.85rem 1.1rem !important;
    width:100% !important; outline:none !important;
    -webkit-transition:var(--tr) !important;
    transition:var(--tr) !important;
    caret-color:var(--blue-bright) !important;
    -webkit-appearance:none; appearance:none;
}

[data-testid="stTextInput"] input:focus {
    border-color:var(--border-blue) !important;
    box-shadow:0 0 0 3px rgba(0,80,220,.12),0 0 20px rgba(0,80,220,.08) !important;
}

[data-testid="stTextInput"] input::-webkit-input-placeholder { color:var(--tm) !important; }
[data-testid="stTextInput"] input::-moz-placeholder           { color:var(--tm) !important; }
[data-testid="stTextInput"] input:-ms-input-placeholder       { color:var(--tm) !important; }
[data-testid="stTextInput"] input::placeholder                { color:var(--tm) !important; }

/* run button */
[data-testid="stButton"] > button {
    width:100% !important;
    background:var(--blue-core) !important;
    background-image:-webkit-linear-gradient(top,#1166ee,#003399) !important;
    background-image:   linear-gradient(to bottom,#1166ee,#003399) !important;
    color:#fff !important;
    border:1px solid rgba(60,130,255,.3) !important;
    border-radius:var(--r-md) !important;
    padding:.8rem 2rem !important;
    font-family:var(--fd) !important; font-weight:600 !important;
    font-size:.82rem !important; letter-spacing:.14em !important;
    text-transform:uppercase !important; cursor:pointer !important;
    -webkit-transition:var(--tr) !important; transition:var(--tr) !important;
    box-shadow:0 4px 20px rgba(0,80,220,.4),0 1px 3px rgba(0,0,0,.5) !important;
    margin-top:.85rem !important;
    -webkit-appearance:none; appearance:none;
}

[data-testid="stButton"] > button:hover {
    background-image:-webkit-linear-gradient(top,#2277ff,#0044cc) !important;
    background-image:   linear-gradient(to bottom,#2277ff,#0044cc) !important;
    box-shadow:0 6px 28px rgba(0,80,220,.55),0 1px 3px rgba(0,0,0,.5) !important;
    -webkit-transform:translateY(-1px) !important; transform:translateY(-1px) !important;
}

[data-testid="stButton"] > button:active {
    -webkit-transform:translateY(0) !important; transform:translateY(0) !important;
    box-shadow:0 2px 10px rgba(0,80,220,.35) !important;
}

/* ── Pipeline grid ──────────────────────────────── */
.mn-pipeline-label {
    font-family:var(--fm); font-size:.65rem;
    letter-spacing:.22em; text-transform:uppercase;
    color:var(--tm); margin-bottom:1rem;
}

.mn-grid {
    display:-ms-grid; display:grid;
    -ms-grid-columns:1fr 0.85rem 1fr;
    grid-template-columns:1fr 1fr;
    grid-gap:.85rem; gap:.85rem;
    margin-bottom:2rem;
    -webkit-animation: fadeUp .55s .22s ease both;
    animation:         fadeUp .55s .22s ease both;
}

@media (max-width:560px) {
    .mn-grid { -ms-grid-columns:1fr; grid-template-columns:1fr; }
}

.mn-card {
    background:var(--s1);
    border:1px solid var(--border);
    border-radius:var(--r-md);
    padding:1.25rem 1.3rem;
    position:relative; overflow:hidden;
    -webkit-transition:border-color .3s ease,background .3s ease;
    transition:border-color .3s ease,background .3s ease;
}

.mn-card:hover { border-color:rgba(0,80,220,.2); }

.mn-card.is-running {
    border-color:var(--border-blue) !important;
    background:rgba(0,60,200,.06) !important;
    box-shadow:0 0 24px rgba(0,60,200,.14) !important;
}

.mn-card.is-done {
    border-color:rgba(60,180,60,.3) !important;
    background:rgba(60,180,60,.04) !important;
}

.mn-card::after {
    content:''; position:absolute;
    top:0;left:0;right:0;height:2px;
    background:-webkit-linear-gradient(left,transparent,rgba(0,80,220,.5),transparent);
    background:   linear-gradient(to right,transparent,rgba(0,80,220,.5),transparent);
    opacity:0;
    -webkit-transition:opacity .3s; transition:opacity .3s;
}

.mn-card.is-running::after,.mn-card:hover::after { opacity:1; }

.mn-card.is-done::after {
    background:-webkit-linear-gradient(left,transparent,rgba(60,180,60,.5),transparent);
    background:   linear-gradient(to right,transparent,rgba(60,180,60,.5),transparent);
    opacity:1;
}

.mn-card-step {
    font-family:var(--fm); font-size:.6rem;
    letter-spacing:.15em; color:var(--tm);
    margin-bottom:.55rem; text-transform:uppercase;
}

.mn-card-row {
    display:-webkit-box; display:-ms-flexbox; display:flex;
    -webkit-box-align:center; -ms-flex-align:center; align-items:center;
    gap:.6rem; margin-bottom:.45rem;
}

.mn-card-icon { font-size:1.2rem; line-height:1; }

.mn-card-title {
    font-family:var(--fd); font-weight:600;
    font-size:.75rem; letter-spacing:.08em;
    color:var(--tp); text-transform:uppercase;
}

.mn-card-desc {
    font-size:.82rem; font-weight:300;
    color:var(--tm); line-height:1.55; letter-spacing:.01em;
}

.mn-pill {
    display:-webkit-inline-box; display:-ms-inline-flexbox; display:inline-flex;
    -webkit-box-align:center; -ms-flex-align:center; align-items:center;
    gap:.35rem; margin-top:.85rem;
    font-family:var(--fm); font-size:.58rem;
    letter-spacing:.12em; text-transform:uppercase;
    padding:.22rem .65rem; border-radius:3px;
}

.mn-pill.idle    { background:rgba(255,255,255,.03); color:var(--tm); border:1px solid rgba(255,255,255,.06); }
.mn-pill.running { background:rgba(0,80,220,.12); color:var(--blue-bright); border:1px solid var(--border-blue); }
.mn-pill.done    { background:rgba(60,180,60,.10); color:#4dc44d; border:1px solid rgba(60,180,60,.28); }

@-webkit-keyframes pill-pulse { 0%,100%{opacity:1} 50%{opacity:.3} }
@keyframes         pill-pulse { 0%,100%{opacity:1} 50%{opacity:.3} }

.mn-dot {
    width:5px; height:5px; border-radius:50%;
    background:currentColor; display:inline-block;
    -webkit-animation:pill-pulse 1.2s ease-in-out infinite;
    animation:        pill-pulse 1.2s ease-in-out infinite;
}

/* ── Results ────────────────────────────────────── */
.mn-results-head {
    display:-webkit-box; display:-ms-flexbox; display:flex;
    -webkit-box-align:center; -ms-flex-align:center; align-items:center;
    gap:.75rem; margin-bottom:1.25rem;
}

.mn-results-title {
    font-family:var(--fd); font-weight:700;
    font-size:.95rem; letter-spacing:.1em;
    text-transform:uppercase; color:var(--tp);
}

.mn-ok-badge {
    font-family:var(--fm); font-size:.6rem; letter-spacing:.12em;
    background:rgba(60,180,60,.1); color:#4dc44d;
    border:1px solid rgba(60,180,60,.28);
    padding:.18rem .55rem; border-radius:3px; text-transform:uppercase;
}

.mn-report-card {
    background:var(--s1); border:1px solid var(--border);
    border-radius:var(--r-lg); padding:1.75rem;
    margin-bottom:1rem; position:relative; overflow:hidden;
}

.mn-report-card::before {
    content:''; position:absolute; top:0;left:0;right:0; height:2px;
    background:-webkit-linear-gradient(left,transparent,var(--blue-mid),var(--blue-bright),var(--blue-mid),transparent);
    background:   linear-gradient(to right,transparent,var(--blue-mid),var(--blue-bright),var(--blue-mid),transparent);
}

.mn-report-card.feedback::before {
    background:-webkit-linear-gradient(left,transparent,#3cb33c,#5de05d,#3cb33c,transparent);
    background:   linear-gradient(to right,transparent,#3cb33c,#5de05d,#3cb33c,transparent);
}

.mn-section-label {
    font-family:var(--fm); font-size:.65rem;
    letter-spacing:.2em; text-transform:uppercase;
    color:var(--blue-bright); margin-bottom:1.1rem; display:block;
}

.mn-section-label.feedback { color:#4dc44d; }

/* markdown body inside cards */
[data-testid="stMarkdownContainer"] p {
    font-family:var(--fb) !important; font-size:.97rem !important;
    font-weight:400 !important; color:var(--ts) !important;
    line-height:1.85 !important; letter-spacing:.01em !important;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    font-family:var(--fd) !important; font-weight:700 !important;
    letter-spacing:.06em !important; color:var(--tp) !important;
    margin-top:1.4rem !important; margin-bottom:.5rem !important;
    text-transform:uppercase !important;
}

[data-testid="stMarkdownContainer"] h1 { font-size:1.2rem !important; }
[data-testid="stMarkdownContainer"] h2 { font-size:1.0rem !important; }
[data-testid="stMarkdownContainer"] h3 { font-size:.88rem !important; }
[data-testid="stMarkdownContainer"] strong { color:var(--tp) !important; }

[data-testid="stMarkdownContainer"] code {
    font-family:var(--fm) !important; font-size:.84em !important;
    background:rgba(0,80,220,.1) !important;
    border:1px solid rgba(0,80,220,.2) !important;
    border-radius:3px !important; padding:.12em .4em !important;
    color:#6090ff !important;
}

[data-testid="stMarkdownContainer"] ul,
[data-testid="stMarkdownContainer"] ol {
    padding-left:1.3rem !important; margin-bottom:.8rem !important;
}

[data-testid="stMarkdownContainer"] li {
    color:var(--ts) !important; font-family:var(--fb) !important;
    font-size:.97rem !important; margin-bottom:.3rem !important;
}

/* expander */
[data-testid="stExpander"] {
    background:var(--s1) !important; border:1px solid var(--border) !important;
    border-radius:var(--r-md) !important; margin-bottom:.65rem !important; overflow:hidden !important;
}

[data-testid="stExpander"] summary {
    font-family:var(--fm) !important; font-size:.72rem !important;
    letter-spacing:.12em !important; text-transform:uppercase !important;
    color:var(--tm) !important; padding:.85rem 1.1rem !important;
    -webkit-transition:color .2s !important; transition:color .2s !important;
}

[data-testid="stExpander"] summary:hover { color:var(--blue-bright) !important; }

/* download button */
[data-testid="stDownloadButton"] > button {
    background:transparent !important;
    border:1px solid var(--border-blue) !important;
    border-radius:var(--r-sm) !important; color:var(--blue-bright) !important;
    font-family:var(--fd) !important; font-weight:600 !important;
    font-size:.72rem !important; letter-spacing:.14em !important;
    text-transform:uppercase !important; padding:.6rem 1.4rem !important;
    cursor:pointer !important;
    -webkit-transition:var(--tr) !important; transition:var(--tr) !important;
}

[data-testid="stDownloadButton"] > button:hover {
    background:rgba(0,80,220,.08) !important;
    box-shadow:0 0 16px rgba(0,80,220,.25) !important;
    -webkit-transform:translateY(-1px) !important; transform:translateY(-1px) !important;
}

/* spinner & alert */
[data-testid="stSpinner"] > div {
    color:var(--blue-bright) !important;
    font-family:var(--fm) !important; font-size:.8rem !important;
    letter-spacing:.08em !important;
}

[data-testid="stAlert"] {
    border-radius:var(--r-md) !important;
    font-family:var(--fb) !important; font-size:.9rem !important;
}

/* code blocks */
[data-testid="stCode"] {
    background:var(--s2) !important; border:1px solid var(--border) !important;
    border-radius:var(--r-sm) !important;
    font-family:var(--fm) !important; font-size:.78rem !important;
    color:var(--tm) !important;
}

/* footer */
.mn-footer { text-align:center; padding:2.5rem 1rem 1.5rem; margin-top:1rem; }

.mn-footer-line {
    height:1px; border:none;
    background:-webkit-linear-gradient(left,transparent,var(--border),transparent);
    background:   linear-gradient(to right,transparent,var(--border),transparent);
    margin-bottom:2rem;
}

.mn-footer-logo {
    font-family:var(--fd); font-weight:900;
    font-size:1.6rem; letter-spacing:.2em;
    color:var(--blue-core);
    text-shadow:0 0 20px rgba(0,80,220,.4);
    margin-bottom:.45rem;
}

.mn-footer-sub {
    font-family:var(--fm); font-size:.62rem;
    letter-spacing:.2em; color:var(--tm); text-transform:uppercase;
}

/* fade-up entry */
@-webkit-keyframes fadeUp {
    from { opacity:0; -webkit-transform:translateY(14px); transform:translateY(14px); }
    to   { opacity:1; -webkit-transform:translateY(0);    transform:translateY(0);    }
}
@keyframes fadeUp {
    from { opacity:0; transform:translateY(14px); }
    to   { opacity:1; transform:translateY(0);    }
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
for k, v in {
    "results":  None,
    "running":  False,
    "error":    None,
    "stages":   {"search":"idle","reader":"idle","writer":"idle","critic":"idle"},
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════════════════
AGENTS = [
    ("01","🔍","Search Agent",
     "Scans the web for current, reliable information on your topic."),
    ("02","📄","Reader Agent",
     "Visits the top URL and extracts full structured content."),
    ("03","✍", "Writer Chain",
     "Synthesises all data into a coherent research report."),
    ("04","⚖", "Critic Chain",
     "Reviews the report for accuracy, depth, and clarity."),
]
KEYS = ["search","reader","writer","critic"]


def _card(step, icon, title, desc, status):
    cls   = {"idle":"mn-card","running":"mn-card is-running","done":"mn-card is-done"}[status]
    pcls  = {"idle":"mn-pill idle","running":"mn-pill running","done":"mn-pill done"}[status]
    pbody = {"idle":"Idle",
             "running":'<span class="mn-dot"></span> Running',
             "done":"✓ Complete"}[status]
    return f"""<div class="{cls}">
  <div class="mn-card-step">Step {step}</div>
  <div class="mn-card-row">
    <span class="mn-card-icon">{icon}</span>
    <span class="mn-card-title">{title}</span>
  </div>
  <div class="mn-card-desc">{desc}</div>
  <span class="{pcls}">{pbody}</span>
</div>"""


def _grid():
    html = '<div class="mn-grid">'
    for i,(step,icon,title,desc) in enumerate(AGENTS):
        html += _card(step,icon,title,desc,st.session_state.stages[KEYS[i]])
    return html+"</div>"


@st.cache_resource(show_spinner=False)
def _load_agents():
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from agents import (build_search_agent, build_reader_agent,
                            writer_chain, critic_chain)
        return build_search_agent, build_reader_agent, writer_chain, critic_chain, None
    except Exception as e:
        return None, None, None, None, str(e)


def _text(obj):
    return obj.content if hasattr(obj,"content") else str(obj)


# ══════════════════════════════════════════════════════════════════════════════
#  HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="mn-hero">
  <div class="mn-eyebrow">Deep Research Intelligence</div>
  <div class="mn-title">MANAN</div>
  <div class="mn-tagline">AI-Powered &nbsp;·&nbsp; Research Intelligence</div>
  <div class="mn-desc">
    A four-stage AI pipeline — Search, Read, Write, Critique —
    that delivers a publication-ready report on any topic.
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  INPUT  (centred on page by layout="centered" + block-container constraint)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="mn-input-wrap">', unsafe_allow_html=True)
st.markdown('<div class="mn-label">▸ &nbsp;Enter Research Topic</div>',
            unsafe_allow_html=True)

topic = st.text_input(
    label="topic",
    placeholder="e.g.  Future of Autonomous AI Agents",
    key="topic_input",
    label_visibility="collapsed",
)

run_clicked = st.button("⚡  Run Deep Research", key="run_btn",
                        use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PIPELINE CARDS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="mn-pipeline-label">// Pipeline Agents</div>',
            unsafe_allow_html=True)

grid_slot = st.empty()
grid_slot.markdown(_grid(), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  EXECUTION
# ══════════════════════════════════════════════════════════════════════════════
if run_clicked:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        st.session_state.results = None
        st.session_state.error   = None
        for k in KEYS: st.session_state.stages[k] = "idle"

        build_search, build_reader, w_chain, c_chain, imp_err = _load_agents()

        if imp_err:
            st.session_state.error = f"Import error — {imp_err}"
        else:
            state = {}

            # Stage 1 — Search
            st.session_state.stages["search"] = "running"
            grid_slot.markdown(_grid(), unsafe_allow_html=True)
            with st.spinner("🔍  Search Agent scanning the web …"):
                try:
                    r = build_search().invoke({"messages":[
                        ("user", f"Find recent, reliable and detailed information about: {topic}")
                    ]})
                    state["search_results"] = r["messages"][-1].content
                    st.session_state.stages["search"] = "done"
                except Exception as e:
                    st.session_state.error = f"Search Agent — {e}"

            # Stage 2 — Reader
            if not st.session_state.error:
                st.session_state.stages["reader"] = "running"
                grid_slot.markdown(_grid(), unsafe_allow_html=True)
                with st.spinner("📄  Reader Agent scraping top source …"):
                    try:
                        r = build_reader().invoke({"messages":[
                            ("user",
                             f"Based on the following search results about '{topic}', "
                             f"pick the most relevant URL and scrape it for deeper content.\n\n"
                             f"Search Results:\n{state['search_results'][:800]}")
                        ]})
                        state["scraped_content"] = r["messages"][-1].content
                        st.session_state.stages["reader"] = "done"
                    except Exception as e:
                        st.session_state.error = f"Reader Agent — {e}"

            # Stage 3 — Writer
            if not st.session_state.error:
                st.session_state.stages["writer"] = "running"
                grid_slot.markdown(_grid(), unsafe_allow_html=True)
                with st.spinner("✍  Writer Chain composing report …"):
                    try:
                        combined = (f"SEARCH RESULTS:\n{state['search_results']}\n\n"
                                    f"SCRAPED CONTENT:\n{state['scraped_content']}")
                        state["report"] = w_chain.invoke(
                            {"topic":topic,"research":combined})
                        st.session_state.stages["writer"] = "done"
                    except Exception as e:
                        st.session_state.error = f"Writer Chain — {e}"

            # Stage 4 — Critic
            if not st.session_state.error:
                st.session_state.stages["critic"] = "running"
                grid_slot.markdown(_grid(), unsafe_allow_html=True)
                with st.spinner("⚖  Critic Chain reviewing …"):
                    try:
                        state["feedback"] = c_chain.invoke(
                            {"report": state["report"]})
                        st.session_state.stages["critic"] = "done"
                    except Exception as e:
                        st.session_state.error = f"Critic Chain — {e}"

            if not st.session_state.error:
                st.session_state.results = state

        grid_slot.markdown(_grid(), unsafe_allow_html=True)
        st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  ERROR DISPLAY
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.error:
    st.markdown(f"""
    <div style="background:rgba(0,60,200,.08);border:1px solid rgba(0,80,220,.28);
    border-radius:10px;padding:.9rem 1.1rem;margin:.5rem 0 1.5rem;
    font-family:'Source Code Pro',monospace;font-size:.78rem;
    color:#6090ff;letter-spacing:.05em;">
    ⚠ &nbsp;{st.session_state.error}</div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  RESULTS
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.results:
    res = st.session_state.results

    st.markdown('<hr class="mn-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div class="mn-results-head">
      <span class="mn-results-title">Research Report</span>
      <span class="mn-ok-badge">Complete</span>
    </div>""", unsafe_allow_html=True)

    # Report
    st.markdown('<div class="mn-report-card">', unsafe_allow_html=True)
    st.markdown('<span class="mn-section-label">▸ &nbsp;Final Report</span>',
                unsafe_allow_html=True)
    report_text = _text(res.get("report",""))
    st.markdown(report_text)
    st.markdown('</div>', unsafe_allow_html=True)

    # Feedback
    st.markdown('<div class="mn-report-card feedback">', unsafe_allow_html=True)
    st.markdown('<span class="mn-section-label feedback">▸ &nbsp;Critic Feedback</span>',
                unsafe_allow_html=True)
    feedback_text = _text(res.get("feedback",""))
    st.markdown(feedback_text)
    st.markdown('</div>', unsafe_allow_html=True)

    # Raw outputs
    with st.expander("// Raw — Search Results"):
        st.code(str(res.get("search_results","")), language=None)

    with st.expander("// Raw — Scraped Content"):
        st.code(str(res.get("scraped_content","")), language=None)

    # Download
    st.markdown("<br>", unsafe_allow_html=True)
    dl = f"""# MANAN — Deep Research Report
## Topic: {st.session_state.get("topic_input","")}

---

## Final Report

{report_text}

---

## Critic Feedback

{feedback_text}

---

## Raw Search Results

{res.get("search_results","")}

---

## Scraped Content

{res.get("scraped_content","")}
"""
    st.download_button(
        label="⬇  Download Report  (.md)",
        data=dl,
        file_name=f"manan_report_{int(time.time())}.md",
        mime="text/markdown",
    )

# ══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="mn-footer">
  <div class="mn-footer-line"></div>
  <div class="mn-footer-logo">MANAN</div>
  <div class="mn-footer-sub">
    Multi-Agent AI Deep Research System &nbsp;·&nbsp; Powered by LangChain
  </div>
</div>
""", unsafe_allow_html=True)