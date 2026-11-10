# Secondary use: the same record reused for AI model training - governed run

- Scenario: `s2_research_reuse` (simulated, no real patient data)
- Run at: 2026-11-10T19:12:02+00:00 | model: claude-opus-5-5 | effort: medium | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I only agreed to share my records for my treatment. I want to know who else can use them.

## Step 1: Dubai hospital shares de-identified record with an AI research partner
Receiving hospital (DHA-licensed, Dubai) (DHA) -> AI research partner (Dubai) (DHA), purpose: `research_ai_training`

**Outcome: PAUSE** | data released: False

- Consent tracker: PURPOSE_NOT_COVERED
- DHA: 4 condition(s) still to be met
- FEDERAL: 3 condition(s) still to be met

Consent tracker findings:
- PURPOSE_NOT_COVERED (HIGH): Proposed purpose 'research_ai_training' is not in any recorded consent (recorded purposes: treatment).
- DEIDENTIFIED_CLAIM (INFO): Sender states the data is de-identified; each regulator's definition must be checked.

### Dubai Health Authority (DHA): PERMIT_WITH_CONDITIONS
DHA rules treat research as a secondary use. Such use relies on anonymous data where practicable, and consent is normally required when identifiable data is needed. Anonymised information may be used for training only if proper controls ensure the anonymisation was done properly. Pseudonymised data still counts as personally identifiable. The handoff can proceed without new consent only if the record is truly anonymised, not merely pseudonymised or masked, and the anonymisation is properly controlled. Otherwise consent covering research or AI training is needed, and the recorded consent covers treatment only.

Applies because: Both sender and receiver are in Dubai under DHA jurisdiction. The sender is a DHA-licensed hospital sharing patient health data for research and AI training, which DHA policy defines as a secondary use of health information.

Conditions:
- The shared clinical record and imaging must be genuinely anonymous, so that no individual can be identified directly or indirectly. Pseudonymised, masked or key-coded data does not qualify.
- Proper controls must be in place to verify that the anonymisation has been performed properly, including checking quasi-identifiers and any identifying content embedded in the images.
- The entity must consider whether identifiable patient information is actually needed for the research purpose.
- If identifiable or re-identifiable data is required, consent from the patient for this purpose must be obtained before sharing.
- The legal basis for sharing should be documented, for example in a data sharing agreement.
- Access should be limited to the information needed for the partner's function.

Still to be met before release (Care Passport items):
- No evidence shows the data is anonymised rather than pseudonymised; it is only 'described as de-identified'.
- No evidence shows that proper controls verified the anonymisation.
- No consent covers research or AI training (the recorded purpose is treatment only). This consent is needed if the data turns out to be identifiable or pseudonymised.
- No documented legal basis or data sharing agreement for this sharing is shown.

Open questions:
- Does the DHA teaching/training provision (4.17) cover AI model training, or only health education?
- What de-identification method was used? Is the data anonymised or pseudonymised, and can the hospital or partner re-identify it?
- Do the imaging files contain embedded identifiers or quasi-identifiers?
- Is a data sharing agreement with the AI research partner required in this case, and does one exist?
- Is research ethics approval required? The excerpts do not address it.

Citations (8/8 matched to source text):
- [dha_health_info_sharing_policy::0012] (verified) "Secondary Use of Health Information: is using health information for purposes other than" - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0023] (verified) "If it is not practicable to work with anonymous data, then consent is normally required" - Standards for Health Information Consent and Access Control
- [dha_health_info_sharing_policy::0012] (verified) "Pseudonymised information is still considered" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0043] (verified) "4.17.1. Protected health information should not be used as a dataset for teaching purposes" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0043] (verified) "Proper control should be in place to make" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0043] (verified) "If information or media is used which can, directly or indirectly, identify an" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0050] (verified) "Legal basis for sharing the data and information. If consent is required, then" - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0029] (verified) "To the extent, technologically feasible users should be granted access only to health" - Standards for Health Information Consent and Access Control

