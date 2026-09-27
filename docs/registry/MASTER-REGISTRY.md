# WisdomPact — Master Registry

**Project:** WisdomIntercessor  
**Repository:** WisdomPact  
**Registry authority:** WI-MR-001  
**Registry version:** 0.2.0  
**Last reviewed:** 2026-09-27

This file is the human-readable index of controlled and planned documents in the WisdomPact repository. It is governed by `docs/registry/WI-MR-001.md`.

## Status legend

- **Planned** — identified but not yet created.
- **Draft** — working document; not an approved baseline.
- **Review** — submitted for structured review.
- **Approved** — approved project baseline.
- **Final Baseline** — current baseline designation in the source document; formal approval remains subject to registry control unless explicitly recorded as Approved.
- **Alignment Required** — existing material needs normalization before becoming canonical.
- **Decision Record** — records an architectural decision and its consequences.

## Foundation

| ID | Title | Path | Version | Status | Notes |
|---|---|---|---:|---|---|
| EW-CHARTER | Eternal Wisdom Charter / Wisdom Pact | charter/ | existing | Alignment Required | Existing Persian/English DOCX/PDF files use legacy “Global” filenames. |
| EW-CHARTER-MD | Canonical Markdown Charter | charter/CHARTER.md | — | Planned | File currently exists but is empty. |

## Registry & decisions

| ID | Title | Path | Version | Status |
|---|---|---|---:|---|
| WI-MR-001 | Master Registry & Document Control | docs/registry/WI-MR-001.md | 0.2.0 | Draft / Controlled |
| ADR-2026-09-25 | Three-Space Architecture Decision | docs/registry/ADR-2026-09-25-Three-Space-Architecture.md | 1.0 | Decision Record |

## Architecture

| ID | Title | Path | Version | Status |
|---|---|---|---:|---|
| WI-MA-001 | Master Architecture & System Structure | docs/architecture/WI-MA-001.md | 0.1.0 | Draft |
| WI-MA-002 | Final Experience & Site Architecture | docs/architecture/WI-MA-002-Final-Experience-and-Site-Architecture.md | 1.0.0 | Final Baseline |
| WI-TA-001 | Technical Architecture | docs/architecture/WI-TA-001.md | 0.1.0 | Draft |
| WI-UX-001 | Outdoor / Indoor / WisdomSpace Experience Architecture | docs/architecture/WI-UX-001.md | 0.1.0 | Draft |
| WI-UX-002 | Three-Space Experience Architecture | docs/architecture/WI-UX-002-Three-Space-Experience-Architecture.md | 1.0.0 | Final Baseline |

## Planned foundational documents

These are registry targets, not yet claims of completed documents:

| Proposed ID | Document | Target area |
|---|---|---|
| WI-GV-001 | Governance & Justice | docs/governance/ |
| WI-DG-001 | Data Governance & Privacy | docs/governance/ |
| WI-EC-001 | Wisdom Economy | docs/economy/ |
| WI-WM-001 | Memory & Civilization Record | docs/memory/ |
| WI-WS-001 | WisdomSpace | docs/experience/ |
| WI-RM-001 | Roadmap & Exit Criteria | docs/roadmap/ |

These IDs become controlled documents only when their specifications are created and registered.

## Repository gaps

1. Canonical Markdown Charter is missing.
2. Legacy Charter filenames containing “Global” require alignment.
3. The registry needs future dependency/version relationships as documents mature.
4. Governance, privacy/data, economy, memory, WisdomSpace, and roadmap specifications are not yet present as controlled documents.
5. Research and translation directories currently contain only README placeholders.

## Rule

Do not create a document merely to fill a directory. A new controlled document must have a defined purpose, identifier, owner, scope, status, and relationship to existing architecture.
