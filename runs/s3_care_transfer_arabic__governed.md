# Continuing treatment (Arabic-speaking patient) - governed run

- Scenario: `s3_care_transfer_arabic` (simulated, no real patient data)
- Run at: 2026-11-10T19:11:44+00:00 | model: claude-opus-5-5 | effort: medium | KB fingerprint: 48837ef86e4ad24e
- Patient request (ar): أتلقى العلاج في مستشفى في أبوظبي وسأنتقل إلى دبي. أرجو إرسال ملفي الطبي إلى مستشفاي الجديد في دبي حتى يستمر علاجي.

## Step 1: Release treatment record to the Dubai hospital
Origin hospital (DoH-licensed, Abu Dhabi) (DOH) -> Receiving hospital (DHA-licensed, Dubai) (DHA), purpose: `treatment`

**Outcome: PAUSE** | data released: False

- DOH: 2 condition(s) still to be met
- DHA: 2 condition(s) still to be met
- FEDERAL: 4 condition(s) still to be met

Consent tracker findings:
- CROSS_JURISDICTION_CONSENT (MEDIUM): Consent for 'treatment' was recorded under DOH; the receiving party is under DHA. Whether the receiving regulator recognises that consent must be checked.

### Department of Health - Abu Dhabi (DoH): PERMIT_WITH_CONDITIONS
DoH rules allow an Abu Dhabi facility to share identifiable health records for a health purpose such as continuing treatment, provided the patient has given written consent (or a listed exception, such as exchange via Malaffi, applies). The sharing must stay confidential, be used only for health purposes, and respect the patient's selective-disclosure choices. Dubai is inside the UAE, so the DoH ban on transfers outside the UAE is not triggered. The evidence does not show a written patient consent covering disclosure to this Dubai hospital.

Applies because: The sender is a DoH-licensed facility in Abu Dhabi disclosing protected health information about services delivered in Abu Dhabi. DoH data-privacy rules govern anyone who exchanges and circulates that patient information.

Conditions:
- Obtain the patient's written consent for this disclosure, unless a listed exception applies (for example, exchange between facilities on the Malaffi/ADHIE platform).
- Keep the shared records confidential.
- Use the records only for health purposes, here continuing treatment.
- Honour any selective-disclosure instruction the patient has given about which facilities may receive the data.
- Apply need-to-know and least-privilege access to the shared records.
- Keep the data within the UAE; any onward transfer outside the UAE needs a DoH exception.

Still to be met before release (Care Passport items):
- No written patient consent covering disclosure to the DHA-licensed Dubai hospital is shown. The tracker notes only a 'treatment' consent recorded under DOH, and its form and scope are unverified.
- No evidence shows that the sharing route is the Malaffi/ADHIE exchange, which is the alternative exception basis.

Open questions:
- Is the recorded DOH 'treatment' consent written, and does it cover disclosure to facilities outside Abu Dhabi such as this Dubai hospital?
- Does the Dubai hospital participate in, or receive data through, the ADHIE/Malaffi? The Malaffi notice mentions enabling care by facilities 'elsewhere', but the scope is unclear.
- Has the patient made any selective-disclosure instruction that excludes this recipient?
- Whether the DHA recognises the DOH-recorded consent is outside DoH's rules and must be checked by the DHA assessor.

Citations (9/9 matched to source text):
- [doh_patient_data_privacy_std::0009] (verified) "Must not use it without the written consent of the patient, except in the following cases." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "All entities who are interacting with the patient health data lifecycle should take the patient’s consent." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "Must ensure its confidentiality." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "Must not use it for non-health purposes." - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0009] (verified) "No entity is permitted to store, develop, or transfer PHI outside the United Arab Emirates that is related to health services provided within Abu Dhabi" - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0012] (verified) "Health information exchange between healthcare facilities on Abu Dhabi" - DOH Standard on Patient Healthcare Data Privacy
- [doh_malaffi_privacy_notice::0006] (verified) "in the Emirate of Abu Dhabi and elsewhere" - Privacy Notice
- [doh_patient_data_privacy_std::0016] (verified) "Patients shall have the authority for selective disclosure of their health information" - DOH Standard on Patient Healthcare Data Privacy
- [doh_patient_data_privacy_std::0016] (verified) "Entities shall adopt the principles of ‘need to know’ and ‘least privilege’." - DOH Standard on Patient Healthcare Data Privacy

