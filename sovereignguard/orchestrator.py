"""Coordinator - deterministic code, no language model.

For each handoff step it: runs the Consent Chain Tracker, asks every regulator agent
whose rules may apply (sender's, receiver's, and federal) IN PARALLEL and independently,
then compares their answers. Divergence between regulators, silence, and consent gaps
are written to a Gap Register. The step outcome is fail-closed:
  BLOCK   - any regulator blocks
  PAUSE   - consent gap, conditions not yet met, silence, or an unverified citation -> human review;
            the unmet conditions from every regulator form one checklist (the Care Passport)
  PROCEED - every applicable regulator permits, all conditions are met, the consent chain is intact
            -> data is released and the handoff is recorded in the consent ledger
"""
from concurrent.futures import ThreadPoolExecutor

from .agents import JurisdictionAgent, NavigatorAgent
from .consent import ConsentLedger

REGULATORS = {
    "FEDERAL": JurisdictionAgent("FEDERAL", "UAE Federal", "UAE federal law and federal health policy (incl. MOHAP)", "FEDERAL"),
    "DHA": JurisdictionAgent("DHA", "Dubai Health Authority", "Dubai Health Authority (DHA)", "DHA"),
    "DOH": JurisdictionAgent("DOH", "Department of Health - Abu Dhabi", "Department of Health - Abu Dhabi (DoH)", "DOH"),
}


def regulators_for(step):
    codes = []
    for j in (step["from_jurisdiction"], step["to_jurisdiction"], "FEDERAL"):
        if j in REGULATORS and j not in codes:
            codes.append(j)
    return codes


def decide(step, findings, assessments):
    decisions = {a["agent"]: a["assessment"]["decision"] for a in assessments}
    applicable = {k: v for k, v in decisions.items() if v != "NOT_APPLICABLE"}
    reasons, gaps = [], []

    if any(v == "BLOCK" for v in applicable.values()):
        outcome = "BLOCK"
        reasons += [f"{k} blocks this step" for k, v in applicable.items() if v == "BLOCK"]
    else:
        outcome = "PROCEED"
        if any(f["severity"] == "HIGH" for f in findings):
            outcome = "PAUSE"
            reasons += [f"Consent tracker: {f['code']}" for f in findings if f["severity"] == "HIGH"]
        unmet = {a["agent"]: a["assessment"]["unmet_conditions"] for a in assessments
                 if a["assessment"]["decision"] == "PERMIT_WITH_CONDITIONS" and a["assessment"]["unmet_conditions"]}
        if unmet:
            outcome = "PAUSE"
            reasons += [f"{k}: {len(v)} condition(s) still to be met" for k, v in unmet.items()]
        if any(v == "SILENT" for v in applicable.values()):
            outcome = "PAUSE"
            reasons += [f"{k} rules are silent on this step" for k, v in applicable.items() if v == "SILENT"]
        if any(a["citation_check"]["unverified_ids"] for a in assessments):
            outcome = "PAUSE"
            reasons.append("At least one citation could not be matched to the source text")

    for k, v in applicable.items():
        if v == "SILENT":
            gaps.append({"type": "POLICY_SILENCE", "regulator": k, "step": step["id"],
                         "question": step["question"]})
    if len(set(applicable.values())) > 1:
        gaps.append({"type": "COORDINATION_GAP", "step": step["id"],
                     "detail": "Regulators reached different decisions on the same handoff: "
                               + ", ".join(f"{k}={v}" for k, v in applicable.items())})
    for f in findings:
        if f["code"] in ("PURPOSE_NOT_COVERED", "CROSS_JURISDICTION_CONSENT"):
            gaps.append({"type": "CONSENT_CHAIN_GAP", "step": step["id"], "detail": f["detail"]})
    return outcome, reasons, gaps


def run_governed(scenario):
    ledger = ConsentLedger(scenario["consents"])
    results, gap_register = [], []
    for step in scenario["steps"]:
        findings = ledger.check(step)
        codes = regulators_for(step)
        with ThreadPoolExecutor(max_workers=len(codes)) as pool:
            assessments = list(pool.map(lambda c: REGULATORS[c].assess(step, findings), codes))
        outcome, reasons, gaps = decide(step, findings, assessments)
        if outcome == "PROCEED":
            ledger.record_transfer(step)
        gap_register += gaps
        results.append({"step": step, "consent_findings": findings, "assessments": assessments,
                        "outcome": outcome, "reasons": reasons, "data_released": outcome == "PROCEED"})
    plan = NavigatorAgent().plan(scenario["patient_request"], scenario.get("language", "en"), results)
    return {"mode": "governed", "steps": results, "gap_register": gap_register, "patient_plan": plan}


def run_ungoverned(scenario):
    """Baseline: data moves with no checks. The tracker is run afterwards only to show what was missed."""
    ledger = ConsentLedger(scenario["consents"])
    results = []
    for step in scenario["steps"]:
        missed = ledger.check(step)
        ledger.record_transfer(step)
        results.append({"step": step, "outcome": "TRANSFERRED_WITHOUT_CHECKS", "data_released": True,
                        "issues_not_caught": missed})
    return {"mode": "ungoverned", "steps": results}
