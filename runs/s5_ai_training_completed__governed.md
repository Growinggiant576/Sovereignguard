# AI training reuse, after the Care Passport checklist is completed - governed run

- Scenario: `s5_ai_training_completed` (simulated, no real patient data)
- Run at: 2026-11-10T19:11:42+00:00 | model: claude-opus-5-5 | effort: medium | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I have agreed that my de-identified records can be used to train an AI model for research, as long as they stay in the UAE.

## Step 1: Hospital shares de-identified record with an AI research partner (inside the UAE)
Hospital (DHA-licensed, Dubai) (DHA) -> AI research partner (Dubai) (DHA), purpose: `research_ai_training`

**Outcome: PAUSE** | data released: False

- DHA: 4 condition(s) still to be met

Consent tracker findings:
- DEIDENTIFIED_CLAIM (INFO): Sender states the data is de-identified; each regulator's definition must be checked.

### Dubai Health Authority (DHA): PERMIT_WITH_CONDITIONS
DHA excerpts treat research and similar non-care uses as secondary use. They direct entities to consider whether identifiable data is needed, and require consent normally only where anonymous data cannot be used. They also allow anonymised information for training, provided proper controls confirm the anonymisation. Here the data is said to be de-identified, and the patient has also given separate revocable opt-in consent, so the share appears allowable under the cited DHA rules, subject to conditions. Two things are not yet shown. First, nothing confirms the data is truly anonymised rather than pseudonymised; under DHA, pseudonymised data is still identifiable information and must be transferred securely. Second, the data-sharing agreement does not show how data subject rights are handled. This assessment is for human review, not legal advice.

Applies because: Both parties are in Dubai under DHA (the sender is DHA-licensed). The purpose (research / AI training) is a secondary use of health information as DHA defines it.

Conditions:
- The de-identification must be true anonymisation, with proper controls in place to confirm it was performed properly, including handling of quasi-identifiers.
- If the data is in fact pseudonymised (for example, the hospital keeps a re-linking key), it must be treated as personally identifiable PHI, handled cautiously and transferred only by secure means.
- Consent c2 must be recorded and managed as described in the data-sharing agreement, and its revocability honoured.
- Only the minimum data needed for the research function should be shared and accessed.
- The partner must keep to its commitments in the agreement: confidentiality and use for health research only.

Still to be met before release (Care Passport items):
- No evidence that proper controls verified the anonymisation (for example, a re-identification risk review covering quasi-identifiers in the clinical record and imaging, such as image metadata).
- No evidence on whether a re-linking key or pseudonym is kept, which would make the data pseudonymised PHI under DHA.
- The data-sharing agreement, as described, does not show data subject rights or procedures for handling access requests.
- The data-sharing agreement, as described, does not show the details and contact information of the responsible persons at each participating entity.

Open questions:
- Do DHA section 4.17's rules on 'teaching' and 'health education and training' datasets cover AI model training? The excerpts do not say so explicitly.
- The excerpts do not define what counts as adequate anonymisation for imaging data.
- The AI in Healthcare Policy excerpts provided contain only definitions and references, with no substantive requirements for AI training data.
- The excerpts do not address whether research ethics committee approval is required, or whether UAE-only storage is required for this step.

Citations (11/11 matched to source text):
- [dha_health_info_sharing_policy::0012] (verified) "Secondary Use of Health Information: is using health information for purposes other than" - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0023] (verified) "Entity must always consider whether identifiable" - Standards for Health Information Consent and Access Control
- [dha_consent_access_control_std::0023] (verified) "If it is not practicable to work with anonymous data, then consent is normally required" - Standards for Health Information Consent and Access Control
- [dha_health_info_sharing_policy::0043] (verified) "anonymised information on Data Subject/Patients and medical conditions can be" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0043] (verified) "Proper control should be in place to make" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0043] (verified) "4.17.3. If information or media is used which can, directly or indirectly, identify an" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0012] (verified) "Pseudonymised information is still considered" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0012] (verified) "Quasi-identifiers: are variables in the dataset that are not directly identifying but can be" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0050] (verified) "Legal basis for sharing the data and information. If consent is required, then" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0050] (verified) "Data Subject/Patients’ rights including procedures for dealing with data and" - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0029] (verified) "To the extent, technologically feasible users should be granted access only to health" - Standards for Health Information Consent and Access Control