### Dubai Health Authority (DHA): PERMIT_WITH_CONDITIONS
DHA rules allow identifiable records to move between licensed entities in different organisations in the UAE for continuing care, but only with patient consent. Three routes are listed: a referral with clear signed consent, an HIE exchange (Nabidh, Malaffi, Riayati) with patient consent, or the patient carrying their own records. Where the receiving entity requests the record, separate patient consent is required. No evidence shows that a consent meeting DHA requirements exists, or which route was used. The tracker notes that the only consent on file was recorded under DOH, and the DHA excerpts do not say whether DHA recognises it. This is an assessment for human review, not legal advice.

Applies because: The receiving hospital is DHA-licensed in Dubai. DHA policy covers all entities under DHA jurisdiction and all users of health data in Dubai's healthcare sector. The data (clinical records, lab results and imaging) falls within DHA's definition of health information.

Conditions:
- Obtain patient consent for the transfer between these two separate organisations, in a form that meets DHA consent requirements.
- If the referral route is used, the consent must be clear and signed.
- If the transfer happens at the Dubai hospital's request, separate patient consent is required.
- Use a recognised route: referral with signed consent, HIE exchange (Nabidh/Malaffi/Riayati) with patient consent, or the patient transferring their own records.
- Share only the PHI relevant to the patient's direct care needs.
- If email is used, it must be appropriately encrypted and sent from official entity accounts.

Still to be met before release (Care Passport items):
- No evidence of patient consent that meets DHA requirements for this transfer; the only consent noted was recorded under DOH.
- The sharing route used (referral, HIE exchange, or patient-carried) is not shown.

Open questions:
- Does DHA recognise a treatment consent recorded under DOH, or is a separate DHA-compliant consent needed?
- Do DHA rules bind the Abu Dhabi sender, or only the Dubai receiver?
- Was the transfer initiated at the Dubai hospital's request, which would trigger the separate-consent requirement?
- How does the general statement that consent is needed for sharing beyond direct care (4.3.1) fit with the table requiring consent for care transfers between UAE entities?

Citations (9/9 matched to source text):
- [dha_health_info_sharing_policy::0021] (verified) "request from the other Entity (separate Patient consent is required in this case)." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0021] (verified) "Between Entities (not within the same Patient transferring" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0021] (verified) "with clear signed" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0021] (verified) "Riayati) with" - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0017] (verified) "4.3.2. Consent should be as per DHA requirements (Consent & Access Control Policy)." - Policy for Health Data and Information Sharing
- [dha_consent_access_control_std::0023] (verified) "All relevant PHI should be accessed and shared as per necessities of direct care to" - Standards for Health Information Consent and Access Control
- [dha_health_data_protection_policy::0011] (verified) "3.1. All Entities working under jurisdiction of DHA." - Policy for Data and Health Information Protection and Confidentiality
- [dha_health_info_sharing_policy::0016] (verified) "3.2.4. X-ray and imaging reports, output and images." - Policy for Health Data and Information Sharing
- [dha_health_info_sharing_policy::0029] (verified) "4.10.1. Protected Health Information should only be sent via email if it is appropriately" - Policy for Health Data and Information Sharing

### UAE federal law and federal health policy (incl. MOHAP): PERMIT_WITH_CONDITIONS
Under Federal Law No. 2 of 2019, a domestic exchange of identifiable health records between licensed facilities for continuing treatment appears permissible on conditions. The sender and receiver must keep the data confidential and use it only for health purposes. The exchange needs the patient's written consent, or a documented reliance on a statutory exception. Exception 3 (maintaining the health and safety of the patient) may cover it, but the excerpts do not confirm this for routine continuing care. The data stays within the UAE, so the Article 13 bar on transfers outside the country is not triggered. The evidence does not show federal-compliant written consent: the tracker notes only a 'treatment' consent recorded under DOH. This is an assessment for human review, not legal advice.

Applies because: Federal Law No. 2 of 2019 applies to all uses of ICT in the health fields across the UAE. 'Exchange of Health information' is defined to include transfer and disclosure, so an electronic release of records from an Abu Dhabi facility to a Dubai facility falls within its scope.

Conditions:
- Obtain the patient's written consent for the exchange, or document reliance on an Article 16 exception, such as maintaining the health and safety of the patient.
- Both the origin and receiving hospitals must keep the patient information confidential.
- The receiving hospital must use the data for health purposes only, not for non-health purposes.
- Share only the information necessary for the specified treatment purpose.
- Exchange the information only with authorized individuals.
- Keep the data within the UAE; do not store or transfer it outside the country without a decree from the health authority in coordination with the Ministry.
- Take all necessary measures to protect the safety and confidentiality of the data during and after the transfer.

