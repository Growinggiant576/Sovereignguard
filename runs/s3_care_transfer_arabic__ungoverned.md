# Continuing treatment (Arabic-speaking patient) - ungoverned run

- Scenario: `s3_care_transfer_arabic` (simulated, no real patient data)
- Run at: 2026-11-10T17:16:13+00:00 | model: none (no model used in this mode) | effort: n/a | KB fingerprint: 48837ef86e4ad24e
- Patient request (ar): أتلقى العلاج في مستشفى في أبوظبي وسأنتقل إلى دبي. أرجو إرسال ملفي الطبي إلى مستشفاي الجديد في دبي حتى يستمر علاجي.

## Step 1: Release treatment record to the Dubai hospital
Origin hospital (DoH-licensed, Abu Dhabi) (DOH) -> Receiving hospital (DHA-licensed, Dubai) (DHA), purpose: `treatment`

**Outcome: TRANSFERRED_WITHOUT_CHECKS** | data released: True

Issues nobody checked:
- CROSS_JURISDICTION_CONSENT (MEDIUM): Consent for 'treatment' was recorded under DOH; the receiving party is under DHA. Whether the receiving regulator recognises that consent must be checked.

