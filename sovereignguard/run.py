"""Run a scenario and write the full audit trace.

    python -m sovereignguard.run scenarios/s1_care_transfer.json            # governed (default)
    python -m sovereignguard.run scenarios/s1_care_transfer.json --mode ungoverned
    python -m sovereignguard.run --all                                      # every scenario, both modes

Traces are written to runs/<scenario>__<mode>.json (complete) and .md (readable).
"""
import argparse
import datetime as dt
import json
from pathlib import Path

from . import kb
from .llm import EFFORT, MODEL
from .orchestrator import run_governed, run_ungoverned

ROOT = Path(__file__).resolve().parent.parent


def to_markdown(trace):
    s = trace["scenario"]
    out = [f"# {s['title']} - {trace['result']['mode']} run", "",
           f"- Scenario: `{s['id']}` (simulated, no real patient data)",
           f"- Run at: {trace['run_at']} | model: {trace['model']} | effort: {trace['effort']} | KB fingerprint: {trace['kb_fingerprint']}",
           f"- Patient request ({s.get('language', 'en')}): {s['patient_request']}", ""]
    r = trace["result"]
    for st in r["steps"]:
        step = st["step"]
        out += [f"## Step {step['id']}: {step['title']}",
                f"{step['from_entity']} ({step['from_jurisdiction']}) -> {step['to_entity']} ({step['to_jurisdiction']}), purpose: `{step['purpose']}`", "",
                f"**Outcome: {st['outcome']}** | data released: {st['data_released']}", ""]
        if r["mode"] == "ungoverned":
            out.append("Issues nobody checked:")
            out += [f"- {f['code']} ({f['severity']}): {f['detail']}" for f in st["issues_not_caught"]] or ["- none"]
            out.append("")
            continue
        out += [f"- {x}" for x in st["reasons"]] + [""]
        out.append("Consent tracker findings:")
        out += [f"- {f['code']} ({f['severity']}): {f['detail']}" for f in st["consent_findings"]] or ["- none"]
        out.append("")
        for a in st["assessments"]:
            asm = a["assessment"]
            out += [f"### {a['authority']}: {asm['decision']}",
                    asm["summary"], "",
                    f"Applies because: {asm['applies_because']}", ""]
            if asm["conditions"]:
                out += ["Conditions:"] + [f"- {c}" for c in asm["conditions"]] + [""]
            if asm.get("unmet_conditions"):
                out += ["Still to be met before release (Care Passport items):"] + [f"- {c}" for c in asm["unmet_conditions"]] + [""]
            if asm["open_questions"]:
                out += ["Open questions:"] + [f"- {q}" for q in asm["open_questions"]] + [""]
            out.append(f"Citations ({a['citation_check']['verified']}/{a['citation_check']['total']} matched to source text):")
            for c in asm["citations"]:
                mark = "verified" if c["verified"] else "NOT VERIFIED"
                out.append(f"- [{c['excerpt_id']}] ({mark}) \"{c['quote']}\" - {c.get('document', '?')}")
            out.append("")
    if r["mode"] == "governed":
        out.append("## Gap register")
        out += [f"- {g['type']} (step {g['step']}): {g.get('detail') or g.get('regulator', '') + ' silent on: ' + g.get('question', '')}"
                for g in r["gap_register"]] or ["- none"]
        p = r["patient_plan"]["plan"]
        out += ["", f"## Patient action plan ({p['language']})", f"**{p['headline']}**", "",
                p["status_in_plain_words"], ""] + [f"{i}. {x}" for i, x in enumerate(p["what_you_need_to_do"], 1)] + [
               "", p["what_happens_next"], "", f"_{p['disclaimer']}_"]
    return "\n".join(out) + "\n"


def run_one(path: Path, mode: str):
    scenario = json.loads(path.read_text(encoding="utf-8"))
    result = run_governed(scenario) if mode == "governed" else run_ungoverned(scenario)
    used_model = mode == "governed"
    trace = {"scenario": scenario, "run_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
             "model": MODEL if used_model else "none (no model used in this mode)",
             "effort": EFFORT if used_model else "n/a",
             "kb_fingerprint": kb.kb_fingerprint(), "result": result}
    out_dir = ROOT / "runs"
    out_dir.mkdir(exist_ok=True)
    stem = f"{scenario['id']}__{mode}"
    (out_dir / f"{stem}.json").write_text(json.dumps(trace, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / f"{stem}.md").write_text(to_markdown(trace), encoding="utf-8")
    print(f"{stem}: " + ", ".join(f"step {s['step']['id']}={s['outcome']}" for s in result["steps"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario", nargs="?")
    ap.add_argument("--mode", choices=["governed", "ungoverned"], default="governed")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    if a.all:
        for p in sorted((ROOT / "scenarios").glob("*.json")):
            for m in ("ungoverned", "governed"):
                run_one(p, m)
    elif a.scenario:
        run_one(Path(a.scenario), a.mode)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
