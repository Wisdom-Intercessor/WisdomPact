# WI-DR-001 — Document Architecture, Technical & Legal Review

**Status:** Review Baseline / Action Required  
**Version:** 1.0.0  
**Date:** 2026-10-05  
**Project:** WisdomIntercessor

## 1. Executive conclusion

The existing documents have a strong architectural skeleton: Layer 0 + 8, Registry/Architecture/Specification/Implementation separation, open architecture, identity/privacy invariants, security, provenance, interoperability, AI governance, resilience and a three-space experience model.

The principal weakness is not lack of architecture. It is **control integrity**. Several authoritative documents use overlapping names, slightly different hierarchy chains, different meanings for the same terms, and different status semantics. The main risk is that WordPress, GitHub, Registry and future specifications become four interpretations of one architecture.

The correct remedy is controlled reconciliation, not another conceptual expansion.

## 2. Critical findings

### CR-01 — Document hierarchy is internally inconsistent

Some documents describe Charter → WI-MW-001 → WI-MR-001 → architecture specifications, while the Master Registry material explicitly places WI-MR-002 between WI-MR-001 and WI-MA-001. The distinction must be explicit:

- **WI-MR-001** = specification/standard defining how the Registry works.
- **WI-MR-002** = the actual controlled Master Registry instance.
- **WI-MA-001** = architecture derived from the controlled Registry.

Canonical chain:

**Wisdom Pact/Charter → WI-MW-001 → WI-MR-001 → WI-MR-002 → WI-MA-001 → domain/technical specifications → implementation/operations.**

### CR-02 — Repository terminology conflicts with controlled document identity

The current WisdomPact README calls WI-MR-001 “Master Registry & Document Control”, while the controlled document is “Master Registry Specification”. This is a source-of-truth defect. Exact IDs and titles must be used everywhere.

### CR-03 — WisdomCore is semantically overloaded

WisdomCore is Layer 0 in the master architecture and also the participant's personal operational center in the website architecture. These can coexist only if the documentation explicitly states that the public UX surface is an expression of the Layer 0 entity, not a second Layer or duplicate entity.

### CR-04 — Three conceptual realms and three experience spaces are not mapped one-to-one

The architecture defines human microcosmic / microcosmic realm / macrocosm. The site model defines Cosmic Realm / Wisdom Divan / WisdomCore. They are different categories. The site must explicitly state:

**Conceptual realms describe the relationship; experience spaces describe user experience; logical layers describe system structure.**

### CR-05 — Layer naming needs normalization

Variants include WisdomLife vs WisdomLife & Health and Wisdom of Existence & Time vs WisdomExistence & Time. WisdomKnowledge is also used alongside broader intelligence/AI terminology. One canonical terminology table must be authoritative in the Registry.

### CR-06 — Charter, Pact and Manifesto need explicit normative status

The project correctly distinguishes Charter and Manifesto conceptually, but the public site must state whether each document is normative, visionary, contractual, institutional, advisory, or merely explanatory. A philosophical Charter must not accidentally be represented as a legally enforceable constitution, corporate instrument, governmental law or contract.

## 3. Technical findings

### T-01 — Architecture conformance control is missing as an explicit gate

Before implementation, verify: Registry ID; valid primary layer; parent/relationships; required specification; security/privacy coverage; interfaces/dependencies; truthful implementation status; legal/governance status; version/source traceability. This is governance, not a new architecture layer.

### T-02 — Lifecycle/status vocabulary needs one controlled model

The Registry has technical/legal/governance status fields, but the lifecycle vocabulary must be unified and defined. A possible controlled progression is proposed → registered → specified → prototype → beta → operational → deprecated/retired. “Registered” must never mean built, production-ready, legally active or available.

### T-03 — Versioning needs dependency semantics

Every controlled document should identify parent document/version, supersedes, superseded-by, effective date, review date, change summary, approver/reviewer and compatibility impact.

### T-04 — Single Source of Truth should become machine-readable

