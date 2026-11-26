# WI-GOV-CHARTER-SOURCE-LINEAGE-CLARIFICATION-001
## Proponent-confirmed lineage of the Eternal Wisdom Charter

- **Document ID:** WI-GOV-CHARTER-SOURCE-LINEAGE-CLARIFICATION-001
- **Version:** 0.1
- **Status:** REVIEW — PROVENANCE CLARIFICATION
- **Date:** 2026-11-26
- **Repository:** Wisdom-Intercessor/WisdomPact
- **Related audit:** WI-GOV-CHARTER-BASELINE-EVIDENCE-AUDIT-001

## 1. Proponent clarification

Following the merge of PR #25, the Charter's proponent clarified the intended document lineage:

1. **Original mother Charter / initial source:** the file titled `Eternal Wisdom Charter(Wisdom Pact).pdf`, currently located at `charter/Eternal Wisdom Charter(Wisdom Pact).pdf`.
2. **Operational and executable mother-Charter edition:** the Persian and English Version 1.0 (2026) text/documents previously inventoried in the repository.
3. The Version 1.0 operational edition is therefore not to be treated as the initial origin of the Charter. It is the structured and operationalized edition derived from the earlier mother Charter.

This lineage is recorded as an explicit proponent statement, not as an independently completed textual equivalence finding.

## 2. Source identifiers currently available

### 2.1 Original mother Charter PDF

- **Path:** `charter/Eternal Wisdom Charter(Wisdom Pact).pdf`
- **Git blob object ID:** `ff642d285c7af078dc2c91f5b1575ae4172ede3d`
- **Repository display URL:** https://github.com/Wisdom-Intercessor/WisdomPact/blob/main/charter/Eternal%20Wisdom%20Charter(Wisdom%20Pact).pdf
- **Repository-reported size:** 9,728,861 bytes

The Git blob object ID is a Git object identifier, not a SHA-256 checksum of the PDF file.

### 2.2 Operational Version 1.0 edition

The repository inventory records the following paired artifacts:

- Persian DOCX: `charter/fa/Eternal_Wisdom_Global_Charter_FA.docx` — Git blob object ID `442cc09a0555e18e21f8cb2675d81830a7c59e1f`.
- English DOCX: `charter/en/Eternal_Wisdom_Global_Charter_EN.docx` — Git blob object ID `b079780ddd402f82ccb0cf74569b683243508b86`.
- Persian PDF: `charter/fa/Eternal_Wisdom_Global_Charter_Wisdom_Pact_FA'.pdf` — Git blob object ID `f215d8443117b20ccdcefb872f2f4df2d56f8843`.
- English PDF: `charter/en/Eternal_Wisdom_Global_Charter_Wisdom_Pact_EN'.pdf` — Git blob object ID `8f796b09b7cfbf3ee3941a43470702471eaac808`.

The corresponding files under `charter/releases/` have the same Git blob object IDs as the language-folder files. They are duplicate paths to the same Git blob content, not distinct content versions.

The retrieved Persian Markdown identifies itself as a rewritten, structured, operational version 1.0 (2026). The retrieved English Markdown contains the English edition. The complete source-to-derived comparison remains outstanding.

## 3. Corrected interpretation of the prior audit

The finding in WI-GOV-CHARTER-BASELINE-EVIDENCE-AUDIT-001 that no ratification baseline was designated remains valid as to **internal ratification**. It must not be interpreted as denying the source lineage now clarified by the proponent.

The working document hierarchy for subsequent verification is:

`Original Mother Charter PDF`
→ `Operational and Executable Version 1.0 (Persian and English)`
→ `Verified controlled Markdown / release representations`
→ `Separate internal adoption and external voluntary-adoption records`

This hierarchy is a provenance and document-development model. It does not by itself prove that the two editions are textually equivalent, establish an internal ratification, or create legal force.

## 4. Verification work still required

- [ ] Obtain a readable extraction of the original mother Charter PDF and preserve its page structure.
- [ ] Record its visible title, date/version (if present), authorship/presenter information, section structure, and any document-control metadata exactly as printed.
- [ ] Compare the original mother Charter against operational Version 1.0, identifying additions, omissions, reorganizations, clarifications, and substantive changes.
- [ ] Compare the Persian and English operational editions clause by clause.
- [ ] Verify each PDF and DOCX rendering against its corresponding controlled text.
- [ ] Produce SHA-256 checksums for the exact original PDF and the selected operational release files; retain Git blob IDs separately.
- [ ] Obtain the proponent's confirmation of the completed comparison and exact candidate release pair.
- [ ] Only after those checks, designate the controlled source baseline for an internal adoption proposal.
- [ ] Keep internal ratification evidence and external voluntary adoption records separate from source and version verification.

## 5. Access limitation recorded

The GitHub connector returned the original PDF's repository metadata and Git blob object ID, but did not provide readable PDF text through the text-only file retrieval interface. Therefore this clarification does not paraphrase, reconstruct, or infer the original PDF's contents. Its binary content must be inspected through a supported PDF/file-reading route before a substantive comparison is claimed.

## 6. Governance and publication safeguards

This clarification:
- does not modify either Charter text;
- does not rename, move, or delete legacy files;
- does not declare Version 1.0 ratified or legally binding;
- does not establish the competence of an internal approving body;
- does not publish the Charter to the website;
- does not activate any governance, identity, financial, wallet, or external-service functionality.

**Provenance status:** Proponent-confirmed lineage; source-to-derived comparison pending.  
**Internal ratification status:** Not established by this document.  
**External voluntary adoption status:** Not established by this document.
