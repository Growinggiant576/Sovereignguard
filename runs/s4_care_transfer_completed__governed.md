# Continuing treatment, after the Care Passport checklist is completed - governed run

- Scenario: `s4_care_transfer_completed` (simulated, no real patient data)
- Run at: 2026-11-10T19:11:37+00:00 | model: claude-opus-5-5 | effort: medium | KB fingerprint: 48837ef86e4ad24e
- Patient request (en): I have signed the consent forms both hospitals gave me. Please send my records to my new hospital in Dubai so my treatment can continue.

## Step 1: Release treatment record to the Dubai hospital
Origin hospital (DoH-licensed, Abu Dhabi) (DOH) -> Receiving hospital (DHA-licensed, Dubai) (DHA), purpose: `treatment`

**Outcome: PROCEED** | data released: True


Consent tracker findings:
- none

### Department of Health - Abu Dhabi (DoH): PERMIT_WITH_CONDITIONS
Under the DoH excerpts, a DoH-licensed facility may disclose identifiable health records to another licensed facility if the patient has given written consent. The receiver must also keep the data confidential, use it only for health purposes, and keep it inside the UAE. The patient's signed written consent at the origin hospital (c2) meets the consent requirement. Dubai is inside the UAE, so the prohibition on transfers outside the UAE is not triggered. The receiver's commitments cover the ongoing duties. Based on the evidence provided, no DoH requirement appears unmet. The excerpts do not specifically address direct inter-emirate sharing by referral outside the Malaffi/ADHIE platform; see open questions. This assessment is for human review and is not legal advice.

Applies because: The disclosing entity is a DoH-licensed hospital in Abu Dhabi holding PHI about health services provided within Abu Dhabi. The DoH Standard on Patient Healthcare Data Privacy governs anyone who exchanges and circulates such patient information.

Conditions:
- The receiving hospital must keep the record confidential (committed in the evidence).
- The record may be used only for health purposes, here continuing treatment (committed in the evidence).
- The PHI must not be stored or transferred outside the UAE (committed in the evidence: stored only inside the UAE).
- The disclosure must stay within the scope of the patient's written consent c2, including any selective-disclosure choices the patient made.
- Access must follow 'need to know' and 'least privilege' principles at both entities.

Open questions:
- The DoH excerpts discuss facility-to-facility sharing mainly through the ADHIE/Malaffi platform. They do not expressly address a direct, referral-based disclosure to an out-of-emirate (DHA-licensed) facility outside that platform.
- Does consent c2 specifically name the Dubai receiving hospital and cover all three categories (clinical record, lab results, imaging), consistent with the patient's selective-disclosure right?
- Consent c3, signed at the Dubai hospital, is outside DoH's authority. Its sufficiency is a matter for the DHA assessor.

Citations (9/9 matched to source text):
- [doh_patient_data_privacy_std::0009] (verified) "Must not use it without the written consent of the patient, except in the following cases." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "All entities who are interacting with the patient health data lifecycle should take the
patient’s consent." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "Must ensure its confidentiality." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "Must not use it for non-health purposes." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "No entity is permitted to store, develop, or transfer PHI outside the United Arab
Emirates that is related to health services provided within Abu Dhabi" - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0016] (verified) "Patients shall have the authority for selective disclosure of their health information
to entities (e.g. hospitals, health care providers etc.) as deemed necessary." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0016] (verified) "Entities shall adopt the principles of ‘need to know’ and ‘least privilege’." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0012] (verified) "Provision of health information regarding activities and healthcare services,
referrals, or administrative services." - DOH Standard on Patient Healthcare Data Privacy
- [doh_malaffi_privacy_notice::0006] (verified) "for the purpose of enabling such other Healthcare Facilities in the Emirate of Abu Dhabi and elsewhere (including the relevant Healthcare Professionals and other authorised users of such Healthcare Facilities) to provide you with clinical care." - Privacy Notice

### Dubai Health Authority (DHA): PERMIT_WITH_CONDITIONS
Under the DHA excerpts, a DHA-licensed facility may receive an identifiable medical record from another UAE entity for continuing care when the referral route has clear signed patient consent. Where the receiving entity requests the record, separate patient consent is also required. The evidence shows a signed referral, the patient's consent at the origin (c2) and a separate consent at the Dubai hospital (c3), so no DHA prerequisite appears unmet. Remaining duties are to share only what direct care needs, use a secure transmission channel, and ensure the consents meet DHA's Consent & Access Control requirements. This is an assessment for human review, not legal advice.

Applies because: DHA policies apply to healthcare entities under DHA jurisdiction. The receiving Dubai hospital is DHA-licensed, and the data (medical records, lab reports, imaging) falls within DHA's definition of health information. DHA's rules govern the receiving side; the Abu Dhabi sender's disclosure is primarily a matter for DoH.

Conditions:
- Share and access only the PHI relevant to the patient's direct care (continuing treatment).
- If the record is sent by email, it must be appropriately encrypted or sent via an authenticated portal link, using official Entity email accounts.
- Patient consents (c2/c3) should conform to DHA Consent & Access Control requirements.
- Receiving hospital to keep the record confidential and use it only for continuing treatment, as committed in the evidence.

Open questions:
- The transmission channel is not stated (email, HIE such as Nabidh/Malaffi, physical copy); DHA channel-specific rules may apply.
- Do consents c2 and c3 meet the specific form and content requirements of the DHA Consent & Access Control Policy? Those details are not in the excerpts.
- The excerpts do not state how far DHA rules govern the Abu Dhabi (DoH-licensed) sender's disclosure; that is likely a DoH matter.