The Registry principle should be implemented as a machine-readable canonical export (JSON/YAML/CSV or equivalent), from which site navigation, entity names and documentation indexes can eventually be generated. WordPress pages and README files should not become competing registries.

### T-05 — Provenance must be a web content contract

The Master Architecture already calls for stable document IDs, metadata, versions, sources and preservation. Controlled document pages should expose at minimum: Document ID, title, version, status, effective date, source, parent, language and last review.

### T-06 — Data governance needs an operational inventory

The architecture distinguishes Data Owner, Data Steward, Data Custodian and Data Processor and covers purpose, necessity, consent, privacy, bias, security and retention. What is still needed is an operational inventory mapping data category, purpose, legal basis, location, processor, retention, access class and deletion path.

### T-07 — WisdomID needs a public trust/status boundary

WisdomID has strong invariants: it is not protocol-owned, not a tradable asset, not a universal reputation score, and must remain separate from political power and wealth. The website must clearly distinguish current implementation from future architecture and must not imply that a production identity service exists if it does not.

### T-08 — AI governance needs feature-level disclosure

The architecture already covers model evaluation, provenance, prompt governance, retrieval security, tool injection, human confirmation and AI constitutional principles. Each deployed AI feature should additionally disclose purpose, provider/model where appropriate, limitations, human oversight, data handling and whether output is advisory or generated.

For EU-facing use cases, AI transparency obligations require current legal assessment; the European Commission states that Article 50 transparency rules apply from 2 August 2026 to specified AI systems. citeturn0search0turn0search4

### T-09 — Security/resilience need implementation evidence

The master architecture already specifies least privilege, zero trust, auditability, incident response, backup, redundancy, RTO/RPO and recovery. The gap is operational evidence: owner, test frequency, recovery exercise, incident procedure and evidence of control effectiveness.

### T-10 — Accessibility needs to become a page-template requirement

Mobile-first, low-bandwidth, multilingual and assistive-technology compatibility are already recognized. The site specification should make accessibility mandatory for templates, with WCAG 2.2 as the technical baseline and EN 301 549 assessed where EU legal scope makes it relevant. WCAG 2.2 is a W3C Recommendation. citeturn0search2turn0search16

## 4. Legal and governance findings

### L-01 — Legal Architecture is referenced but not operationalized

The existence of “Legal Framework” in the master architecture does not itself establish a legal framework. A controlled legal baseline needs operator identity, legal personality, jurisdiction, applicable law, contractual capacity, liability model and dispute venue/process.

### L-02 — Operator/controller identity must be explicit

The public service needs an identified operator/publisher and, where personal data is processed, a defined controller/controller structure. If several parties jointly determine purposes and means, their responsibilities must be documented. GDPR Article 25 requires data protection by design and by default where GDPR applies. citeturn1search0

### L-03 — Privacy governance needs a public/legal layer

Implementation requires a privacy notice, purposes, legal bases where applicable, retention rules, data-subject rights, processor/subprocessor information, transfer rules, security contact, breach procedure and a rights-exercise route.

### L-04 — Terms and community rules need explicit instruments

If accounts, submissions, profiles, comments, collaboration, marketplace activity or community content are enabled, Terms of Use and Community/Content Rules are required operational instruments covering account responsibility, prohibited conduct, content rights, moderation, suspension, appeals and termination.

### L-05 — Moderation and appeal must precede broad community activation

The architecture already recognizes rights-oriented appeal and independent resolution for identity disputes. The public site should not open broad user-generated-content functionality without moderation and appeal processes. Where the EU Digital Services Act applies, notice-and-action, complaint, decision-reason and appeal obligations become relevant. citeturn1search1turn1search2

### L-06 — Intellectual property and licensing need a first-class policy

Open-source architecture does not automatically determine copyright ownership or licensing for every document, dataset, image, code component or user contribution. Each repository/document class needs a rights statement or license; user contributions need explicit ownership/licence/attribution/takedown rules.

### L-07 — Economic/token language needs a non-activation boundary

WisdomChain, WIS/Wisdomium, wallets, payments and economic infrastructure must be presented as architecture unless and until a separately reviewed legal/technical deployment exists. No diagram should be interpreted as an offer, custody service, investment product, exchange or payment service.

