# Secondary use: the same record reused for AI model training - ungoverned run

- Scenario: `s2_research_reuse` (simulated, no real patient data)
- Run at: 2026-11-10T17:16:09+00:00 | model: none (no model used in this mode) | effort: n/a | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I only agreed to share my records for my treatment. I want to know who else can use them.

## Step 1: Dubai hospital shares de-identified record with an AI research partner
Receiving hospital (DHA-licensed, Dubai) (DHA) -> AI research partner (Dubai) (DHA), purpose: `research_ai_training`

**Outcome: TRANSFERRED_WITHOUT_CHECKS** | data released: True

Issues nobody checked:
- PURPOSE_NOT_COVERED (HIGH): Proposed purpose 'research_ai_training' is not in any recorded consent (recorded purposes: treatment).
- DEIDENTIFIED_CLAIM (INFO): Sender states the data is de-identified; each regulator's definition must be checked.

## Step 2: Research partner processes the data on a cloud server outside the UAE
AI research partner (Dubai) (DHA) -> Cloud processing provider (outside the UAE) (OUTSIDE_UAE), purpose: `research_ai_training`

**Outcome: TRANSFERRED_WITHOUT_CHECKS** | data released: True

Issues nobody checked:
- PURPOSE_NOT_COVERED (HIGH): Proposed purpose 'research_ai_training' is not in any recorded consent (recorded purposes: treatment).
- CROSS_BORDER_TRANSFER (HIGH): Data would be stored or processed outside the UAE.
- DEIDENTIFIED_CLAIM (INFO): Sender states the data is de-identified; each regulator's definition must be checked.

