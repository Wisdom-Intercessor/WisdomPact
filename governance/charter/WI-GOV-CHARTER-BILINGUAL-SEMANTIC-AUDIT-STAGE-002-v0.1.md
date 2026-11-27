# Bilingual Charter Semantic and Structure Audit — Stage 002

**Status:** Review evidence only; not a certification of complete bilingual equivalence.  
**Sources:** `charter/CHARTER.md` (Persian operational edition V1.0, 2026) and `charter/CHARTER-EN.md` (English edition, V1.0, 2026).  
**Scope:** Parts V–VIII, with focused cross-checks of Parts VI–VII and the addenda.  
**Method:** Compare section order, named entities, article/protocol sequence, and representative substantive passages in repository Markdown renderings. This is not a legal review and does not establish ratification.

## 1. Confirmed structural alignment

- Part V contains ten thematic protocols in both editions, in the same order: women's rights and gender justice; children's rights; minorities; democracy/rule of law/freedom of expression; economic justice/labor rights; peace/disarmament/security; refugees/migrants/climate displacement; worldwide health/pandemics; cybersecurity/privacy/data sovereignty; bioethics/emerging technologies.
- The five institutions in Part VI correspond in both editions: World Wisdom Assembly, Wisdom Council, Wisdom Court, World Wisdom Network, and World Wisdom Fund.
- Part VII uses the same monitoring domains and the same reporting, accountability, and dispute-resolution categories in both editions.
- Part VIII has ten addenda in both editions. Persian lettering (الف، ب، ج، د، هـ، و، ح، ط، ی، ک) should not be mechanically normalized to Latin letters; the English edition labels the latter four G–J.
- Parts IX–XIII retain corresponding section order in the English contents and closing sections. Full line-by-line semantic verification remains pending.

## 2. Issues requiring correction or source-file verification

### 2.1 Repeated list numbering in the English Markdown rendering
In Part VI, the English rendering shows every institution function as a list item numbered `1.`, whereas the Persian source uses bullets. In Part VII, Reporting, Accountability, and Dispute Resolution likewise show repeated `1.` markers in English where the Persian source uses distinct bullet items. This may be a Markdown/PDF extraction or list-style conversion artifact; verify against the English DOCX/PDF before changing the source document.

**Classification:** Formatting/rendering defect or extraction artifact; not yet a substantive translation discrepancy.

### 2.2 Digital-domain string in Persian Addendum K
The Persian Markdown rendering contains the literal sequence `com.wisdomintercessor` in Addendum K, while the English rendering gives `wisdomintercessor.com`. Because domain names are direction-sensitive strings and must remain exact, inspect the Persian DOCX/PDF source to determine whether this is merely right-to-left display/extraction reversal or an actual source-text typo. Do not silently normalize it based on visual appearance alone.

**Classification:** High-priority exact-string verification; possible RTL extraction artifact.

### 2.3 Scope and terminology of institutional authority
The institution names and broad functions correspond structurally. This stage does not establish that terms such as “judgments,” “ethically binding,” “Assembly,” “Court,” or “World” carry identical legal or institutional implications across both language versions. These terms need a dedicated terminology and authority-boundary review before any claim of full semantic equivalence.

**Classification:** Semantic/legal terminology review pending.

## 3. Substantive spot-checks

- The ten Part V protocol titles and their five-article sequence are aligned in the inspected text. The English rendering of Protocol 10 includes the same main topics visible in Persian: genome intervention, cloning, AGI and converging technologies; end-of-life issues; abortion regulation; human experimentation; and lethal autonomous weapons.
- Addenda A–E express corresponding positions on non-automatic legal bindingness, complementarity with existing international instruments, the operational definition of wisdom, four levels of realization, and periodic review.
- Addenda F–J correspond in sequence to institution-building, worldwide participation, ideological independence, evolution/openness, and digital infrastructure.
- The English Addendum J explicitly uses `wisdomintercessor.com`; the Persian Addendum K requires the exact-string verification described above.

These spot-checks support structural and thematic correspondence only. They do not prove that every sentence, qualification, modality, or legal nuance is equivalent.

## 4. No changes authorized to Charter text

This audit records findings only. It does not amend either language edition, alter the canonical source, approve or ratify the Charter, or settle institutional/legal questions. Any text correction should follow source verification, a tracked change proposal, and owner approval.

## 5. Next audit stage

1. Inspect the English DOCX/PDF and Persian DOCX/PDF for the numbering and domain-string issues.
2. Perform clause-level comparison of Parts IX–XIII, including the Covenant, Technical Appendix, Ten-Year Roadmap, and Presenter Standing.
3. Build a controlled bilingual glossary for key terms, including wisdom, reason/intellect, dignity, collective reason, ethical bindingness, and institutional titles.
4. Only then produce a consolidated discrepancy register with severity, source evidence, proposed resolution, and approval status.
