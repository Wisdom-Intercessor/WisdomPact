# WI-MR-001 — Master Registry & Document Control

**Project:** WisdomIntercessor  
**Repository:** WisdomPact  
**Status:** Draft / Controlled  
**Version:** 0.2.0  
**Language:** Persian-first; English companion versions may be added  
**Owner:** WisdomIntercessor

## 1. Purpose

This document establishes the master registry and document-control rules for the WisdomIntercessor knowledge base hosted in GitHub.

The registry is the authoritative index of controlled project documents. It prevents duplicate, obsolete, unapproved, or disconnected documents from silently becoming part of the project architecture.

## 2. Scope

This registry covers:

- foundational Charter/Pact documents;
- governance and institutional documents;
- master and technical architecture;
- UX and experience architecture;
- implementation specifications;
- research and evidence;
- controlled architecture decisions;
- release and revision records.

GitHub is the version-control and controlled documentation layer. Public website publication is a separate release decision.

## 3. Naming Convention

Controlled documents use:

`WI-[DOMAIN]-[NUMBER]`

Current master families include:

- `WI-MR` — Master Registry and document control
- `WI-MA` — Master Architecture
- `WI-TA` — Technical Architecture
- `WI-UX` — Experience Architecture
- `WI-W` — Wisdom ecosystem specifications
- `WI-G` — Governance and institutional specifications

A document identifier is permanent once formally registered. Its content changes by version; the identifier must not be silently reused for a different subject.

## 4. Controlled Statuses

- **Planned** — identified in the roadmap/registry but not yet created.
- **Draft** — working material; not an approved project requirement.
- **Review** — submitted for structured review.
- **Approved** — approved as a project baseline.
- **Superseded** — replaced by a newer approved version.
- **Archived** — retained for historical traceability and no longer active.
- **Deprecated** — intentionally withdrawn from future implementation.

A file existing in GitHub does not by itself make it Approved.

## 5. Source-of-Truth Rule

For each controlled document, the latest **Approved** version is the project baseline.

A website page, AI-generated draft, external document, or conversational note does not override an approved GitHub document unless the change is explicitly recorded through document control.

Where no Approved version exists, the latest Draft/Review material is informative only.

## 6. Change Control

Every substantive change must:

1. identify the affected document;
2. state the reason for change;
3. preserve historical traceability through Git;
4. update dependent documents when necessary;
5. distinguish conceptual decisions from implementation decisions;
6. update the registry status/version when the controlled state changes.

No public release is implied merely by committing a change to this repository.

## 7. Master Registry

The current document inventory is maintained in:

**`docs/registry/MASTER-REGISTRY.md`**

That index records document ID, title, path, version, status, language, dependency/relationship, and notes.

## 8. Current Controlled Document Inventory

| ID | Document | Path | Version | Status |
|---|---|---|---|---|
| WI-MR-001 | Master Registry & Document Control | docs/registry/WI-MR-001.md | 0.2.0 | Draft / Controlled |
| WI-MA-001 | Master Architecture & System Structure | docs/architecture/WI-MA-001.md | 0.1.0 | Draft / Architectural Baseline |
| WI-MA-002 | Final Experience & Site Architecture | docs/architecture/WI-MA-002-Final-Experience-and-Site-Architecture.md | 1.0.0 | Final Baseline |
| WI-TA-001 | Technical Architecture | docs/architecture/WI-TA-001.md | 0.1.0 | Draft |
| WI-UX-001 | Outdoor / Indoor / WisdomSpace Experience Architecture | docs/architecture/WI-UX-001.md | 0.1.0 | Draft |
| WI-UX-002 | Three-Space Experience Architecture | docs/architecture/WI-UX-002-Three-Space-Experience-Architecture.md | 1.0.0 | Final Baseline |
| ADR-2026-09-25 | Three-Space Architecture Decision | docs/registry/ADR-2026-09-25-Three-Space-Architecture.md | 1.0 | Decision Record |
| EW-CHARTER | Eternal Wisdom Charter / Wisdom Pact | charter/ | existing files | Alignment Required |

## 9. Foundational Charter Rule

The Eternal Wisdom Charter / Wisdom Pact is the opening foundational declaration of the public experience.

The repository must maintain one controlled document identity for the Charter, with Persian and English versions linked to the same controlled version.

Existing files whose names still contain **Global** are legacy repository artifacts and must be aligned with the current official title before being treated as the canonical release.

The currently empty `charter/CHARTER.md` is reserved for the canonical Markdown representation and must not be treated as complete until the approved Charter text is placed there.

## 10. Architectural Vocabulary

The repository must distinguish three categories:

**Concept** — an idea, principle, model, or future possibility.

**Service** — a capability delivered to participants.

**Product** — a defined deliverable with user-facing scope and lifecycle.

A concept must not automatically become a product merely because it has been named.

## 11. Architecture Decision Records

Material architectural choices that affect multiple documents or constrain future implementation should be recorded as ADRs.

An ADR records the decision and its consequences. It does not replace the controlled architecture document it affects.

## 12. Release Boundary

GitHub repository changes are development/documentation artifacts.

The following require separate explicit release decisions:

- public website publication;
- production deployment;
- token or wallet deployment;
- financial activity;
- public governance activation;
- external service activation.

## 13. Repository Structure

The controlled repository currently uses:

- `charter/` — foundational Charter/Pact materials;
- `docs/registry/` — registry and architecture decisions;
- `docs/architecture/` — architecture baselines;
- `research/` — research and evidence;
- `translations/` — translation/alignment material;
- `media/` — controlled repository media.

New top-level directories should not be introduced without a documented reason.

## 14. Revision History

### 0.2.0
Normalized the registry model, added explicit Planned/Review states, established the master registry index, recorded current architecture baselines, and identified the Charter naming/alignment gap.

### 0.1.0
Initial controlled registry established during the WisdomPact repository alignment with the current WisdomIntercessor architecture.
