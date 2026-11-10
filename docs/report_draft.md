# AI for Good Sandbox Hackathon - Team Polaris - SovereignGuard

Team leader: Asna Khan
Team members: Shafi Anwar (solution design and prototype), Asna Khan (team leader, problem definition and validation)
Contact details: shafianwar745@gmail.com | Country of residence: India (both members)
GitHub link: https://github.com/Growinggiant576/Sovereignguard

## 1. Introduction - the problem

A patient's health record in the UAE is protected by more than one regulator: the Dubai Health Authority (DHA) for Dubai facilities, the Department of Health - Abu Dhabi (DoH) for Abu Dhabi facilities, and federal law everywhere. Each has its own rules on consent and sharing.

Records leave a hospital for three common reasons: the patient continues treatment in another emirate, a research partner wants the data to train an AI model, or a provider wants to process it on a server. Each of these crosses from one set of rules into another. Before the record moves, someone must check that the patient's consent covers this exact use, that every regulator involved allows it, and that the data stays in the UAE. None of the 12 public documents we collected says whether consent given under one emirate's rules is valid under another's.

**SovereignGuard is a checkpoint for health records, like passport control for data.** Before a record leaves a hospital, it:
1. asks one AI agent per regulator involved whether the transfer is allowed, quoting the exact clause;
2. holds the record if anything is missing, and merges all missing items into one checklist, the **Care Passport**;
3. tells the patient and the hospitals, in English or Arabic, exactly what to sign or confirm;
4. re-checks when the items are done, and releases the record;
5. logs every silence or disagreement between regulators as evidence for policy makers.

In our runs it held a care transfer until the consents were signed and then released it; it **blocked** a transfer of patient data to a server outside the UAE, citing Article 13 of Federal Law No. 2 of 2019; and for reuse of records to train an AI model, it produced the exact remaining checklist before any data is shared.

Scope: research prototype, simulated scenarios only, no real patient data, not legal advice. The knowledge base contains public documents only (Section 5).

## 2. The solution

For each proposed handoff (sender, receiver, purpose, data categories), the Consent Chain Tracker first compares the handoff with the patient's recorded consent. The Coordinator then asks, independently and in parallel, every regulator agent whose rules may apply: the sender's emirate, the receiver's emirate, and federal law. Each agent searches only its own regulator's documents and must quote the clauses it relies on. The Coordinator compares the answers and applies fixed rules: any BLOCK blocks the step; a consent gap, a condition not yet met, a silence or an unverified quote holds it; otherwise the data is released and the handoff is recorded. The unmet conditions from all regulators become one checklist; once the patient or hospitals provide the evidence (for example a signed consent and the sharing route used), the same check runs again and releases the data. The Patient Navigator then explains the result to the patient, and every disagreement, silence and consent gap is written to the gap register.

### 2.1 Building blocks, their functions, and where they can be reused

| Building block | Type | Function | Hackathon role | Reuse in another context |
|---|---|---|---|---|
| Regulator agent (3 instances: Federal, DHA, DoH) | LLM agent - one class, three instances | Reads only its own regulator's partition of the knowledge base. Returns PERMIT, PERMIT_WITH_CONDITIONS, BLOCK, SILENT or NOT_APPLICABLE, with conditions, open questions and quoted citations | Institutional participant; policy and legal adviser | Point it at another regulator's documents (e.g. two education regulators, or two financial regulators). No code change |
| Consent Chain Tracker | Rule-based, no LLM | Ledger of what the patient consented to, for which purpose, recorded under which regulator. Flags a purpose not covered, consent recorded under another regulator, and transfer outside the UAE | Supporting component | Any consent-based data sharing (student records, banking data). Only the labels change |
| Coordinator | Rule-based, no LLM | Asks the relevant regulator agents independently and in parallel, compares their decisions, applies fail-closed rules (BLOCK / PAUSE / PROCEED), merges unmet conditions into the Care Passport checklist, releases the data only on PROCEED, writes the gap register | Multi-agent coordination | Any process where several authorities must agree on one decision |
| Patient Navigator | LLM agent | Turns the structured results into a short action plan in the patient's language | Innovative AI solution (citizen-facing) | Any citizen-facing explanation of a multi-agency decision |
| Citation verifier | Rule-based, no LLM | Checks that every quoted clause appears in the excerpt it cites. An unmatched quote pauses the step | Auditability | Any retrieval-based assistant that cites sources |

