# Site Master Structure & Page Template Specification

**Document ID:** WI-UA-002  
**Status:** Reconciliation Baseline  
**Version:** 1.0.0  
**Date:** 2026-10-05  
**Project:** WisdomIntercessor.com  
**Parent:** WI-MA-001 / WI-UA-001  
**Registry Dependency:** WI-MR-001 / WI-MR-002  
**Foundational Dependency:** Wisdom Pact / Eternal Wisdom Charter  

## 1. Purpose

This specification defines the public information architecture, page hierarchy, navigation, reusable page templates and architectural mappings for wisdomintercessor.com.

It does **not** create a new system architecture. It is the website projection of the existing Layer 0 + 8 architecture, the three conceptual realms, the current three-space experience model, the controlled document hierarchy and the existing UX baselines.

The governing distinction is:

**Registry = what exists; Architecture = where it belongs and how it relates; Specification = how it behaves; Website = public experience and publication surface.**

## 2. Authoritative model

The website must preserve three separate dimensions:

### 2.1 Conceptual dimension — three realms

1. **عالِم صغری — Human Microcosmic:** human as participant, chooser and agent.
2. **عالم صغری — Microcosmic Realm:** the digital/civilizational environment connecting people to knowledge, tools, services, economy and governance.
3. **عالم کبری — Macrocosm:** Earth, nature, society, time, space and existence.

These are conceptual relationships, not three WordPress page categories.

### 2.2 Experience dimension — three principal spaces

1. **عالم کبری / Cosmic Realm** — world/time/place interface.
2. **دیوان حکمت / Wisdom Divan** — eight governance/coordination halls.
3. **WisdomCore** — participant operational center and gateway to WisdomSpace.

### 2.3 Logical dimension — Layer 0 + 8

- L0 WisdomCore
- L1 WisdomNetwork
- L2 WisdomChain
- L3 WisdomTreasury
- L4 WisdomKnowledge
- L5 WisdomGuard
- L6 Wisdom Governance & Justice
- L7 WisdomLife & Health
- L8 Wisdom of Existence & Time

A page may reference all three dimensions, but must not collapse them into one taxonomy.

## 3. Canonical site hierarchy

```text
wisdomintercessor.com
│
├── 01. Gateway / رستاخیز حکمت جاویدان
│   ├── Eternal Wisdom Charter / Wisdom Pact
│   ├── Principles
│   ├── Invitation / Participation
│   └── Enter Wisdom System
│
├── 02. عالم کبری / Cosmic Realm
│   ├── Cosmic View
│   ├── Earth
│   ├── Time
│   ├── Place / Geography
│   ├── Living Data Context
│   └── Enter Wisdom Divan / WisdomCore
│
├── 03. دیوان حکمت / Wisdom Divan
│   ├── WisdomNetwork
│   ├── WisdomChain
│   ├── WisdomTreasury
│   ├── WisdomKnowledge
│   ├── WisdomGuard
│   ├── Wisdom Governance & Justice
│   ├── WisdomLife & Health
│   └── Wisdom of Existence & Time
│
├── 04. WisdomCore
│   ├── Personal Core / Dashboard
│   ├── My WisdomSpace
│   ├── Identity / WisdomID
│   ├── Knowledge & Work
│   ├── Resources / Treasury
│   ├── Economy / Chain
│   ├── Security / Guard
│   ├── Governance / Participation
│   ├── Life & Health
│   └── Existence & Time
│
├── 05. WisdomSpace
│   ├── Personal Showcase
│   ├── Works
│   ├── Research / Knowledge
│   ├── Projects
│   ├── Skills
│   ├── Services / Products
│   ├── Resources / Assets
│   └── Collaboration
│
├── 06. Wisdom Library / Knowledge & Documents
│   ├── Foundational Documents
│   ├── Architecture
│   ├── Registry
│   ├── Technical Specifications
│   ├── Research / Papers
│   ├── Manifesto
│   └── Archive / Versions
│
├── 07. Governance & Participation
│   ├── Wisdom Pact / Charter Governance
│   ├── Proposals / Critique
│   ├── Decisions / Architecture Decisions
│   ├── Participation Rules
│   ├── Moderation / Appeals
│   └── Transparency
│
├── 08. About / Project
│   ├── What is WisdomIntercessor?
│   ├── Vision / Mission
│   ├── Architecture Overview
│   ├── Open Architecture
│   ├── GitHub Bridge
│   └── Roadmap / Status
│
└── 09. Legal, Privacy, Security & Accessibility
    ├── Legal Notice / Operator
    ├── Terms / Participation Terms
    ├── Privacy
    ├── Cookies / Similar Technologies
    ├── Intellectual Property / Licenses
    ├── Security / Responsible Disclosure
    ├── Accessibility
    └── Data / AI Transparency
```