### UAE federal law and federal health policy (incl. MOHAP): PERMIT_WITH_CONDITIONS
Under Federal Law No. 2 of 2019, Article 16, patient information may not be used for non-health purposes without the patient's written consent. One listed exception covers scientific and clinical research, but only if the patient's identity is not disclosed and the ethics and rules of scientific research are followed. Treatment-only consent therefore does not by itself block this handoff, provided the AI training qualifies as scientific or clinical research and both conditions are actually met. The evidence does not yet show this: de-identification is only claimed, and no ethics approval or research-rules compliance is documented. The data stays in the UAE, so the Article 13 bar on transfers outside the country is not triggered. This is an assessment for human review, not legal advice.

Applies because: Federal Law No. 2 of 2019 applies to all uses of ICT in health fields in the UAE, including free zones. Here a DHA-licensed Dubai facility is electronically exchanging clinical and imaging data with a Dubai-based partner, which falls within that scope.

Conditions:
- The patient's identity must not be disclosed to the AI research partner. The data must be effectively de-identified, not just labelled as such.
- The ethics and rules of scientific research must be followed for the AI training project.
- The AI model training must qualify as 'scientific and clinical research' under Article 16(2).
- The receiver must keep the information confidential and not use it for non-health purposes.
- The data must not be stored, developed or transferred outside the UAE unless a decree is issued by the health authority in coordination with the Ministry.

Still to be met before release (Care Passport items):
- No evidence shows the data meets the requirement that the patient's identity is not disclosed. The sender only states that the data is de-identified, and no method or verification is provided.
- No evidence shows that the ethics and rules of scientific research are being followed, such as research ethics committee approval or a research protocol.
- No evidence shows that the AI training is a scientific or clinical research activity rather than commercial product development.

Open questions:
- Does training an AI model for a commercial or research partner fall within 'scientific and clinical research' under Article 16(2)? The excerpts do not define the term.
- What standard of de-identification satisfies 'the patient's identity is not disclosed'? Do imaging data and their metadata meet that standard?
- Which specific 'ethics and rules of scientific research' apply, and who approves compliance? The federal excerpts do not specify. DHA-level rules may govern this.
- Do the executive decree or health-authority rules under Articles 6 and 10 impose additional exchange conditions? These were not provided in the excerpts.
- Are there contractual commitments from the partner on confidentiality, non-health use and keeping the data in the UAE?

Citations (5/5 matched to source text):
- [fed_law_2_2019::0011] (verified) "anyone who exchanges and circulates patient information must ensure its confidentiality and not use it for non-health purposes, and without the written consent of the patient, except in the following cases:" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "2. The purposes of scientific and clinical research, provided that the patient's identity is not disclosed and that the ethics and rules of scientific research are followed." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0006] (verified) "This law applies to all methods and uses of ICTs in the health fields in the country, including free zones." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "It is not permitted to store, develop, or transfer data and health information outside the country that is related to health services provided within the country," - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0007] (verified) "To maintain the confidentiality of health data and information by not allowing them to be traded or exchanged in other than authorized cases." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare

## Step 2: Research partner processes the data on a cloud server outside the UAE
AI research partner (Dubai) (DHA) -> Cloud processing provider (outside the UAE) (OUTSIDE_UAE), purpose: `research_ai_training`

**Outcome: BLOCK** | data released: False

- FEDERAL blocks this step

Consent tracker findings:
- PURPOSE_NOT_COVERED (HIGH): Proposed purpose 'research_ai_training' is not in any recorded consent (recorded purposes: treatment).
- CROSS_BORDER_TRANSFER (HIGH): Data would be stored or processed outside the UAE.
- DEIDENTIFIED_CLAIM (INFO): Sender states the data is de-identified; each regulator's definition must be checked.