### L-08 — Global scope is not a jurisdiction

Before identity, finance, health, governance or community services become operational, the legal architecture needs a jurisdiction matrix covering operator, target market, service category, applicable law, data transfer and dispute venue.

### L-09 — Health and governance domains need claim boundaries

WisdomLife & Health and Governance & Justice are architectural domains. Public copy must not accidentally turn them into medical advice, regulated healthcare, legal advice, governmental authority or binding adjudication without the required operational and legal structures.

### L-10 — Preservation status needs formal distinction

The architecture correctly calls for stable IDs, hashes, versions, replicas and preservation. The records policy should distinguish archival copy, published version, approved normative baseline and evidentiary record.

## 5. Scientific / epistemic findings

### S-01 — “Wisdom” needs epistemic boundaries

Data → Information → Knowledge → Insight → Wisdom is a useful conceptual model, but “Wisdom” should not be presented as an objectively measurable scientific quantity without a defined methodology. Metrics should classify statements as empirical, normative, interpretive or speculative.

### S-02 — Evidence quality and uncertainty should be metadata

Knowledge objects should expose evidence status, uncertainty, date, source quality and whether a statement is normative or empirical. This follows the existing provenance/evidence direction rather than adding a new layer.

### S-03 — Semantic changes need controlled change management

Changing definitions such as Person, Organization, Resource, Rights, Credential, Evidence or Decision can change system behavior. Semantic changes should therefore receive impact analysis, migration notes and versioning.

### S-04 — Activity metrics must not be confused with impact

Views, registrations and transactions measure activity. Claims about trust, knowledge quality, resilience, well-being or civilizational impact require explicit outcome methodology.

## 6. Site-specific corrections

1. Use a stable experience shell plus controlled-document navigation rather than a product-heavy menu.
2. Explicitly distinguish the three experience spaces from the three conceptual realms.
3. Display controlled-document status, ID and version.
4. Give each controlled document a stable source/reference area.
5. Keep Persian and English versions equivalent in structure and normative meaning.
6. Give every page a parent, related space, related layer and return path.
7. Mark Concept / Planned / Prototype / Operational states visibly.
8. Expose privacy, legal, security, governance and accessibility entry points before broad participation.
9. Do not expose undocumented historical products as current architecture.
10. Do not create a new primary navigation category for every product.

## 7. Existing document domains that should close the gaps

The master architecture already anticipates the principal domains. The priority is completion and control, not new layers:

- WI-DA-001 — Data Architecture
- WI-AI-001 — Wisdom Intelligence Architecture
- WI-SA-001 — Security Architecture
- WI-GA-001 — Governance Architecture
- WI-EA-001 — Economic Architecture
- WI-LA-001 — Legal Architecture
- WI-UA-001 — User & UX Architecture
- WI-ME-001 — Metrics Architecture
- controlled Privacy/Data Governance instrument
- Terms of Use / Participation Terms
- Intellectual Property & Licensing Policy
- Community / Content / Moderation and Appeal Policy when participation is enabled
- Incident Response / Security Disclosure policy
- Document Preservation / Records policy

These are specifications/policies/operational instruments already implied by the master architecture; they are not additional architectural layers.

## 8. Priority

**P0:** hierarchy, canonical names, status semantics, realm/space/layer mapping, source-of-truth model, Charter/Pact/Manifesto normative status.

**P1:** privacy/controller model, terms, IP/licensing, moderation/appeal, identity status, security evidence, accessibility baseline.

**P2:** AI deployment governance, jurisdiction matrix, token/payment legal boundary, data inventory, metrics and impact methodology.

## 9. Final assessment

The project does not need another conceptual architecture. It needs a controlled reconciliation baseline. The existing material is sufficiently rich to derive the website structure.

The next authoritative artifact should be **Site Master Structure & Page Template Specification**, derived from the existing Registry, Master Architecture, Technical Architecture, UX baselines and document hierarchy. It must describe the website as a projection of the existing architecture, not create a competing architecture.
