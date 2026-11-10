# AI training reuse, after the Care Passport checklist is completed - ungoverned run

- Scenario: `s5_ai_training_completed` (simulated, no real patient data)
- Run at: 2026-11-10T19:10:34+00:00 | model: none (no model used in this mode) | effort: n/a | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I have agreed that my de-identified records can be used to train an AI model for research, as long as they stay in the UAE.

## Step 1: Hospital shares de-identified record with an AI research partner (inside the UAE)
Hospital (DHA-licensed, Dubai) (DHA) -> AI research partner (Dubai) (DHA), purpose: `research_ai_training`

**Outcome: TRANSFERRED_WITHOUT_CHECKS** | data released: True

Issues nobody checked:
- DEIDENTIFIED_CLAIM (INFO): Sender states the data is de-identified; each regulator's definition must be checked.