The above is an information architecture. It does not create new logical layers or products.

## 4. Primary navigation

The global navigation must remain spatial and architectural rather than product-heavy.

**Primary:**

**Gateway → عالم کبری → دیوان حکمت → WisdomCore → WisdomSpace → Library → Governance → About**

**Utility:** Language, Search, Documents, GitHub Bridge, Account/Entry when operational.

**Legal/footer:** Legal, Privacy, Terms, IP, Security, Accessibility, Contact/Responsible Disclosure.

No product should automatically become a primary navigation item merely because it exists in the Registry.

## 5. Universal navigation contract

Every page must provide:

- current location;
- parent location;
- clear path to one of the three principal spaces;
- related Layer where applicable;
- related Registry entity where applicable;
- related foundational document where applicable;
- language switch;
- search/discovery path;
- accessible page title and semantic headings;
- no dead-end terminal state.

Controlled document pages must additionally show Document ID, version, status, effective date where applicable, source, language and related documents.

## 6. Page templates

### T01 — Gateway / Foundational Declaration

Use for the opening Wisdom Pact/Charter experience.

Required blocks:

1. identity/title;
2. short purpose;
3. declaration/manifesto entry;
4. document status;
5. three-space gateway;
6. participation invitation;
7. critique/feedback route;
8. document vault/library link.

The Gateway is not a technical dashboard.

### T02 — Cosmic Realm

Use for عالم کبری.

Required blocks:

- cosmic/world visual context;
- time/place context;
- progressive focus/zoom where implemented;
- Earth/geography context;
- living-data status;
- gateway to Divan/Core;
- accessible alternative representation for visual/cinematic elements.

Future live data must be marked as Planned/Prototype/Operational according to actual implementation.

### T03 — Wisdom Divan

Use for the central eight-hall coordination surface.

Required blocks:

- Divan purpose;
- eight halls;
- each hall's layer mapping;
- current status;
- related documents;
- entry to relevant Core workflows where operational.

The Divan must not imply that every hall is already a deployed service.

### T04 — Layer / Hall Detail

Use for each of the eight Wisdom domains.

Required blocks:

1. canonical name;
2. Persian name;
3. layer ID;
4. mission;
5. scope;
6. entities/products registered under it;
7. status;
8. dependencies/interfaces;
9. governing specifications;
10. security/privacy/legal notes;
11. related Divan and Core routes.

### T05 — WisdomCore Dashboard

Use for the participant operational center.

Required blocks:

- identity state;
- active work/tasks;
- eight service/tool domains;
- recent activity where appropriate;
- WisdomSpace access;
- participation/governance entry;
- privacy/security controls.

No claim of production functionality unless the underlying service is operational.

### T06 — WisdomSpace / Personal Showcase

Use for participant-owned presence.

Required blocks:

- identity/profile;
- works;
- research/knowledge;
- projects;
- skills;
- services/products;
- resources/assets;
- collaboration;
- visibility controls.

Private, public and selectively shared states must be distinguishable.

### T07 — Controlled Document

