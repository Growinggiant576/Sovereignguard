# Continuing treatment, after the Care Passport checklist is completed - ungoverned run

- Scenario: `s4_care_transfer_completed` (simulated, no real patient data)
- Run at: 2026-11-10T18:57:12+00:00 | model: none (no model used in this mode) | effort: n/a | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I have signed the consent forms both hospitals gave me. Please send my records to my new hospital in Dubai so my treatment can continue.

## Step 1: Release treatment record to the Dubai hospital
Origin hospital (DoH-licensed, Abu Dhabi) (DOH) -> Receiving hospital (DHA-licensed, Dubai) (DHA), purpose: `treatment`

**Outcome: TRANSFERRED_WITHOUT_CHECKS** | data released: True

Issues nobody checked:
- none

