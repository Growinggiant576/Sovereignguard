"""The two language-model agents.

JurisdictionAgent - one reusable class; each instance represents ONE regulator and
  can only read that regulator's partition of the knowledge base. Swap the partition
  (e.g. two education regulators, two financial regulators) and the same class works
  in another domain.
NavigatorAgent - turns the structured results into a plain-language action plan for
  the patient, in the patient's language.
"""
import json
import re

from . import kb
from .llm import complete_json

PURPOSE_TERMS = {
    "treatment": "transfer of medical record to another entity for continuing care and treatment",
    "research_ai_training": "scientific and clinical research purposes secondary use",
}

DECISIONS = ["PERMIT", "PERMIT_WITH_CONDITIONS", "BLOCK", "SILENT", "NOT_APPLICABLE"]

ASSESSMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "decision": {"type": "string", "enum": DECISIONS},
        "summary": {"type": "string"},
        "applies_because": {"type": "string"},
        "conditions": {"type": "array", "items": {"type": "string"}},
        "unmet_conditions": {"type": "array", "items": {"type": "string"}},
        "open_questions": {"type": "array", "items": {"type": "string"}},
        "citations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "excerpt_id": {"type": "string"},
                    "quote": {"type": "string"},
                    "supports": {"type": "string"},
                },
                "required": ["excerpt_id", "quote", "supports"],
                "additionalProperties": False,
            },
        },
        "evidence_sufficient": {"type": "boolean"},
    },
    "required": ["decision", "summary", "applies_because", "conditions", "unmet_conditions",
                 "open_questions", "citations", "evidence_sufficient"],
    "additionalProperties": False,
}

JURISDICTION_SYSTEM = """You are the {name} assessor inside SovereignGuard, a research prototype.
You represent ONLY the published rules of {authority}. You can see only excerpts from
that authority's documents in the knowledge base. You assess ONE proposed handoff of a
patient's health data.

Rules you must follow:
1. Use only the knowledge-base excerpts given to you. Do not use outside knowledge of any law.
2. Every requirement, permission or prohibition you state must be backed by a citation:
   the excerpt_id and a quote copied character-for-character from that excerpt (keep quotes short, one or two sentences).
3. If the excerpts do not address the question, set decision to SILENT and evidence_sufficient to false.
   Never guess to fill a gap. Saying the rules are silent is a valid, useful answer.
4. Decisions: PERMIT (allowed as described), PERMIT_WITH_CONDITIONS (allowed only if the listed
   conditions are met), BLOCK (prohibited as described), SILENT (excerpts do not address it),
   NOT_APPLICABLE (the excerpts show this authority's rules do not govern this step - cite why).
5. Put anything the excerpts leave unclear into open_questions.
6. The step may include evidence_provided (for example a signed consent or the sharing route used).
   Put in unmet_conditions only the requirements that this evidence does not yet show as met.
   Ongoing duties after the handoff (keep confidential, use only for health purposes) belong in
   conditions, not in unmet_conditions, when the receiver has committed to them in the evidence.
7. This is an assessment for human review, not legal advice."""


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