Still to be met before release (Care Passport items):
- The evidence does not show written consent from the patient that satisfies Article 16. The tracker shows only a 'treatment' consent recorded under DOH, and its form (written or not) and scope are not established.
- No documented reliance on an Article 16 exception is shown as an alternative to written consent.
- There is no evidence that the receiving hospital has committed to confidentiality and health-purpose-only use.
- There is no evidence that the exchange is limited to authorized individuals and to the minimum necessary data.

Open questions:
- Does the consent recorded under DOH meet the federal 'written consent' requirement in Article 16, and does it extend to disclosure to a DHA-licensed facility?
- Does exception 3 ('to maintain the health and safety of the patients') cover routine continuing-care transfers without written consent? The excerpts do not settle this.
- Will the transfer go through the federal central system? If so, the Article 14/15 authorization requirements apply, and the Executive Decree conditions are not in the excerpts.
- What Ministry mechanisms and procedures for exchanging health data (Article 10(5)) and Executive Decree controls apply? These are not in the excerpts.
- The emirate-level rules of DOH and DHA on consent recognition are outside this federal assessment.

Citations (8/8 matched to source text):
- [fed_law_2_2019::0006] (verified) "This law applies to all methods and uses of ICTs in the health fields in the country, including free zones." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0006] (verified) "Exchange of Health information: access, exchange, copying, photocopying, transfer, storage, publication, disclosure or transmission of health data and information." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "anyone who exchanges and circulates patient information must ensure its confidentiality and not use it for non-health purposes, and without the written consent of the patient, except in the following cases:" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0011] (verified) "The Purpose of preventive and curative measures related to public health, or to maintain the health and safety of the patients or any other persons in contact with them." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "It is not permitted to store, develop, or transfer data and health information outside the country that is related to health services provided within the country" - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "(A) Dealing with the information only necessary for the performance of the work or purpose specified." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0010] (verified) "(B) Exchange of information with authorized individuals only." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare
- [fed_law_2_2019::0008] (verified) "(B) Confirm all necessary measures to ensure the protection and safety of health data and information and its confidentiality." - Federal Law No. (2) For the year 2019 On the Use of Information and Communications Technology (ICT) in Healthcare

## Gap register
- CONSENT_CHAIN_GAP (step 1): Consent for 'treatment' was recorded under DOH; the receiving party is under DHA. Whether the receiving regulator recognises that consent must be checked.

## Patient action plan (ar)
**نقل ملفك الطبي إلى مستشفى دبي متوقف مؤقتاً، ولم يُرسل أي شيء بعد**

الجهات الثلاث (دائرة الصحة في أبوظبي، وهيئة الصحة في دبي، والقانون الاتحادي) تسمح بنقل ملفك لمواصلة علاجك داخل الإمارات، لكن بشروط لم تكتمل بعد. السبب الرئيسي: لا توجد موافقة مكتوبة منك تشمل إرسال الملف إلى مستشفى دبي، ولم يُحدَّد طريق الإرسال. الموافقة المسجلة حالياً هي موافقة «علاج» لدى دائرة الصحة في أبوظبي، وشكلها ونطاقها غير مؤكدين. القواعد المتاحة لا تقول بعد هل تقبل هيئة الصحة في دبي هذه الموافقة.

1. وقّع موافقة مكتوبة وواضحة تسمح تحديداً بإرسال ملفك إلى مستشفاك الجديد في دبي، وبصيغة تقبلها هيئة الصحة في دبي.
2. إذا طلب مستشفى دبي ملفك بنفسه، فستحتاج إلى تقديم موافقة منفصلة.
3. اسأل المستشفيين عن طريق الإرسال: تحويل طبي بموافقة موقّعة، أو منصة تبادل معتمدة (ملفي، نابض، رياتي)، أو أن تحمل ملفك بنفسك.
4. أخبر المستشفى إذا كانت لديك رغبة في تحديد الجهات التي يحق لها استلام بياناتك.

بعد توفر موافقتك وتحديد طريق الإرسال، يجب أن يلتزم المستشفيان بالسرية، وباستخدام البيانات لأغراض صحية فقط، وبمشاركة ما يلزم لعلاجك فقط مع أشخاص مخوّلين، مع بقاء البيانات داخل الإمارات. بعدها يمكن مراجعة الطلب من جديد.

_هذا نموذج بحثي تجريبي، وليس استشارة قانونية أو طبية._
