"""SovereignGuard demo dashboard (local only).

Start it with:   sh run_dashboard.sh
It binds to 127.0.0.1 (this computer only) and refuses to start on any other address.

Tabs:
  1. Scenarios    - saved runs, side by side: without vs with SovereignGuard (no API key needed)
  2. Run live     - re-run a scenario with the agents (needs ANTHROPIC_API_KEY in .env; costs API credit)
  3. Knowledge base - search one regulator's documents (local, no API key needed)
  4. Architecture - how the building blocks connect, mapped to ITU-T Y.3172
"""
import json
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
RUNS = ROOT / "runs"
SCENARIOS = ROOT / "scenarios"

st.set_page_config(page_title="SovereignGuard", layout="wide")

# Fail closed: this demo has no login, so it must only be reachable from this computer.
_addr = st.get_option("server.address")
if _addr not in ("127.0.0.1", "localhost"):
    st.error("SovereignGuard's dashboard only runs on this computer. Start it with: sh run_dashboard.sh")
    st.stop()

OUTCOME_LABEL = {
    "PROCEED": ":green[**RELEASED**]",
    "PAUSE": ":orange[**HOLD**]",
    "BLOCK": ":red[**BLOCKED**]",
    "TRANSFERRED_WITHOUT_CHECKS": ":gray[**SENT WITHOUT CHECKS**]",
}
DECISION_LABEL = {
    "PERMIT": ":green[PERMIT]",
    "PERMIT_WITH_CONDITIONS": ":orange[PERMIT WITH CONDITIONS]",
    "BLOCK": ":red[BLOCK]",
    "SILENT": ":violet[SILENT - rules do not address this]",
    "NOT_APPLICABLE": ":gray[NOT APPLICABLE]",
}


def load_trace(scenario_id: str, mode: str):
    p = RUNS / f"{scenario_id}__{mode}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def scenario_ids():
    return sorted(p.stem for p in SCENARIOS.glob("*.json"))


def show_ungoverned(trace):
    st.subheader("Without SovereignGuard")
    for st_ in trace["result"]["steps"]:
        step = st_["step"]
        with st.container(border=True):
            st.markdown(f"**Step {step['id']}: {step['title']}**")
            st.error("**SENT** - no checks. The record moved immediately.")
            issues = st_["issues_not_caught"]
            if issues:
                st.markdown("Issues nobody checked:")
                for f in issues:
                    st.markdown(f"- `{f['code']}` ({f['severity']}): {f['detail']}")
            else:
                st.markdown("No consent issues recorded.")


def show_governed(trace):
    r = trace["result"]
    st.subheader("With SovereignGuard")
    for st_ in r["steps"]:
        step = st_["step"]
        with st.container(border=True):
            st.markdown(f"**Step {step['id']}: {step['title']}**")
            st.caption(f"{step['from_entity']} → {step['to_entity']} · purpose: {step['purpose'].replace('_', ' ')}")
            n_missing = sum(len(a["assessment"].get("unmet_conditions", [])) for a in st_["assessments"])
            if st_["outcome"] == "PROCEED":
                st.success("**RELEASED** - every regulator is satisfied. The record was released and the handoff recorded.")
            elif st_["outcome"] == "BLOCK":
                st.error("**BLOCKED** - " + "; ".join(st_["reasons"]) + ". The record was not released.")
            else:
                st.warning(f"**ON HOLD** - {n_missing} item(s) still needed before release. The record was not released.")

            passport = [(a["agent"], c) for a in st_["assessments"] for c in a["assessment"].get("unmet_conditions", [])]
            if passport and st_["outcome"] != "BLOCK":
                st.markdown("**Care Passport: what is still needed**")
                for agent, c in passport:
                    st.markdown(f"☐ **{agent}:** {c}")
            silent = [a["agent"] for a in st_["assessments"] if a["assessment"]["decision"] == "SILENT"]
            if silent:
                st.markdown(f":violet[**Rules silent:** {', '.join(silent)}. Held for human review and logged as a gap.]")

            if st_["consent_findings"]:
                with st.expander("Consent tracker findings"):
                    for f in st_["consent_findings"]:
                        st.markdown(f"- `{f['code']}` ({f['severity']}): {f['detail']}")

            st.markdown("**Each regulator, checked independently**")
            cols = st.columns(len(st_["assessments"]))
            for col, a in zip(cols, st_["assessments"]):
                asm, cc = a["assessment"], a["citation_check"]
                with col:
                    with st.container(border=True):
                        st.markdown(f"**{a['agent']}**")
                        st.markdown(DECISION_LABEL.get(asm["decision"], asm["decision"]))
                        st.caption(f"✅ {cc['verified']}/{cc['total']} quotes matched to the source text")
                        with st.expander("Why"):
                            st.caption(a["authority"])
                            st.write(asm["summary"])
                        with st.expander("Quoted clauses"):
                            for c in asm["citations"]:
                                mark = "✅" if c["verified"] else "⚠️ not matched"
                                st.markdown(f"{mark} *\"{c['quote']}\"*  \n{c.get('document', '')} · `{c['excerpt_id']}`")
                        if asm["open_questions"]:
                            with st.expander("Open questions"):
                                for q in asm["open_questions"]:
                                    st.markdown(f"- {q}")

    if r["gap_register"]:
        st.markdown("**Gap register (evidence for regulators)**")
        st.dataframe([{"type": g["type"], "step": g["step"],
                       "detail": g.get("detail") or f"{g.get('regulator', '')} silent: {g.get('question', '')}"}
                      for g in r["gap_register"]], width="stretch", hide_index=True)

    plan = r["patient_plan"]["plan"]
    st.markdown("**Message to the patient**")
    rtl = plan["language"].lower().startswith("ar")
    body = (f"**{plan['headline']}**\n\n{plan['status_in_plain_words']}\n\n"
            + "\n".join(f"{i}. {x}" for i, x in enumerate(plan["what_you_need_to_do"], 1))
            + f"\n\n{plan['what_happens_next']}\n\n_{plan['disclaimer']}_")
    with st.container(border=True):
        if rtl:
            st.markdown(f'<div dir="rtl" style="text-align:right">{body}</div>', unsafe_allow_html=True)
        else:
            st.markdown(body)