class JurisdictionAgent:
    def __init__(self, code: str, name: str, authority: str, partition: str, k: int = 6):
        self.code, self.name, self.authority, self.partition, self.k = code, name, authority, partition, k

    def assess(self, step: dict, consent_findings: list) -> dict:
        # Several focused searches, merged: the plain question alone can be pulled off-topic
        # (e.g. "AI model" matches strategy documents instead of the binding consent rules).
        queries = [f"{step['question']} {step['purpose']} {' '.join(step['data_categories'])}"]
        queries.append(f"patient consent sharing disclosure of health information {PURPOSE_TERMS.get(step['purpose'], step['purpose'])}")
        if step.get("deidentified"):
            queries.append("de-identified anonymised pseudonymised data secondary use")
        if step.get("to_location") == "OUTSIDE_UAE":
            queries.append("store develop or transfer health data and information outside the country")
        merged = {}
        for q in queries:
            for e in kb.search(self.partition, q, k=self.k):
                if e["excerpt_id"] not in merged or e["distance"] < merged[e["excerpt_id"]]["distance"]:
                    merged[e["excerpt_id"]] = e
        excerpts = sorted(merged.values(), key=lambda e: e["distance"])[:10]
        query = " || ".join(queries)
        excerpt_block = "\n\n".join(
            f"<excerpt id=\"{e['excerpt_id']}\" document=\"{e['title']}\">\n{e['text']}\n</excerpt>"
            for e in excerpts
        )
        user = (
            "Proposed handoff step:\n" + json.dumps(step, indent=2, ensure_ascii=False)
            + "\n\nConsent tracker findings for this step:\n"
            + json.dumps(consent_findings, indent=2, ensure_ascii=False)
            + f"\n\nKnowledge-base excerpts from {self.authority}:\n" + excerpt_block
            + "\n\nAssess this step under your authority's rules only."
        )
        system = JURISDICTION_SYSTEM.format(name=self.name, authority=self.authority)
        result, meta = complete_json(system, user, ASSESSMENT_SCHEMA)

        # Audit check: every quote must really appear in the excerpt it cites.
        by_id = {e["excerpt_id"]: e for e in excerpts}
        for c in result["citations"]:
            src = by_id.get(c["excerpt_id"])
            c["verified"] = bool(src) and _norm(c["quote"]) in _norm(src["text"])
            if src:
                c["document"] = src["title"]
                c["source_url"] = src["source_url"]
        unverified = [c for c in result["citations"] if not c["verified"]]

        return {
            "agent": self.code,
            "authority": self.authority,
            "partition": self.partition,
            "query": query,
            "retrieved": [{k: e[k] for k in ("excerpt_id", "title", "distance")} for e in excerpts],
            "assessment": result,
            "citation_check": {
                "total": len(result["citations"]),
                "verified": len(result["citations"]) - len(unverified),
                "unverified_ids": [c["excerpt_id"] for c in unverified],
            },
            "llm": meta,
        }


PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "language": {"type": "string"},
        "headline": {"type": "string"},
        "status_in_plain_words": {"type": "string"},
        "what_you_need_to_do": {"type": "array", "items": {"type": "string"}},
        "what_happens_next": {"type": "string"},
        "disclaimer": {"type": "string"},
    },
    "required": ["language", "headline", "status_in_plain_words", "what_you_need_to_do",
                 "what_happens_next", "disclaimer"],
    "additionalProperties": False,
}

NAVIGATOR_SYSTEM = """You are the Patient Navigator inside SovereignGuard, a research prototype.
You receive the structured results of regulator assessments for a patient's health-data handoff.
Write a short, plain-language action plan for the patient.
Rules:
- Use ONLY facts in the results given to you. Do not add legal claims of your own.
- If a step was paused or blocked, say why in simple words and what the patient can do.
- If the regulators' rules were silent on something, say plainly that the rules do not yet cover it.
- Write in the language code given (e.g. "en" = English, "ar" = Arabic). Keep it under 180 words.
- Include a one-line disclaimer that this is a prototype, not legal or medical advice."""


class NavigatorAgent:
    code = "NAVIGATOR"

    def plan(self, patient_request: str, language: str, step_results: list) -> dict:
        compact = [{
            "step": r["step"]["title"],
            "outcome": r["outcome"],
            "reasons": r["reasons"],
            "regulators": {a["agent"]: {
                "decision": a["assessment"]["decision"],
                "summary": a["assessment"]["summary"],
                "conditions": a["assessment"]["conditions"],
                "still_needed": a["assessment"]["unmet_conditions"],
            } for a in r["assessments"]},
            "data_released": r["data_released"],
        } for r in step_results]
        user = (f"Language: {language}\nPatient's request: {patient_request}\n\nResults:\n"
                + json.dumps(compact, indent=2, ensure_ascii=False))
        result, meta = complete_json(NAVIGATOR_SYSTEM, user, PLAN_SCHEMA)
        return {"agent": self.code, "plan": result, "llm": meta}
