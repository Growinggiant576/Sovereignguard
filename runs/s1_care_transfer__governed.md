# Continuing treatment: Abu Dhabi hospital to Dubai hospital - governed run

- Scenario: `s1_care_transfer` (simulated, no real patient data)
- Run at: 2026-11-10T19:11:39+00:00 | model: claude-opus-5-5 | effort: medium | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I am being treated at a hospital in Abu Dhabi and I am moving to Dubai. Please send my medical records to my new hospital in Dubai so my treatment can continue.

## Step 1: Release treatment record to the Dubai hospital
Origin hospital (DoH-licensed, Abu Dhabi) (DOH) -> Receiving hospital (DHA-licensed, Dubai) (DHA), purpose: `treatment`

**Outcome: PAUSE** | data released: False

- DOH: 2 condition(s) still to be met
- DHA: 3 condition(s) still to be met
- FEDERAL: 1 condition(s) still to be met

Consent tracker findings:
- CROSS_JURISDICTION_CONSENT (MEDIUM): Consent for 'treatment' was recorded under DOH; the receiving party is under DHA. Whether the receiving regulator recognises that consent must be checked.

### Department of Health - Abu Dhabi (DoH): PERMIT_WITH_CONDITIONS
Under the DoH excerpts, an Abu Dhabi facility may share identifiable records with a Dubai hospital for continuing treatment, subject to conditions. Written patient consent is required unless a listed exception applies; the Malaffi (ADHIE) exchange exception covers only facilities on that platform. The receiver must keep the data confidential and use it only for health purposes. The patient's selective-disclosure choices must be respected. The ban on transfers outside the UAE does not apply because Dubai is in the UAE. No evidence of written consent was provided.

Applies because: The sender is a DoH-licensed facility in Abu Dhabi disclosing protected health information about care given in Abu Dhabi. DoH standards bind anyone who exchanges and circulates that information.

Conditions:
- Obtain the patient's written consent for this disclosure, unless the exchange happens over the Malaffi/ADHIE platform between participating facilities (a listed exception).
- The receiving facility must keep the information confidential.
- The information must not be used for non-health purposes; here the use is limited to continuing treatment.
- Respect any selective-disclosure instruction from the patient limiting which facilities may receive the records.
- Apply 'need to know' and 'least privilege': share only what is needed for continuing treatment.
- Data must stay within the UAE; any onward transfer outside the UAE needs a DoH exception.

Still to be met before release (Care Passport items):
- No signed written patient consent for disclosure to the Dubai hospital has been provided, and no evidence shows the exchange uses the Malaffi/ADHIE platform between participating facilities.
- No evidence confirms the patient has not restricted disclosure to this facility through selective disclosure.

Open questions:
- Is the Dubai (DHA-licensed) hospital a participant in Malaffi/ADHIE? If so, does the HIE consent or exception cover this exchange? The Malaffi notice mentions facilities 'elsewhere', but the standard's exception refers to facilities on the Malaffi platform.
- Does the existing 'treatment' consent recorded under DOH meet the written-consent requirement for disclosure to an out-of-emirate facility? Does DHA recognise that consent? DHA's view is outside DoH's excerpts.
- The excerpts list exceptions to written consent only partly (some items are cut off). Could another exception, for example continuity of care, apply?

Citations (8/8 matched to source text):
- [doh_patient_data_privacy_std::0009] (verified) "Must not use it without the written consent of the patient, except in the following cases." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "Must ensure its confidentiality." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "Must not use it for non-health purposes." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "No entity is permitted to store, develop, or transfer PHI outside the United Arab Emirates that is related to health services provided within Abu Dhabi" - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0012] (verified) "Health information exchange between healthcare facilities on Abu Dhabi Health Information Exchange platform, Malaffi." - DOH Standard on Patient Healthcare Data Privacy
- [doh_malaffi_privacy_notice::0006] (verified) "for the purpose of enabling such other Healthcare Facilities in the Emirate of Abu Dhabi and elsewhere" - Privacy Notice
- [doh_patient_data_privacy_std::0016] (verified) "Patients shall have the authority for selective disclosure of their health information to entities (e.g. hospitals, health care providers etc.) as deemed necessary." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0016] (verified) "Entities shall adopt the principles of ‘need to know’ and ‘least privilege’." - DOH Standard on Patient Healthcare Data Privacy