### Dubai Health Authority (DHA): SILENT
DHA rules govern this data and this AI developer, but the excerpts do not set out when health data may be stored or processed outside the UAE. They only point to Federal Ministerial Decision No 51 of 2021 on 'Cases Allowing the Storage and Transfer' of medical data out of the UAE, and its content is not in the knowledge base. So the excerpts cannot answer the core cross-border question. Related DHA requirements apply to this step regardless: health information includes imaging and non-identifiable data; secondary use such as research normally needs consent unless anonymous data is workable; pseudonymised data is still identifiable and must move only by secure means; and a data sharing agreement must state the legal basis. The recorded consent covers treatment only. A human reviewer should check Ministerial Decision 51/2021 directly. This is an assessment for human review, not legal advice.

Applies because: The DHA AI in Healthcare Policy applies to locally based AI developers that use Dubai patient clinical data to develop AI solutions. The sender is a Dubai AI research partner training models. DHA's definition of health information covers imaging and non-identifiable data, so the de-identification claim does not take the data outside DHA's scope.

Conditions:
- If the data is only pseudonymised rather than anonymous, treat it as personally identifiable and transfer it only by secure means.
- If identifiable or pseudonymised data is needed for research or AI training, obtain consent for that purpose. The recorded consent covers treatment only.
- Document the legal basis for sharing, and how any consent is recorded and managed, in a data sharing agreement.
- Comply with the cross-border rules in Federal Ministerial Decision No 51 of 2021, which DHA policy references. Its specific conditions are not in the excerpts.

Still to be met before release (Care Passport items):
- No consent for research or AI training: the recorded consent covers treatment only.
- No evidence that the data is truly anonymous rather than pseudonymised.
- No evidence of a legal basis for the offshore transfer or that a permitted case under Ministerial Decision 51/2021 applies.
- No evidence of secure transfer means or a data sharing agreement with the cloud provider.

Open questions:
- What conditions or permitted cases does Federal Ministerial Decision No 51 of 2021 set for storing or processing medical data outside the UAE? Its text is not in the excerpts.
- Does DHA's standard for de-identification or anonymisation, if met, remove the need for consent and change the cross-border restrictions?
- Was the de-identification method anonymisation or pseudonymisation, and how is the risk from quasi-identifiers in the imaging and clinical records handled?
- Do any DHA AI policy duties apply specifically to the offshore cloud processor?

Citations (9/9 matched to source text):
- [dha_ai_healthcare_policy::0000] (verified) "National and locally based international AI developers that utilize Dubai based population or patient clinical and nonclinical data to develop AI solutions." - Artificial Intelligence in the Healthcare Policy
- [dha_health_data_protection_policy::0013] (verified) "Federal Ministerial Decision No 51 of 2021 Cases Allowing the Storage and" - Policy for Data and Health Information Protection and Confidentiality
- [dha_health_data_protection_policy::0013] (verified) "Nevertheless, the regulation that is more specialized/detailed in health will" - Policy for Data and Health Information Protection and Confidentiality
- [dha_health_info_sharing_policy::0016] (verified) "3.2.5. Identifiable and non-identifiable data." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0016] (verified) "3.2.4. X-ray and imaging reports, output and images." - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0023] (verified) "If it is not practicable to work with anonymous data, then consent is normally required" - Standards for Health Information Consent and Access Control
- [dha_health_info_sharing_policy::0012] (verified) "Pseudonymised information is still considered" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0012] (verified) "only be transferred using secure means." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0050] (verified) "Legal basis for sharing the data and information." - Policy for Health Data and Information Sharing

### UAE federal law and federal health policy (incl. MOHAP): BLOCK
Federal Law No. 2 of 2019 (Article 13) forbids storing, developing or transferring data and health information about health services provided in the UAE to outside the country. The only exception is a decree issued by the health authority in coordination with the Ministry. No such decree is shown, so offshore cloud processing is blocked as described. Article 16 separately allows research use without written consent if the patient's identity is not disclosed and research ethics are followed. That may cover the consent gap for AI training, but it does not override the Article 13 localisation rule. The de-identification claim does not clearly take the data outside Article 13, whose broad 'Data' definition includes images. This is an assessment for human review, not legal advice.

