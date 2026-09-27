# Wisdom Intercessor — GitHub Ecosystem Architecture

## 1. Purpose

The GitHub ecosystem is governed from **WisdomPact**.

The architecture deliberately separates **Repository, Project, Organization, Product, Service, Module, Protocol, and Concept**. Not every ecosystem entity becomes a GitHub repository.

The purpose of this model is to preserve a small, stable strategic repository structure while allowing the ecosystem to grow without unnecessary repository fragmentation.

## 2. Master structure

```
                    WISDOMPACT
              Repository / Mother Document
              Eternal Wisdom Charter
                       |
          +------------+-------------+
          |                          |
          v                          v
Eternal Wisdom Foundation    WisdomIntercessor.com
       Organization                  Project
          |                          |
          |                    +-----+-----+
          |                    |           |
          v                    v           v
   Institutional          Products      Services
   repositories           Modules       Components
                          Protocols
```

**WisdomPact** is the supra-level repository and documentary root.

**Eternal Wisdom Foundation** is an organizational entity, not automatically a repository.

**WisdomIntercessor.com** is the principal digital project.

Other ecosystem names are classified through the Master Registry before any decision to create an independent repository.

## 3. Entity classification

| Entity | Current type | Role |
|---|---|---|
| **WisdomPact** | Supra Repository / Mother Document | Eternal Wisdom Charter, principles, master registry, architecture and cross-ecosystem governance |
| **WisdomIntercessor.com** | Project | Principal digital project and public ecosystem implementation |
| **Eternal Wisdom Foundation** | Organization | Institutional stewardship, research, preservation and long-term continuity |
| **WisdomChain** | Protocol / Project Candidate | Chain, verifiable records, coordination and related infrastructure |
| **WisdomID** | Service / Infrastructure Candidate | Identity, authentication, authorization, consent and interoperability |
| **WisdomCore** | Module / Product Candidate | Operational core, personal/work environment and orchestration |
| **WisdomAI** | Service / Product Candidate | AI and collective-intelligence capabilities |
| **WisdomTreasury** | Domain / Service Candidate | Treasury, resources and economic mechanisms |
| **WisdomKnowledge** | Domain / Product Candidate | Knowledge, science, technology and knowledge memory |
| **Jame Jam-e Hikmat** | Domain / Product Candidate | Collective knowledge, memory, resources and panoramic/world-state views |
| **Takht-e Hokmrani-e Hikmat** | Governance Domain / Product Candidate | Governance, deliberation, justice, accountability and decision processes |

These classifications are subject to the Master Registry and may evolve through documented architectural decisions.

## 4. Repository policy

A new independent repository should be created only when there is a documented need for independent:

- development lifecycle;
- ownership or stewardship;
- security/data boundary;
- deployment lifecycle;
- issue/project management;
- access-control boundary;
- release/versioning boundary; or
- community/contributor boundary.

A concept, product, service, module or domain does **not** become a repository merely because it has a name or specification.

This prevents repository inflation while preserving the ability to split a mature component into an independent repository when justified.

## 5. WisdomPact — supra repository

**WisdomPact** owns the documentary and normative root of the ecosystem:

- Eternal Wisdom Charter / Wisdom Pact;
- Master Registry;
- foundational policies;
- master architecture;
- repository and project governance rules;
- architectural decisions (ADRs);
- cross-ecosystem standards;
- canonical terminology;
- document-control rules.

WisdomPact does not automatically own production application code, user identity databases, AI runtimes, financial assets, production wallets, or operational secrets.

## 6. WisdomIntercessor.com — principal project

**WisdomIntercessor.com** is the principal digital project of the Wisdom Intercessor ecosystem.

Its scope may include:

- public website and digital gateway;
- Genesis / Charter gateway;
- Cosmic Realm;
- Wisdom Divan;
- public-facing WisdomCore entry;
- public documentation presentation;
- integrations with ecosystem services and modules.

Its internal components do not automatically require separate repositories.

## 7. Eternal Wisdom Foundation — organization

**Eternal Wisdom Foundation** is an institutional organization responsible, where formally established, for:

- stewardship;
- research and preservation;
- educational and cultural programs;
- institutional continuity;
- archival functions;
- support/grant programs where legally established.

The Foundation may own or maintain repositories and projects, but the organization itself is not synonymous with a repository.

## 8. Strategic domains

The following domains are retained as important architectural entities but are **not automatically independent repositories**:

### WisdomChain
Protocol and coordination domain, including verifiable records and approved chain integrations.

### WisdomID
Identity and access domain, including authentication, authorization, consent and interoperability.

### WisdomCore
Operational core and participant workspace domain.

### WisdomAI
AI, reasoning support and collective-intelligence domain.

### WisdomTreasury
Resource, treasury and economic-governance domain.

### WisdomKnowledge
Knowledge, science, technology and knowledge-memory domain.

### Jame Jam-e Hikmat
Collective knowledge, memory, resource representation and panoramic/world-state domain.

### Takht-e Hokmrani-e Hikmat
Governance, deliberation, justice, accountability and decision-process domain.

Each may later be promoted to an independent repository if the Repository Policy criteria are satisfied.

## 9. Authority model

The dependency direction is:

`Charter → Principles → Policies → Architecture → Entity Specifications → Implementations`

WisdomPact is the normative and documentary source. It does not become a software dependency of every implementation.

If an implementation requirement conflicts with the Charter or master architecture, the conflict must be documented through an ADR or Charter amendment proposal before becoming a baseline.

## 10. Change propagation

A change originating in WisdomPact follows:

`WisdomPact → Registry/ADR → affected project/entity specification → implementation → validation → deployment`

A change originating in an implementation follows:

`Implementation proposal → impact analysis → project/entity review → WisdomPact review when normative or cross-domain → implementation`

A Git commit is not equivalent to Charter approval, public deployment, governance activation, financial activation, or production release.

## 11. Repository creation rule

The Master Registry must contain an approved classification and justification before a new strategic repository is created.

Therefore:

**No additional repository is currently required solely because an ecosystem concept or product has its own document.**

The existing 52 ecosystem documents will be classified through the Master Registry rather than converted automatically into repositories.

## 12. Current strategic GitHub model

The intended strategic model is:

1. **WisdomPact** — supra repository / mother document
2. **WisdomIntercessor.com** — principal project
3. **Eternal Wisdom Foundation** — organization
4. **WisdomChain** — strategic protocol/project candidate
5. **WisdomID** — strategic identity/service candidate
6. **WisdomCore** — strategic operational-core candidate
7. **WisdomAI** — strategic intelligence candidate
8. **WisdomTreasury** — strategic economic-resource candidate
9. **WisdomKnowledge** — strategic knowledge candidate

Items 4–9 are architectural entities and strategic candidates; they are not declared existing GitHub repositories until independently approved and created.

## 13. Current GitHub reality

At the time of this document revision, the connected GitHub account confirms **WisdomPact** as an existing repository.

No claim is made that the other entities have already been created as repositories.

Repository creation, organizational setup and project configuration will be performed separately and explicitly.

## 14. Governing principle

> **Everything in the Wisdom Intercessor ecosystem does not need to become a repository.**

GitHub repositories are implementation and collaboration boundaries. The ecosystem architecture is broader than its repository structure.

The **Master Registry** is the authoritative place for deciding what each entity is, where it belongs, and whether it requires an independent repository.