### Dubai Health Authority (DHA): PERMIT_WITH_CONDITIONS
DHA rules allow identifiable treatment records to be shared between licensed UAE entities for continuing care, but only with patient consent. That consent can come through a referral process with clear signed consent, or through health information exchange (Nabidh, Malaffi, Riayati) with patient consent. Where the receiving entity requests the record on a transfer of care, separate patient consent is required. No consent recognised under DHA requirements has been shown for this step. Whether the DOH-recorded consent satisfies DHA has not been confirmed.

Applies because: The receiving hospital is DHA-licensed in Dubai. DHA policies cover all entities under DHA jurisdiction and expressly address sharing PHI between entities in the UAE for care purposes. The data categories (clinical records, lab results, imaging) fall within DHA's definition of health information.

Conditions:
- Patient consent must be in place for the transfer. Acceptable routes are a referral process with clear signed consent, or exchange via HIE (Nabidh, Malaffi, Riayati) with patient consent.
- If the Dubai hospital requests the record from the Abu Dhabi hospital on a transfer of care, separate patient consent is required for that request.
- Consent must meet DHA requirements under the Consent & Access Control Policy.
- Only PHI relevant to the necessities of direct care should be shared (clinical record, labs, imaging limited to what treatment needs).
- If PHI is sent by email, the email must be appropriately encrypted or use authenticated portal links, and must be sent from official entity-issued accounts.

Still to be met before release (Care Passport items):
- No evidence of a clear signed patient consent recognised under DHA requirements (Consent & Access Control Policy) for this inter-entity transfer.
- No evidence of the sharing route used (referral process, or HIE exchange via Nabidh/Malaffi/Riayati).
- No evidence of separate patient consent for a request by the Dubai hospital to the Abu Dhabi hospital, if the transfer is initiated that way.

Open questions:
- Does a treatment consent recorded under DOH (e.g., via Malaffi) satisfy DHA's 'clear signed consent' and Consent & Access Control Policy requirements? The excerpts do not say whether DHA recognises consent recorded under another regulator.
- Policy 4.3.1 suggests consent is needed for sharing 'other than direct provision of health care', while the 4.6.5 table requires consent for inter-entity UAE care sharing. The excerpts do not fully reconcile these provisions.
- Is the record being transferred directly with the patient (patient transferring his/her own information), or via request from the Dubai entity? The consent requirement differs between these routes.

Citations (9/9 matched to source text):
- [dha_health_info_sharing_policy::0021] (verified) "request from the other Entity (separate Patient consent is required in this case)." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0021] (verified) "with clear signed" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0021] (verified) "Nabidh, Malaffi," - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0017] (verified) "Consent should be as per DHA requirements (Consent & Access Control Policy)." - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0023] (verified) "All relevant PHI should be accessed and shared as per necessities of direct care to" - Standards for Health Information Consent and Access Control
- [dha_health_data_protection_policy::0011] (verified) "All Entities working under jurisdiction of DHA." - Policy for Data and Health Information Protection and Confidentiality
- [dha_health_info_sharing_policy::0016] (verified) "X-ray and imaging reports, output and images." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0038] (verified) "Health data and information should only be disclosed when the consent of the Data" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0029] (verified) "Protected Health Information should only be sent via email if it is appropriately" - Policy for Health Data and Information Sharing

### UAE federal law and federal health policy (incl. MOHAP): PERMIT_WITH_CONDITIONS
Federal Law No. 2 of 2019 governs ICT-based exchange of health information anywhere in the UAE, so it covers this Abu Dhabi-to-Dubai transfer. Article 16 lets an identifiable record be exchanged only for health purposes, kept confidential, and with the patient's written consent unless a listed exception applies. Exception 3 ('to maintain the health and safety of the patients') may cover continuing treatment, but the excerpts do not say so expressly. The safe course is to confirm that the DOH-recorded treatment consent is in writing and covers disclosure to the Dubai hospital. The Article 13 ban on transfers outside the country is not triggered, because the receiver is in the UAE. The federal excerpts are silent on whether a DHA facility must recognise a DOH-recorded consent. This is an assessment for human review, not legal advice.

