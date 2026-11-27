# Eternal Wisdom Charter — Document Control Map and Foundation Roadmap

**Document ID:** WI-GOV-CHARTER-001  
**Version:** 0.1.0-draft  
**Status:** Review proposal  
**Owner:** WisdomPact maintainers under WisdomCore document-control rules  
**Scope:** Charter source hierarchy, status semantics, reconciliation and next foundation steps.

## 1. Purpose

This document provides a control map to prevent the Charter, annexes, architecture, registry, technical specifications and operational implementation from being treated as interchangeable. It is an inventory/control proposal, not a replacement Charter and not an approval of documents listed below.

## 2. Normative and document hierarchy

1. **Eternal Wisdom Charter / منشور حکمت جاویدان** — foundational commitments, principles, rights, duties and limits. Approved text is authoritative only when the controlled source and approval record are verified.
2. **Charter annexes and protocols** — operational interpretation proposals, participation, privacy, deliberation, recognition, appeals and revision procedures. An annex is not incorporated merely by being present in Git.
3. **Master Whitepaper and Master Architecture** — ecosystem-wide conceptual and architectural model.
4. **Master Registry** — controlled inventory of components, systems, products, repositories and lifecycle status.
5. **Domain and technical specifications** — system behavior, APIs, schemas, security, economic design and implementation constraints.
6. **Operational policies and implementations** — approved workflows, service operations and deployed capabilities.

No product, administrator, token, algorithm, repository, or majority process may silently override Charter rights and safeguards. Conflicts require documented review and appropriate pause/containment.

## 3. Controlled status vocabulary

Use these statuses consistently:
- **Planned:** approved for consideration or roadmap, not drafted as a complete proposal.
- **Draft:** authored working text, not yet submitted for formal review.
- **Review:** submitted for review; comments/approval unresolved.
- **Approved:** formally approved through the documented process; approval evidence and scope must be recorded.
- **Superseded:** replaced by a newer controlled document; retain traceability.
- **Archived:** retained for history, not current guidance.
- **Deprecated:** discouraged/retired, with replacement or reason recorded.

A file, commit, PR merge, or website display does not automatically make a document Approved or Published. Document approval and public publication are separate controls.

## 4. Current known source map (snapshot; verify before relying)

| Source / document | Known status | Authority / role | Required action |
|---|---|---|---|
| charter/CHARTER.md | Reserved canonical path; source text not yet verified in the reviewed README | Intended canonical Markdown for approved Charter | Import and verify exact approved text; preserve provenance/version |
| Persian and English master editions | Parallel controlled editions intended | Same Charter identity in two languages | Confirm source, edition/version, translation alignment and approval |
| Participation and Shared Action annex | Proposed annex for public review | Participation rights/duties, attribution, deliberation, recognition, privacy and safeguards | Review; do not treat as incorporated Charter |
| WI-CA-001 | Proposed architectural baseline, v0.1.0 | Charter-centered participatory operating architecture | Review alignment, dependencies and architecture conformance |
| WI-DR-001 | Review baseline/action required (2026-10-05) | Reconciliation findings and risk register | Track each critical finding to a controlled resolution |
| WisdomCore WI-ARCH-CHARTER-001 | Draft architecture baseline, merged in PR #199; merge is not document approval | Digital infrastructure foundation and roadmap | Review/approve document status separately |
| WisdomCore WI-ARCH-WL-002 | Draft blueprint proposed in PR #200 | WisdomLand capability map and phased infrastructure | Await review/merge; then domain review |
| WisdomEconomy WI-ECON-LEARN-001 | Draft framework proposed in PR #2 | Learning, contribution and support reward model | Await review/merge; later develop pilot specification |
| WisdomCore Registry WI-MR-002 | Controlled registry instance | Inventory and canonical repository/component mappings | Continue reconciliation; verify WisdomCosmos scope separately |

This table is a partial snapshot based on files inspected. It is not a full inventory of all Charter directory files or a claim that the canonical source is complete.

## 5. Document approval and publication controls

For each document, record:
- document ID, canonical title, version, language, owner;
- status and status date;
- parent authority and related documents;
- source/provenance and translation relationship;
- reviewer(s), review result, approval authority and evidence;
- change summary, supersession/replacement and next review date;
- publication state and publication location (separate from Git status).

Do not set Approved without a recorded decision. Do not set Published without an explicit publication action. Drafts should visibly state their status.

## 6. Reconciliation actions

### Priority 0 — source integrity
- Locate the exact approved Persian Charter source and provenance.
- Verify the English edition against the approved Persian source (or documented source-language policy).
- Import canonical source into the reserved canonical path only after verification.
- Resolve legacy Global naming only after canonical replacement files are verified; preserve legacy history.

### Priority 1 — critical review findings
- Resolve inconsistent document hierarchy chains and exact WI-MR titles.
- Normalize WisdomCore meaning: Layer 0 architecture entity versus participant-facing UX expression.
- Explicitly distinguish conceptual realms, experience spaces and logical layers.
- Normalize canonical system names in Registry and documentation.
- Define normative status and legal disclaimers for Charter, Pact, Manifesto and annexes.
- Establish conformance gate for implementation (Registry ID, layer, relationships, spec, security/privacy, dependencies, status, legal/governance, traceability).

### Priority 2 — participation and learning/economy
- Review proposed participation annex and WI-CA-001 architecture.
- Review WisdomEconomy Learn/Contribute/Support framework.
- Define learning evidence, competency, accessibility routes, privacy and appeals.
- Separate points, reputation, grants, compensation, treasury assets and token balances.
- Require explicit approvals before reward pilots or financial/token activation.

### Priority 3 — controlled roadmap
- Charter source and edition reconciliation.
- Document/Registry/architecture alignment.
- Accessible Charter and learning/knowledge pathways.
- Participation, collaboration, project and review workflows.
- Deliberation and governance pilots.
- Non-financial recognition pilot, followed by bounded reward pilot only with approvals.
- WisdomLand realm integration and progressive expansion.

## 7. Immediate next deliverables

1. Verified canonical Charter source and bilingual alignment record.
2. Document hierarchy and Registry reconciliation PRs.
3. Review disposition matrix for WI-DR-001 findings (CR-01 through CR-06 and technical findings).
4. Charter annex review/decision record.
5. Learning and contribution rewards pilot specification (only after framework review).
6. WisdomLand infrastructure ADR set and dependency backlog.

## 8. Non-authorization

This control map does not approve the Charter, annexes, policies, architecture, reward programs or implementations. It does not authorize public website publication, production deployment, collection of sensitive data, financial services, token issuance, binding voting or institutional/legal claims. These require their own documented approvals.