Use for Charter, Manifesto, Whitepaper, Registry, Architecture and Specifications.

Required metadata:

- Document ID;
- official title;
- Persian/English title;
- document class/type;
- version;
- status;
- parent;
- supersedes/superseded-by;
- source;
- effective date if applicable;
- language;
- license/rights statement;
- related documents;
- download/read options;
- change history.

The page must distinguish **published** from **approved normative baseline**.

### T08 — Registry Entity

Use for a Layer, Domain, Platform, Product, Protocol, Tool, Service, Institution, Program, Capability, Standard, Asset or Document registered in WI-MR-002.

Minimum display:

- Registry ID;
- official/Persian name;
- type;
- primary layer;
- parent;
- mission/function;
- status;
- dependencies/interfaces;
- source;
- specification links;
- implementation status.

A Registry page must never imply that registration equals deployment.

### T09 — Research / Knowledge Object

Use for books, articles, papers, datasets, laws, treaties, standards and related library objects.

Metadata should follow the existing knowledge-architecture direction: title, author, publisher, date, language, subject, license, edition, version, identifiers and source, plus provenance/evidence status where relevant.

### T10 — Governance / Decision

Use for proposals, architecture decisions, amendments, reviews and documented decisions.

Required blocks:

- issue/proposal;
- scope;
- evidence;
- affected entities;
- decision;
- rationale;
- authority/process;
- effective date;
- appeal/review route where applicable;
- version/change impact.

### T11 — Legal / Privacy / Security / Accessibility

Use for normative public policies.

Each policy must show owner/operator, version, effective date, scope, contact route, rights/process where applicable and relationship to higher-level architecture.

### T12 — About / Architecture Overview

Use for public orientation. It explains the project without replacing controlled documents. It should link to the Charter, Master Whitepaper, Registry, Master Architecture, technical architecture, site specification and GitHub.

## 7. Layer-to-site mapping

| Layer | Canonical site surface | Primary experience | Core function |
|---|---|---|---|
| L0 | WisdomCore | WisdomCore | foundational/meta + participant core |
| L1 | WisdomNetwork | Divan / Core | identity, connection, media, interaction |
| L2 | WisdomChain | Divan / Core | trust, value, ownership, transactions |
| L3 | WisdomTreasury | Divan / Core | resources, treasury, allocation |
| L4 | WisdomKnowledge | Divan / Core | knowledge, AI, science, learning |
| L5 | WisdomGuard | Divan / Core | security, protection, resilience |
| L6 | Governance & Justice | Divan / Core | governance, law, justice |
| L7 | WisdomLife & Health | Divan / Core | life and health |
| L8 | Wisdom of Existence & Time | Cosmic / Divan / Core | existence, memory, time, future |

This table is a navigation mapping, not a change to the logical architecture.

## 8. Document hierarchy on the website

The public documentation tree must mirror the controlled hierarchy:

**Wisdom Pact / Charter**
→ **WI-MW-001 Master Whitepaper**
→ **WI-MR-001 Registry Specification**
→ **WI-MR-002 Master Registry**
→ **WI-MA-001 Master Architecture**
→ **WI-TA-001 / WI-DA-001 / WI-AI-001 / WI-SA-001 / WI-GA-001 / WI-EA-001 / WI-LA-001 / WI-UA-001 / WI-ME-001**
→ Product/technical specifications
→ Operational documents.

The website may provide multiple routes to the same object, but it must not create duplicate authoritative copies with independent status.

## 9. Publication/status model

The site must visually distinguish:

- Concept
- Proposed
- Registered
- Specified
- Prototype
- Beta
- Operational
- Deprecated/Retired

These are implementation/status states, not philosophical judgments.

A document may additionally be:

- Draft
- Review
- Approved Baseline
- Superseded
- Archived

A public page must never infer one status dimension from another.

## 10. Content governance and source-of-truth rule

For every architectural object:

