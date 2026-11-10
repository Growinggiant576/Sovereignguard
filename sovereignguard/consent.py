"""Consent Chain Tracker - deterministic, rule-based component (no language model).

Keeps a ledger of what the patient consented to, under which regulator's framework,
and checks each proposed handoff against it. Because it is plain rules over a simple
record format, it can be reused unchanged for any data-sharing domain (education
records, financial data, ...): only the purpose and jurisdiction labels change.
"""


class ConsentLedger:
    def __init__(self, consents):
        self.consents = list(consents)
        self.transfers = []  # handoffs that actually executed

    def check(self, step):
        findings = []
        purpose = step["purpose"]
        covering = [c for c in self.consents if purpose in c["purposes"]]
        if not covering:
            granted = sorted({p for c in self.consents for p in c["purposes"]})
            findings.append({
                "code": "PURPOSE_NOT_COVERED", "severity": "HIGH",
                "detail": f"Proposed purpose '{purpose}' is not in any recorded consent "
                          f"(recorded purposes: {', '.join(granted) or 'none'}).",
            })
        else:
            frameworks = sorted({c["recorded_under"] for c in covering})
            if step["to_jurisdiction"] not in frameworks and step["to_jurisdiction"] != "OUTSIDE_UAE":
                findings.append({
                    "code": "CROSS_JURISDICTION_CONSENT", "severity": "MEDIUM",
                    "detail": f"Consent for '{purpose}' was recorded under {', '.join(frameworks)}; "
                              f"the receiving party is under {step['to_jurisdiction']}. Whether the "
                              f"receiving regulator recognises that consent must be checked.",
                })
        if step.get("to_location") == "OUTSIDE_UAE":
            findings.append({
                "code": "CROSS_BORDER_TRANSFER", "severity": "HIGH",
                "detail": "Data would be stored or processed outside the UAE.",
            })
        if step.get("deidentified"):
            findings.append({
                "code": "DEIDENTIFIED_CLAIM", "severity": "INFO",
                "detail": "Sender states the data is de-identified; each regulator's definition must be checked.",
            })
        return findings

    def record_transfer(self, step):
        self.transfers.append(step["id"])
