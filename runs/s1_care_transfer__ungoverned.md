# Continuing treatment: Abu Dhabi hospital to Dubai hospital - ungoverned run

- Scenario: `s1_care_transfer` (simulated, no real patient data)
- Run at: 2026-11-10T17:16:06+00:00 | model: none (no model used in this mode) | effort: n/a | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I am being treated at a hospital in Abu Dhabi and I am moving to Dubai. Please send my medical records to my new hospital in Dubai so my treatment can continue.

## Step 1: Release treatment record to the Dubai hospital
Origin hospital (DoH-licensed, Abu Dhabi) (DOH) -> Receiving hospital (DHA-licensed, Dubai) (DHA), purpose: `treatment`

**Outcome: TRANSFERRED_WITHOUT_CHECKS** | data released: True

Issues nobody checked:
- CROSS_JURISDICTION_CONSENT (MEDIUM): Consent for 'treatment' was recorded under DOH; the receiving party is under DHA. Whether the receiving regulator recognises that consent must be checked.