Applies because: Federal Law No. 2 of 2019 covers all uses of ICT in the health fields in the UAE, including free zones, so it reaches a Dubai-based research partner. The step involves storing and processing clinical records and imaging, linked to health services delivered in the UAE, on a server outside the UAE.

Conditions:
- If a qualifying decree is obtained, the receiver must keep the data confidential and use it only for health purposes (Art. 16).
- Research use without written consent relies on the patient's identity not being disclosed and on the ethics and rules of scientific research being followed (Art. 16(2)).

Still to be met before release (Care Passport items):
- No evidence of a decree from the health authority, issued in coordination with the Ministry, permitting this data to be stored or processed outside the UAE (Art. 13).
- No evidence that the ethics and rules of scientific research are being followed, such as research ethics approval, for the research exception in Art. 16(2).
- No evidence that the de-identification is enough to ensure the patient's identity is not disclosed.

Open questions:
- Does Article 13 apply to de-identified or anonymised data? The excerpts give no exemption, and 'Data' is defined broadly.
- Has the DHA, as the relevant health authority, issued any decree in coordination with MOHAP permitting offshore storage or processing for research or AI training?
- What storage conditions does the Ministerial Decree under Article 12 set? It is not included in the excerpts.
- Does AI model training count as 'scientific and clinical research' under Art. 16(2)?

Citations (6/6 matched to source text):
- [fed_law_2_2019::0010] (verified) "It is not permitted to store, develop, or transfer
data and health information outside the
country that is related to health services
provided within the country, except in cases
where a decree is issued by the health
authority in coordination with the ministry." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0006] (verified) "This law applies to all methods and uses of
ICTs in the health fields in the country,
including free zones." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0006] (verified) "Data: All that can be stored, processed,
generated and transferred by ICT such as
numbers, letters, symbols, images and the like." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "The purposes of scientific and clinical research,
provided that the patient's identity is not disclosed
and that the ethics and rules of scientific research are
followed." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "anyone who exchanges and circulates patient
information must ensure its confidentiality and not
use it for non-health purposes" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0009] (verified) "A Ministerial Decree in coordination with the
health authorities shall determine the
conditions and controls for storage of health
data and information within the country." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare

## Gap register
- CONSENT_CHAIN_GAP (step 1): Proposed purpose 'research_ai_training' is not in any recorded consent (recorded purposes: treatment).
- POLICY_SILENCE (step 2): DHA silent on: May health data be stored or processed outside the UAE for AI model training, and under what conditions?
- COORDINATION_GAP (step 2): Regulators reached different decisions on the same handoff: DHA=SILENT, FEDERAL=BLOCK
- CONSENT_CHAIN_GAP (step 2): Proposed purpose 'research_ai_training' is not in any recorded consent (recorded purposes: treatment).

## Patient action plan (en)
**Your records have not been shared with anyone else. Both steps are on hold.**

Your consent covers treatment only. The hospital wanted to give a 'de-identified' copy to an AI research partner. This is paused: no proof yet shows the data is truly anonymous, no research ethics approval is shown, and there is no data sharing agreement. The partner also planned to process the data on a cloud server outside the UAE. Federal law blocks this unless a health authority decree allows it, and none is shown. Dubai (DHA) rules do not yet cover this offshore step in the material reviewed. Nothing has been released.

1. Nothing is required. Your data stays put unless the missing conditions are met.
2. If anyone asks you to agree to research or AI training, you may say yes or no. Your current consent does not cover it.
3. Ask the hospital how it would prove your data is truly anonymous and whether ethics approval exists.

Sharing can go ahead only if the hospital provides the missing proof. Offshore processing stays blocked unless a decree is issued. A human reviewer will check these results.

_This is a research prototype, not legal or medical advice._