### 2.2 How this differs from a general chatbot

- Each regulator agent can only see its own regulator's documents, so disagreement between regulators becomes visible instead of being blended into one answer.
- The final outcome is decided by fixed, readable rules in code, not by the model.
- Every quote is checked by code against the source text.
- "The rules are silent" is a valid, logged output, not a failure.
- The gap register turns everyday use into evidence for policy makers.

**Technical setup.** Python 3.12 on a laptop (Apple M1 Pro, 16 GB RAM); no special hardware. Knowledge base: ChromaDB vector store with ChromaDB's default local embedding model (all-MiniLM-L6-v2), 12 documents split into 797 passages, partitioned by regulator. Each agent runs several focused searches (the question itself, consent and disclosure terms, and de-identification or cross-border terms when relevant) and reads the 10 closest passages. Language model: Claude Opus 5.5 through the Anthropic API, with output constrained to a JSON schema so every agent answer is machine-checkable. Each run writes a JSON and a readable Markdown trace (retrieved passage IDs, decisions, quotes and whether each quote was verified, model ID, token counts, knowledge-base fingerprint). Step-by-step reproduction instructions are in the GitHub README; traces of every scenario are committed so judges can inspect results without running anything.

## 3. Why it is novel

- **It acts, not only advises.** It holds or releases the data, produces the exact checklist of what is missing, and releases the data once the evidence is in.
- **It checks the handoff, not one regulator's rules.** A question-answering assistant answers "what does DHA say?". SovereignGuard asks every regulator involved in the same handoff and compares the answers.
- **Regulators are kept apart on purpose.** Each agent sees only its own regulator's documents, so a disagreement between emirates shows up as a disagreement instead of being averaged away.
- **Silence is an answer.** When the rules do not address a step, the agent must say so; the step pauses and the silence is logged.
- **Helping the patient produces policy evidence.** The gap register is a by-product of normal use: every pause is a documented example of where rules do not yet connect.
- **Consent is tracked as a chain.** The tracker records under which regulator's framework each consent was given, so reuse under another framework or for another purpose is caught.
- **Trust is enforced in code.** Quotes are machine-checked against the source text, and the final outcome is decided by readable fail-closed rules, not by the model.

## 4. Use case requirements (per pipeline node)

- **SRC:** each handoff must state sender, receiver, their regulators, purpose and data categories; the patient's consent records must state purpose and the framework they were recorded under. Knowledge-base documents must be public and carry source URL and access date.
- **C:** documents must be stored per regulator partition, and every run must record which version of the knowledge base it used (fingerprint).
- **PP:** no identifiable patient data is sent to the model; scenarios carry data categories only. Passages keep the original article numbering so citations stay traceable.
- **M:** each regulator agent must use only its own partition, quote every clause it relies on, and declare silence instead of guessing.
- **P:** outcomes are fail-closed and decided by code; a human reviews every PAUSE and BLOCK; unverified quotes pause the step.
- **D:** results go to the sending facility, the receiving facility, the patient (in their language), and the gap register for regulators.
- **SINK:** the patient receives an action plan; facilities receive the decision with reasons and quotes; regulators receive the gap register.

## 5. Mapping with ITU-T Y.3172, the AI Readiness 2.0 Report, and UAE policies

We map SovereignGuard architecturally to the ITU-T Y.3172 pipeline; we do not claim formal conformance. Y.3172 defines its pipeline for "a machine learning application in a telecommunication network"; applying it to health-data governance is our adaptation. Readiness dimensions use the names in the AI Readiness 2.0 framework data (13 dimensions, 6 factors, 111 metrics).