### UAE federal law and federal health policy (incl. MOHAP): PERMIT_WITH_CONDITIONS
Under Federal Law No. 2 of 2019, the hospital may share this data with the Dubai AI research partner, subject to conditions. Article 16 lets patient information be exchanged with the patient's written consent. Separately, it allows exchange for scientific and clinical research if the patient's identity is not disclosed and research ethics are followed. The evidence shows written opt-in consent, ethics committee approval, de-identification and UAE-only storage, so both routes appear covered and no listed requirement is unmet. The receiver remains bound by ongoing duties: keep the data confidential, use it only for health purposes, do not trade it, and do not move it outside the UAE. Some points need human review: whether AI model training counts as 'scientific and clinical research', how de-identification is defined, and the DHA and executive-decree rules not included in these excerpts. This is an assessment for human review, not legal advice.

Applies because: Federal Law No. 2 of 2019 covers all uses of ICT in health fields in the UAE, including free zones. Transferring and storing electronic clinical records and imaging counts as an 'Exchange of Health information' under the law. Both the hospital and the research partner are in Dubai, so the law applies to this step.

Conditions:
- The receiver must keep the shared data confidential and must not use it for non-health purposes (Art. 16). The data-sharing agreement commits to this.
- The patient's identity must not be disclosed at any stage of the research or AI training, including in model outputs or publications (Art. 16(2)).
- The ethics and rules of scientific research must be followed for the whole project, consistent with the ethics committee approval (Art. 16(2)).
- The data must not be traded or exchanged except in authorized cases (Art. 4(1)).
- The data must not be stored, developed or transferred outside the UAE unless a decree is issued by the health authority in coordination with the Ministry (Art. 13). This includes the AI partner's cloud and model-development infrastructure.
- Storage inside the UAE must follow the conditions and controls set by Ministerial Decree (Art. 12), and any rules and standards set by the health authority for its electronic health data systems (Art. 6).

Open questions:
- Do the federal excerpts treat AI model training by a research partner, possibly a commercial one, as 'scientific and clinical research' and as a health purpose under Art. 16? The excerpts do not define research.
- The federal excerpts give no definition or standard for de-identification. Is removing direct identifiers enough to meet 'the patient's identity is not disclosed', especially for imaging data?
- The Ministerial Decree on in-country storage conditions (Art. 12) and the Executive Decree controls (Art. 15(2)) are not in the excerpts. Do they impose extra requirements?
- DHA's own rules and standards under Art. 6 are not in these federal excerpts and need separate assessment.
- The excerpts do not say how revoking the patient's consent affects data already used to train a model.
- Does the partner's work count as 'develop' health information under Art. 13? If so, any offshore model development or hosting would be prohibited without a decree.

Citations (8/8 matched to source text):
- [fed_law_2_2019::0006] (verified) "This law applies to all methods and uses of ICTs in the health fields in the country, including free zones." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0006] (verified) "Exchange of Health information: access, exchange, copying, photocopying, transfer, storage, publication, disclosure or transmission of health data and information." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "anyone who exchanges and circulates patient information must ensure its confidentiality and not use it for non-health purposes, and without the written consent of the patient, except in the following cases:" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "2. The purposes of scientific and clinical research, provided that the patient's identity is not disclosed and that the ethics and rules of scientific research are followed." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0007] (verified) "To maintain the confidentiality of health data and information by not allowing them to be traded or exchanged in other than authorized cases." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "It is not permitted to store, develop, or transfer data and health information outside the country that is related to health services provided within the country, except in cases where a decree is issued by the health authority in coordination with the ministry." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0009] (verified) "A Ministerial Decree in coordination with the health authorities shall determine the conditions and controls for storage of health data and information within the country." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0008] (verified) "The health authority shall establish the rules, standards and standards for its electronic health data and information systems" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare

## Gap register
- none

## Patient action plan (en)
**Your research data share is paused while the hospital finishes some checks**

Both the Dubai Health Authority (DHA) and federal rules say this share can go ahead, but only with conditions. Federal rules show nothing missing. DHA has 4 items still unproven, so the share is paused and no data has been released yet. DHA needs proof that your records are truly anonymised, not just pseudonymised (for example, the hospital keeping a key that could link the data back to you). The agreement also needs to show how your rights and access requests are handled, and who the responsible contacts are at each organisation. Reviewers also noted that whether AI model training counts as 'scientific and clinical research' still needs human review.

1. Nothing is required from you right now; your consent is on record.
2. You can ask the hospital whether a re-linking key is kept for your data.
3. You can ask the hospital how to request access to your data and who the responsible contact is.
4. Remember your consent is revocable; you can withdraw it if you change your mind.

Once the hospital provides the missing DHA evidence, the share can proceed. Your data must stay in the UAE, stay confidential, be used only for health research, and your identity must never be disclosed.

_This is a research prototype, not legal or medical advice._