Applies because: Federal Law No. 2 of 2019 applies to all uses of ICT in health fields across the UAE, including free zones. Its definition of exchange of health information covers transfer and disclosure of health data, so an electronic handoff of clinical records, lab results and imaging between two UAE facilities falls within it.

Conditions:
- The receiving hospital must keep the patient information confidential.
- The information may be used only for health purposes (here, continuing treatment).
- The patient's written consent is required unless an Article 16 exception applies (for example, maintaining the patient's health and safety).
- The data must stay within the UAE; storage or transfer outside the country requires a health-authority decree issued in coordination with the Ministry.
- If the exchange goes through the federal central system, authorised users must handle only the information needed for the specified purpose and exchange it only with authorised individuals.

Still to be met before release (Care Passport items):
- Written patient consent covering disclosure to the receiving Dubai (DHA-licensed) hospital is not shown. The tracker records a treatment consent under DOH, but it does not show whether that consent is written or whether it extends to this receiver. Alternatively, the parties would need to document reliance on an Article 16 exception.

Open questions:
- Does Article 16 exception 3 ('to maintain the health and safety of the patients') cover routine continuity-of-care sharing between providers, removing the need for written consent? The excerpts do not say expressly.
- Is a consent recorded under DOH rules valid federally for disclosure to a DHA-licensed facility? The federal excerpts do not address recognition of consent between emirates.
- Will the exchange use the federal central system or another channel? Articles 8 and 15 duties apply to central-system users, and the detailed conditions are left to an executive decree that is not in the knowledge base.
- Do Ministry or health-authority mechanisms for exchanging health data (Article 10(5)) impose further procedural requirements? These are not included in the excerpts.

Citations (7/7 matched to source text):
- [fed_law_2_2019::0006] (verified) "This law applies to all methods and uses of ICTs in the health fields in the country, including free zones." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0006] (verified) "Exchange of Health information: access, exchange, copying, photocopying, transfer, storage, publication, disclosure or transmission of health data and information." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "anyone who exchanges and circulates patient information must ensure its confidentiality and not use it for non-health purposes, and without the written consent of the patient, except in the following cases:" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "3. The Purpose of preventive and curative measures related to public health, or to maintain the health and safety of the patients or any other persons in contact with them." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "It is not permitted to store, develop, or transfer data and health information outside the country that is related to health services provided within the country" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "(A) Dealing with the information only necessary for the performance of the work or purpose specified." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "(B) Exchange of information with authorized individuals only." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare

## Gap register
- CONSENT_CHAIN_GAP (step 1): Consent for 'treatment' was recorded under DOH; the receiving party is under DHA. Whether the receiving regulator recognises that consent must be checked.

## Patient action plan (en)
**Your records have not been sent yet: your signed consent is needed first**

Sending your medical records from Abu Dhabi to your new hospital in Dubai is paused. All three regulators (Abu Dhabi DOH, Dubai DHA, and federal) allow this transfer for continuing treatment, but only once certain conditions are met. Right now there is no signed written consent from you showing that you agree to share your records with the Dubai hospital. It is also not yet clear which sharing route will be used (a referral, or a health exchange system such as Malaffi or Nabidh). The rules do not yet cover whether a consent you gave in Abu Dhabi automatically counts in Dubai. No data has been released.

1. Sign a written consent that names your new Dubai hospital as the receiver of your records.
2. Tell the hospitals if you want to limit which facilities can see your records.
3. Ask both hospitals which route they will use: a referral or a health information exchange (Malaffi, Nabidh, Riayati).
4. If the Dubai hospital requests your records itself, be ready to give a separate consent for that request.

Once your consent and the sharing route are confirmed, the transfer can go ahead. Only the information needed for your treatment will be shared, and it will stay within the UAE.

_This is a research prototype, not legal or medical advice._