| Node | SovereignGuard component | AI Readiness 2.0 dimension | UAE documents in the knowledge base |
|---|---|---|---|
| SRC | Patient request, handoff steps, consent records; 12 public regulation texts | 1 Data/Model Marketplace; 4 Contextualization and Regional Impact | NABIDH Policies and Standards V2.0 (DHA); Policy on the Abu Dhabi Health Information Exchange (DoH) |
| C | Ingestion into ChromaDB, one partition per regulator; KB fingerprint per run | 13 Digital Infrastructure | Abu Dhabi Healthcare Information and Cyber Security Standard (ADHICS); DHA Policy for Data and Health Information Protection and Confidentiality |
| PP | Passage splitting with article numbers kept; only data categories, no patient data, reach the model | 10 AI & Policies; 1 Data/Model Marketplace | DHA Standards for Health Information Consent and Access Control; DHA Policy for Health Data and Information Sharing |
| M | Three regulator agents (one class) and the Patient Navigator | 5 Level of Integration of AI in Workflows; 8 Collaboration with AI | DHA Artificial Intelligence in the Healthcare Policy; UAE National Strategy for Artificial Intelligence 2031 |
| P | Fail-closed outcome rules, human review of every pause, citation verifier | 10 AI & Policies; 9 Impacts of Humans in AI Integration | Federal Law No. 2 of 2019 (ICT in Healthcare); DOH Standard on Patient Healthcare Data Privacy |
| D | Routing of results to sender, receiver, patient and gap register | 7 Strategy Alignment; 3 Cross-Domain Correlation Analysis | DHA Policy for Health Data and Information Sharing; Policy on the Abu Dhabi HIE |
| SINK | Patient action plan (English/Arabic), facility decision, gap register | 6 Human Interface; 11 AI for Inclusion | Malaffi Privacy Notice; DHA "My Personal Health Data Preferences" |


## 6. Demo scenarios and error scenarios

All five scenarios were run on 10-11 November 2026 with governance off and on (Claude Opus 5.5, effort medium). Full traces are in the GitHub `runs/` folder. Across the final runs, **122 of 122 quoted clauses were matched to the source text** by the citation verifier.

| Scenario (simulated) | Without governance | With SovereignGuard |
|---|---|---|
| s1: patient moves from an Abu Dhabi (DoH) hospital to a Dubai (DHA) hospital | Record transferred; nobody notices the consent was recorded under DoH rules only | **HOLD.** All three regulators allow it only with conditions; unmet items become the Care Passport: written consent for this disclosure, a separate DHA-compliant consent, and the sharing route (referral or exchange) |
| s4: same handoff after the patient signs and the hospitals confirm a signed-referral route | Record transferred | **RELEASED.** No regulator has an unmet condition; the handoff is recorded in the consent ledger |
| s2: Dubai hospital shares a "de-identified" copy with an AI research partner (step 1), which then processes it on a server outside the UAE (step 2) | Both transfers executed; 3 issues not caught | **Step 1 HOLD:** consent covers treatment only; DHA asks for proof of anonymisation and a data-sharing agreement, federal law for research-ethics approval. **Step 2 BLOCK:** the federal agent cites Article 13 ("It is not permitted to store, develop, or transfer data and health information outside the country...") |
| s5: AI-training reuse after the patient opts in, with ethics approval, a data-sharing agreement and UAE-only processing | Record transferred | **HOLD with 4 exact items:** federal conditions met; DHA still requires proof that anonymisation was verified, that no re-linking key is kept, and two missing clauses in the data-sharing agreement |
| s3: same as s1, patient writes in Arabic | As s1 | Same decisions; the patient's checklist is written in Arabic (not yet checked by a native speaker) |

**Error scenario (where the system itself went wrong):**

1. **Step 1 - deployment.** SovereignGuard holds a care transfer until the consents are signed, then releases it (s1, s4).
2. **Step 2 - a new use appears.** The hospital proposes to share a de-identified copy with an AI research partner, which wants to process it outside the UAE (s2).
3. **Step 3 - the controversy.** In our first run, both the DHA and federal agents declared **SILENT** on the cross-border step. Our own check showed a **retrieval miss, not a real silence**: the search had been pulled towards AI-strategy text by the words "AI model" and missed the binding rule. Because outcomes are fail-closed, the data was still **held**, not released. The first run's trace is kept in the repository history.
4. **Corrective action.** Each agent now runs focused legal-term searches alongside the question. After re-running every scenario, the federal agent finds Article 13 and **blocks** the transfer. Remaining safeguard: a human confirms every SILENT before it is published as a policy gap.

