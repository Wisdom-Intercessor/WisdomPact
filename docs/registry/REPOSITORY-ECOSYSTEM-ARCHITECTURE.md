# Wisdom Intercessor — GitHub Repository Ecosystem

## 1. Purpose

The GitHub ecosystem is governed from the **WisdomPact** repository.

WisdomPact is the supra-structural repository: it contains the Eternal Wisdom Charter, the foundational principles, repository governance rules, architectural decisions, and the master registry that defines how the other repositories serve the Charter.

The other repositories are implementation, infrastructure, institutional, identity, intelligence, economic, governance, and operational domains. None of them supersedes the Charter.

## 2. Repository hierarchy

```
                         WISDOM PACT
              Eternal Wisdom Charter / Wisdom Pact
                         (SUPRA)
                              |
       +----------------------+----------------------+
       |                      |                      |
       v                      v                      v
 WisdomIntercessor.com  EternalWisdomFoundation  WisdomCore
 Digital Infrastructure Institutional Stewardship Operational Core
       |                      |                      |
       +----------+-----------+----------+-----------+
                  |                      |
                  v                      v
              WisdomID                WisdomAI
              Identity              Intelligence
                  |                      |
                  +----------+-----------+
                             |
          +------------------+------------------+
          |                  |                 |
          v                  v                 v
     WisdomChain        WisdomTreasury   Jam & Takht-e Hikmat
     Coordination/      Economic         Governance & Justice
     Verification       Resources        Governance Domain
```

## 3. Controlled repository set

| # | Repository | Role | Relationship to WisdomPact |
|---|---|---|---|
| 0 | **WisdomPact** | Supreme charter, principles, document control, master architecture and repository governance | Parent / normative source |
| 1 | **WisdomIntercessor.com** | Public digital infrastructure and user-facing website/ecosystem gateway | Implements approved public-facing requirements |
| 2 | **EternalWisdomFoundation** | Institutional stewardship, research, grants, preservation and long-term continuity | Institutional implementation of Charter mission |
| 3 | **WisdomCore** | Personal/operational core, dashboards, services and orchestration | Core implementation domain |
| 4 | **WisdomID** | Identity, account, permissions, consent and interoperability | Identity infrastructure |
| 5 | **WisdomAI** | AI, collective-intelligence and wisdom-support capabilities | Intelligence infrastructure |
| 6 | **WisdomChain** | Verifiable coordination, records, protocols and value-transfer infrastructure | Technical/economic protocol domain |
| 7 | **WisdomTreasury** | Treasury, resource accounting, incentives and economic governance infrastructure | Economic-resource domain |
| 8 | **Jam & Takht-e Hikmat** | Governance and justice domain: Jam (collective resources) + Takht-e Hikmat (wisdom governance) | Governance implementation domain |

### Repository 8 — Jam & Takht-e Hikmat

**Jam & Takht-e Hikmat** is the dedicated governance-domain repository for the two complementary institutional concepts:

- **Jam (جام):** collective resources, shared assets, common wealth/resource coordination and transparent stewardship interfaces.
- **Takht-e Hikmat (تخت حکمت):** wisdom-centered governance, deliberation, decision records, justice mechanisms, institutional rules and governance processes.

This repository does not replace **WisdomTreasury**. WisdomTreasury owns the economic/treasury infrastructure; Jam & Takht-e Hikmat owns the governance layer that defines how collective resources and governance decisions are deliberated, recorded, reviewed and administered.

It also does not replace **WisdomPact**. The Charter remains the normative source. Jam & Takht-e Hikmat implements approved governance requirements under the Charter.

## 4. Authority model

**WisdomPact does not become a software dependency of every repository.** It is the normative and documentary root.

The dependency direction is:

`Charter → Principles → Policies → Architecture → Repository Specifications → Implementations`

No implementation repository may silently redefine a Charter principle.

If an implementation requirement conflicts with the Charter, the conflict must be recorded as an architectural decision or Charter amendment proposal before it is treated as a baseline.

## 5. Repository boundaries

### WisdomPact
Owns:
- Eternal Wisdom Charter / Wisdom Pact
- Master Registry
- foundational policies
- architecture principles
- repository governance
- ADRs
- cross-repository standards
- canonical terminology

Does not own:
- production website code
- user identity database
- AI runtime
- financial assets
- production wallets
- operational secrets

### WisdomIntercessor.com
Owns:
- public website
- public content delivery
- Genesis / Charter gateway
- Cosmic Realm / Wisdom Divan / WisdomCore entry surfaces
- public documentation presentation
- integration layer for public services

### EternalWisdomFoundation
Owns:
- institutional stewardship
- research and preservation
- educational and cultural programs
- grants/support programs when legally established
- continuity and archival functions

### WisdomCore
Owns:
- personal/workspace core
- operational orchestration
- service dashboard
- participant workspace integration
- cross-domain user experience

### WisdomID
Owns:
- identity
- authentication/authorization interfaces
- consent
- profile and account interoperability
- identity lifecycle specifications

### WisdomAI
Owns:
- AI services
- reasoning/knowledge-support components
- collective wisdom tooling
- AI safety and evaluation specifications

### WisdomChain
Owns:
- protocol-level coordination
- verifiable records
- chain integrations
- smart-contract/protocol specifications where approved

### WisdomTreasury
Owns:
- treasury architecture
- resource accounting
- economic policies
- incentives and allocation mechanisms
- financial controls and audit interfaces

### Jam & Takht-e Hikmat
Owns:
- governance architecture and operating rules
- deliberation and decision-making processes
- justice and dispute-resolution specifications
- governance records and decision provenance
- collective-resource governance interfaces
- institutional role and authority models
- governance integration with WisdomTreasury and WisdomChain

Does not own:
- the normative Charter
- the treasury's underlying financial infrastructure
- identity infrastructure
- the public website as a whole

## 6. Cross-repository rule

Every repository must contain a `GOVERNANCE.md` or equivalent document identifying:

1. its purpose;
2. its scope;
3. its dependencies on WisdomPact;
4. the applicable Charter principles;
5. its owner/maintainer model;
6. security and data boundaries;
7. release policy;
8. the process for proposing changes that affect another repository.

For **Jam & Takht-e Hikmat**, cross-repository governance must explicitly define interfaces with:
- WisdomPact;
- WisdomTreasury;
- WisdomChain;
- WisdomID;
- WisdomCore;
- WisdomIntercessor.com.

## 7. Change propagation

A change originating in WisdomPact follows:

`WisdomPact → Registry/ADR → affected repository specification → implementation → validation → public deployment`

A change originating in an implementation repository follows:

`Implementation proposal → impact analysis → repository review → WisdomPact/ADR review when normative or cross-domain → implementation`

Git commits are not equivalent to Charter approval, public deployment, governance activation, financial activation, or production release.

## 8. Naming

The official master project name is **Wisdom Intercessor**.

The foundational document is **Eternal Wisdom Charter**, with the short name **Wisdom Pact**.

The governance repository's working English identifier is **Jam-and-Takht-e-Hikmat**. Its human-readable Persian title is **جام و تخت حکمت**.

Repository names use stable technical identifiers and should not introduce competing master brands.

## 9. Current state

At the time of this specification, only `WisdomPact` is confirmed as an existing repository in the connected GitHub account.

The remaining repositories are therefore **planned repository targets**, including **Jam-and-Takht-e-Hikmat**, not yet represented as existing repositories.

Creation and initialization should proceed one repository at a time after this registry is approved.