- Registry identity comes from WI-MR-002.
- Layer placement comes from WI-MA-001.
- Behavior comes from the applicable specification.
- Implementation status comes from implementation/operational records.
- Normative principles come from the Wisdom Pact/Charter.
- Public explanation comes from the website but may not silently redefine the controlled source.

## 11. Three-space ↔ three-realm mapping rule

The website must include a visual or textual explanation with the following semantics:

**عالِم صغری (human)** = participant/agency.

**عالم صغری (digital realm)** = the ecosystem environment in which knowledge, services, participation and coordination occur.

**عالم کبری (macrocosm)** = the world/existence that the ecosystem interfaces with.

The three website spaces are experience surfaces across this relationship:

- Cosmic Realm primarily expresses Macrocosm.
- WisdomCore primarily expresses participant agency and access into the Microcosmic Realm.
- Wisdom Divan provides the governance/coordination surface inside the Microcosmic Realm.
- WisdomSpace expresses participant presence within WisdomCore.

This mapping must not be represented as a new four- or five-layer architecture.

## 12. Accessibility, privacy and legal baseline

Every template must support:

- keyboard navigation;
- semantic headings and landmarks;
- accessible names/labels;
- non-visual alternatives to essential visual information;
- responsive/mobile-first behavior;
- low-bandwidth fallback where practical;
- Persian/English language equivalence;
- privacy-respecting analytics;
- clear document/source status;
- accessible contact and complaint routes.

Legal and privacy pages must be available before collecting non-essential personal data or enabling broad participation.

## 13. Future feature rule

A future feature must answer five questions before receiving a public navigation location:

1. What is its Registry identity?
2. What is its primary Layer?
3. Is it Concept, Service, Product, Tool or another Registry type?
4. Which experience surface exposes it?
5. Which specification and implementation status support the claim?

If these cannot be answered, it remains documentation/proposal content rather than a public product destination.

## 14. No-dead-end rule

Every major page must provide at least one path back to the spatial model and one path toward deeper evidence/documentation. Controlled documents must provide parent/related-document navigation. Terminal pages such as a PDF viewer or external repository page must provide an explicit return route.

## 15. WordPress implementation boundary

WordPress is the current public CMS/application surface. It is not the long-term definition of the architecture.

The website should therefore implement stable templates and metadata fields while keeping advanced live-data, identity, AI, economic, governance and other services attachable behind those stable experience contracts.

## 16. GitHub bridge

The site must provide a permanent **GitHub Bridge** to the WisdomPact repository and relevant controlled documentation. The bridge is a navigation/publication mechanism, not an automatic deployment mechanism.

The repository remains the controlled source for architecture/documentation; the website is the public experience and publication surface. A GitHub commit does not automatically mean public publication or production activation.

## 17. Acceptance criteria

The Site Master Structure is accepted when:

- every primary page maps to one experience space or the controlled documentation/legal/support area;
- every Layer 0 + 8 domain has a defined navigation destination;
- every controlled document has a template and metadata contract;
- three realms, three spaces and nine logical layers are explicitly distinguished;
- no page invents a new architectural layer;
- product names not present in the controlled Registry are not promoted to primary navigation;
- status is visible and truthful;
- Persian/English structure remains equivalent;
- privacy, legal, security and accessibility entry points exist;
- every page has a return/discovery path;
- GitHub and WordPress remain linked without treating either as an automatic substitute for the other.

## 18. Final architectural statement

**WisdomIntercessor.com is the public experience and knowledge/publishing surface of the WisdomIntercessor architecture. It does not replace the Charter, Master Whitepaper, Master Registry or Master Architecture, and it does not create a competing taxonomy.**

The site expresses the existing architecture through a controlled journey:

**Wisdom Pact / Charter → عالم کبری → دیوان حکمت → WisdomCore → WisdomSpace**, with the controlled Library, Registry, Governance and Legal/Privacy/Security/Accessibility systems accessible throughout.

**Wisdom for all, all for Eternal Wisdom.**