**Judges' added scenario (anticipated): the patient withdraws consent after a release.** DHA's consent standard says the patient "must be given the right to withdraw and opt-out". The ledger already records every executed handoff, so each downstream recipient can be identified; automatic notification is a next step, not yet built.

## 7. Policy gaps and standards gaps

### 7.1 Standards gaps in ITU-T Y.3172 (team analysis of the Recommendation text)

We searched the full text of Y.3172 (06/2019). It contains no construct for legal or regulatory applicability, consent, data provenance, audit logs, human approval, or multiple jurisdictions or administrative domains; the words "legal", "law", "regulat" and "jurisdiction" do not appear. The policy node is defined as "This node enables the application of policies to the output of the model node", with a network operator's rules as the example. Privacy appears only as preventing "unauthorized access to, and data leaking from, an ML pipeline" (clause 9).

| Gap | Effect in a multi-regulator setting | Extension we propose |
|---|---|---|
| One policy source per P node | Which authority's rules apply is itself a decision; conflicting authorities cannot be represented | P node holding several policy sets, each labelled with its authority, plus an explicit conflict rule |
| No consent or provenance metadata | Purpose and consent cannot travel with the data from SRC to SINK | Consent and provenance metadata carried with the data through every node |
| No audit requirement | Decisions cannot be reconstructed afterwards | An audit record per node (inputs, sources used, decision) |
| No human approval node | Human review is outside the architecture (nearest concept: the ML sandbox) | An explicit human decision gate between P and D |

### 7.2 Policy gaps

**Reported by the agents (from the runs):**
- In s1 and s3, every regulator agent asked for consent that meets its own framework; none of them could treat the consent recorded under the other emirate's rules as sufficient.
- In s2 step 2, the federal agent blocked the offshore transfer, while the DHA agent found its own policy only points to a separate Ministerial Decision (No. 51 of 2021) that sets the exemptions: two regulators, two different answers to the same handoff.
- In s5, the same AI-training handoff satisfied federal law but not DHA, which asks for extra evidence on anonymisation and the data-sharing agreement: the evidence required depends on which regulator is asked.

**Confirmed by our analysis of the knowledge-base text (domain-level, with a global example):**

| Gap | Evidence in the 12 documents | Global example |
|---|---|---|
| No rule for recognising consent across emirate frameworks | DHA: "Consent should be as per DHA requirements"; DoH and federal law require written consent. Our text search found no provision on recognising a consent recorded under another emirate's framework | The EU European Health Data Space Regulation (in force 26 March 2025) sets one framework for sharing health data "across borders for the healthcare delivery" |
| Different wording for "de-identified" | DHA defines anonymisation ("does not identify an individual; and cannot be practically used to determine their identity"); federal Article 16 allows research "provided that the patient's identity is not disclosed"; the Malaffi notice says "de-identified data only". No shared definition across the three | EHDS: secondary use only "based on a permit issued by a health data access body" |
| AI model training is not named as a purpose | No binding text in the knowledge base addresses training AI models on patient data; the AI Strategy 2031 notes "Machine learning models need access to training data sets" | EHDS: people may "opt out in a simple and reversible manner" from secondary use |

**Where the rules agree (not a gap):** transfer outside the UAE is prohibited by federal law (Article 13), DHA (4.15.1) and DoH (4.1.4), except under exemptions. The exemption instrument cited by DHA (Ministerial Decision No. 51 of 2021) is not in our knowledge base.

Limitations: for a simple care transfer the patient may also carry a copy of the record (DHA policy 4.6.4), so the strongest need is for flows the patient never sees. The English text of Federal Decree-Law No. 45 of 2021 and Cabinet Resolution No. 32 of 2020 could not be obtained, so the federal partition is thin; regulator agents' interpretations have not been reviewed by a lawyer.

## 8. Next steps

1. Have UAE health-data legal experts review the regulator agents' outputs and the gap register.
2. Add the missing federal texts (Decree-Law No. 45 of 2021, Cabinet Resolution No. 32 of 2020) and official Arabic versions.
3. Add an offline local-model option so the prototype runs without an API key.
4. Test reuse in a second domain by swapping in another pair of regulators' documents.
5. Write up the Y.3172 extensions in Section 7.1 as a proposal for discussion with ITU-T experts, and the gap register method as a paper.
