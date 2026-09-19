# WI-MR-001 — Master Registry & Document Control

**Project:** WisdomIntercessor  
**Repository:** WisdomPact  
**Status:** Draft / Controlled  
**Version:** 0.1.0  
**Language:** Persian-first; English companion versions may be added  
**Owner:** WisdomIntercessor

## 1. Purpose

This document establishes the master registry and document-control rules for the WisdomIntercessor knowledge base hosted in GitHub.

The registry is the authoritative index of controlled project documents. It is intended to prevent duplicate, obsolete, unapproved, or disconnected documents from becoming part of the project architecture.

## 2. Scope

This registry covers:

- governance and foundational documents;
- master architecture;
- technical architecture;
- experience and UX architecture;
- operational specifications;
- research and whitepaper material;
- implementation specifications;
- controlled decisions and revisions.

GitHub is the version-control and collaboration layer. Publication to the public website is a separate release decision.

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

A document identifier is permanent once formally registered. Its content changes by version, not by silently reusing the identifier for a different subject.

## 4. Controlled Statuses

- **Draft** — working material; not an approved project requirement.
- **Review** — submitted for structured review.
- **Approved** — approved as a project baseline.
- **Superseded** — replaced by a newer approved version.
- **Archived** — retained for historical traceability and no longer active.
- **Deprecated** — intentionally withdrawn from future implementation.

## 5. Source-of-Truth Rule

The latest approved version of a controlled document is the project baseline.

A website page, AI-generated draft, external document, or conversational note does not override an approved GitHub document unless the change is explicitly recorded and approved.

## 6. Change Control

Every substantive change must:

1. identify the affected document;
2. state the reason for change;
3. preserve historical traceability through Git;
4. update dependent documents when necessary;
5. distinguish conceptual decisions from implementation decisions.

No public release is implied merely by committing a change to this repository.

## 7. Initial Registry

| ID | Document | Status |
|---|---|---|
| WI-MR-001 | Master Registry & Document Control | Draft |
| WI-MA-001 | Master Architecture & System Structure | Draft |
| WI-TA-001 | Technical Architecture | Planned |
| WI-UX-001 | Outdoor / Indoor / WisdomSpace Experience Architecture | Planned |

## 8. Architectural Vocabulary

The repository must distinguish three categories:

**Concept** — an idea, principle, model, or future possibility.

**Service** — a capability offered to participants of the ecosystem.

**Product** — a concrete implementable offering with defined scope and lifecycle.

A concept must not automatically become a product merely because it has been named.

## 9. Release Boundary

GitHub repository changes are development artifacts. Website publication, token deployment, public governance activation, and other consequential releases require separate explicit approval.

## 10. Revision History

### 0.1.0
Initial controlled registry established during the WisdomPact repository alignment with the current WisdomIntercessor architecture.