Citations (8/8 matched to source text):
- [dha_health_info_sharing_policy::0001] (verified) "Applicability: All Healthcare Entities under the Jurisdiction of Dubai Health Authority" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0016] (verified) "3.2.4. X-ray and imaging reports, output and images." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0021] (verified) "Where a Patient’s care/treatment is transferred to another Entity, a copy of the medical record may be transferred directly with the Data Subject/Patient or via a request from the other Entity (separate Patient consent is required in this case)." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0021] (verified) "with clear signed" - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0023] (verified) "All relevant PHI should be accessed and shared as per necessities of direct care to" - Standards for Health Information Consent and Access Control
- [dha_health_info_sharing_policy::0038] (verified) "Health data and information should only be disclosed when the consent of the Data" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0017] (verified) "Consent should be as per DHA requirements (Consent & Access Control Policy)." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0029] (verified) "Protected Health Information should only be sent via email if it is appropriately" - Policy for Health Data and Information Sharing

### UAE federal law and federal health policy (incl. MOHAP): PERMIT_WITH_CONDITIONS
Under Federal Law No. 2 of 2019, a person exchanging patient information must keep it confidential, use it only for health purposes, and have the patient's written consent unless a listed exception applies. Health data about services provided in the UAE must not be stored or transferred outside the country without a decree. The evidence shows written patient consent (c2, plus c3 at the receiving hospital), a treatment-only purpose, a confidentiality commitment, and storage only inside the UAE. On these excerpts the Abu Dhabi to Dubai handoff for continuing treatment is permissible, subject to the ongoing duties below. No unmet condition is shown. Some procedural rules (central-system authorization, executive and ministerial decrees) are referenced but not provided. This is an assessment for human review, not legal advice.

Applies because: Federal Law No. 2 of 2019 applies to all methods and uses of ICT in the health fields across the UAE, including free zones. Its definition of 'Exchange of Health information' covers transfer and disclosure of health data. Both hospitals are in the UAE, so a handoff between them is within scope if it is done electronically or through ICT.

Conditions:
- Both hospitals must keep the patient information confidential (Art. 16).
- The record must be used only for health purposes, here the patient's continuing treatment, and not for non-health purposes (Art. 16).
- The disclosure must rest on the patient's written consent; consent c2 has been provided (Art. 16).
- The data must not be stored, developed or transferred outside the UAE unless a decree is issued; both hospitals have committed to UAE-only storage (Art. 13).
- If the federal central system is used, only individuals authorized by the health authority may use it. They may handle only the information necessary for the specified purpose and exchange it only with authorized individuals (Arts. 14-15).
- Both entities must take all necessary measures to protect the data and keep it confidential (Art. 8, if they are central-system users).

Open questions:
- Was the record exchanged through ICT or electronic means? The law applies to ICT uses in health fields, and the excerpts do not say how a paper-only transfer would be treated.
- Was the federal central system used? If so, were the individuals involved authorized under Article 14? The evidence does not say.
- The Executive Decree (Arts. 8, 15) and the Ministerial Decree on storage conditions (Art. 12) are referenced but not in the excerpts, so any additional procedural requirements cannot be checked.
- Article 16 is 'without prejudice to any applicable legislation'. Emirate-level DoH and DHA rules may impose further requirements; they are outside this federal assessment.

Citations (8/8 matched to source text):
- [fed_law_2_2019::0006] (verified) "This law applies to all methods and uses of ICTs in the health fields in the country, including free zones." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0006] (verified) "Exchange of Health information: access, exchange, copying, photocopying, transfer, storage, publication, disclosure or transmission of health data and information." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "anyone who exchanges and circulates patient information must ensure its confidentiality and not use it for non-health purposes, and without the written consent of the patient" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "It is not permitted to store, develop, or transfer data and health information outside the country that is related to health services provided within the country" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "No individual may use the central system unless he is authorized to do so by the health authority or the concerned authority" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "(A) Dealing with the information only necessary for the performance of the work or purpose specified." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0008] (verified) "(B) Confirm all necessary measures to ensure the protection and safety of health data and information and its confidentiality." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0009] (verified) "A Ministerial Decree in coordination with the health authorities shall determine the conditions and controls for storage of health data and information within the country." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare

## Gap register
- none

## Patient action plan (en)
**Your treatment record can be sent to your new hospital in Dubai**

Good news: the transfer of your treatment record to the Dubai hospital was allowed to go ahead, and the record has been released. All three regulators checked (Abu Dhabi DoH, Dubai DHA and the federal rules) said yes, with conditions. Your signed consent forms at both hospitals met their requirements. Nothing is missing. The conditions are mainly duties for the hospitals: keep your record confidential, use it only for your continuing treatment, share only what your care needs, send it securely, and keep it stored inside the UAE. One note: the rules provided do not yet clearly cover direct sharing between emirates outside the Malaffi/ADHIE platform, and some federal procedural rules were referenced but not provided.

1. Nothing more is required from you right now.
2. If you limited what could be shared on your consent forms, check with your new hospital that only those parts were sent.
3. Ask your Dubai hospital to confirm they have received your record before your next appointment.

Your Dubai hospital receives your record and uses it only to continue your treatment, keeping it confidential and inside the UAE.

_SovereignGuard is a research prototype; this is not legal or medical advice._