st.title("SovereignGuard")
st.markdown("**Passport control for health records.** Before a patient's record leaves a hospital, "
            "one agent per UAE regulator (Dubai DHA, Abu Dhabi DoH, federal law) checks it against that "
            "regulator's own documents. The record is **released**, **held** with one checklist of what is "
            "missing, or **blocked**. _Research prototype on simulated scenarios; not legal advice._")

tab_s, tab_live, tab_kb, tab_arch = st.tabs(["Scenarios", "Run live", "Knowledge base", "Architecture"])

with tab_s:
    ids = scenario_ids()
    sid = st.selectbox("Scenario", ids, format_func=lambda s: json.loads((SCENARIOS / f"{s}.json").read_text(encoding="utf-8"))["title"])
    gov, ung = load_trace(sid, "governed"), load_trace(sid, "ungoverned")
    if gov:
        st.markdown(f"**Patient request:** {gov['scenario']['patient_request']}")
        st.caption(f"Run at {gov['run_at']} · model {gov['model']} · effort {gov['effort']} · knowledge base {gov['kb_fingerprint']}")
    left, right = st.columns([1, 2])
    with left:
        if ung:
            show_ungoverned(ung)
        else:
            st.info("No saved run without governance for this scenario.")
    with right:
        if gov:
            show_governed(gov)
        else:
            st.info("No saved governed run for this scenario. Use the Run live tab.")

with tab_live:
    st.markdown("Re-run a scenario with the agents. This calls the Anthropic API and uses credit "
                "(about $0.20-0.40 per scenario, our estimate). Results overwrite the saved run.")
    key_ok = (ROOT / ".env").exists() and "ANTHROPIC_API_KEY=" in (ROOT / ".env").read_text(encoding="utf-8")
    if not key_ok:
        st.warning("No ANTHROPIC_API_KEY found in .env. Saved runs in the Scenarios tab still work.")
    live_id = st.selectbox("Scenario to run", scenario_ids(), key="live")
    if st.button("Run with agents", disabled=not key_ok):
        from sovereignguard.run import run_one
        with st.spinner("Asking the regulator agents..."):
            run_one(SCENARIOS / f"{live_id}.json", "governed")
            run_one(SCENARIOS / f"{live_id}.json", "ungoverned")
        st.success("Done. Open the Scenarios tab to see the new result.")

with tab_kb:
    st.markdown("Search one regulator's documents directly (runs locally, no API key).")
    part = st.radio("Regulator", ["FEDERAL", "DHA", "DOH"], horizontal=True)
    q = st.text_input("Search", "store or transfer health data outside the country")
    if q:
        from sovereignguard import kb
        for e in kb.search(part, q, k=5):
            with st.container(border=True):
                st.markdown(f"**{e['title']}** · `{e['excerpt_id']}` · distance {e['distance']}")
                st.text(e["text"][:900])

with tab_arch:
    st.graphviz_chart("""
digraph G {
  rankdir=LR; node [shape=box, style="rounded,filled", fillcolor="#f5f7fa", fontname="Helvetica"];
  req  [label="SRC\\nHandoff request\\n+ consent records", fillcolor="#e8f0fe"];
  kbn  [label="C / PP\\nKnowledge base\\n12 public UAE documents\\nsplit by regulator"];
  ct   [label="Consent Chain Tracker\\n(rules, no AI)"];
  dha  [label="M\\nDHA agent"]; doh [label="M\\nDoH agent"]; fed [label="M\\nFederal agent"];
  cv   [label="Citation verifier\\n(rules)"];
  co   [label="P\\nCoordinator\\nfail-closed rules", fillcolor="#fff4e5"];
  rel  [label="D / SINK\\nRELEASED\\n+ ledger record", fillcolor="#e6f4ea"];
  hold [label="D / SINK\\nHOLD\\nCare Passport checklist", fillcolor="#fff4e5"];
  blk  [label="D / SINK\\nBLOCKED", fillcolor="#fce8e6"];
  nav  [label="Patient Navigator\\n(English / Arabic)"];
  gap  [label="Gap register\\nfor regulators"];
  req -> ct -> co; req -> dha; req -> doh; req -> fed;
  kbn -> dha [label="DHA only"]; kbn -> doh [label="DoH only"]; kbn -> fed [label="Federal only"];
  dha -> cv; doh -> cv; fed -> cv; cv -> co;
  co -> rel; co -> hold; co -> blk; co -> gap; hold -> nav; rel -> nav; blk -> nav;
  hold -> req [label="evidence provided,\\nre-check", style=dashed];
}
""", width="stretch")
    st.caption("Labels SRC, C, PP, M, P, D, SINK are the ITU-T Y.3172 pipeline nodes (architectural mapping, not a conformance claim).")
