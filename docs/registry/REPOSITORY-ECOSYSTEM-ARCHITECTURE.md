# Wisdom Intercessor — GitHub Repository Ecosystem

## 1. Purpose

The GitHub ecosystem is governed from the **WisdomPact** repository.

WisdomPact is the supra-structural repository: it contains the Eternal Wisdom Charter, foundational principles, repository governance rules, architectural decisions, and the master registry that defines how the other repositories serve the Charter.

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
       +---------------------+---------------------+
       |                     |                     |
       v                     v                     v
  WisdomChain          WisdomTreasury       Jam-e Jam-e Hikmat
  Coordination/       Economic Resources    Collective Knowledge/
  Verification                              Resources
                                                   |
                                                   v
                                           Takht-e Hikmat
                                           Wisdom Governance
```

## 3. Controlled repository set

| # | Repository | Persian title | Role | Relationship to WisdomPact |
|---|---|---|---|---|
| 0 | **WisdomPact** | منشور حکمت جاویدان | Supreme charter, principles, document control, master architecture and repository governance | Parent / normative source |
| 1 | **WisdomIntercessor.com** | زیرساخت دیجیتال Wisdom Intercessor | Public digital infrastructure and user-facing website/ecosystem gateway | Public implementation domain |
| 2 | **EternalWisdomFoundation** | بنیاد حکمت جاویدان | Institutional stewardship, research, preservation and long-term continuity | Institutional implementation domain |
| 3 | **WisdomCore** | هسته حکمت | Personal/operational core, dashboards, services and orchestration | Core implementation domain |
| 4 | **WisdomID** | شناسه حکمت | Identity, account, permissions, consent and interoperability | Identity infrastructure |
| 5 | **WisdomAI** | هوش حکمت | AI, collective-intelligence and wisdom-support capabilities | Intelligence infrastructure |
| 6 | **WisdomChain** | زنجیره حکمت | Verifiable coordination, records, protocols and value-transfer infrastructure | Technical/economic protocol domain |
| 7 | **WisdomTreasury** | خزانه حکمت | Treasury, resource accounting, incentives and economic governance infrastructure | Economic-resource domain |
| 8 | **Jame Jam-e Hikmat** | جام جم حکمت | Knowledge, resource, memory and collective-world-view domain inspired by Jām-e Jam | Collective knowledge/resource domain |
| 9 | **Takht-e Hokmrani-e Hikmat** | تخت حکمرانی حکمت | Wisdom-centered governance, deliberation, justice, institutional rules and decision processes | Governance and justice domain |

### Repository 8 — Jame Jam-e Hikmat

**جام جم حکمت — Jame Jam-e Hikmat** is the repository for the collective and panoramic domain of Wisdom Intercessor.

Its scope includes:
- collective knowledge and wisdom records;
- civilization and institutional memory;
- shared resources and their transparent representation;
- collective dashboards and world-state views;
- knowledge/resource discovery and coordination interfaces;
- connections to WisdomKnowledge, WisdomTreasury, WisdomChain and WisdomCore when those domains are implemented.

**Jame Jam-e Hikmat does not own the underlying treasury infrastructure.** WisdomTreasury remains responsible for treasury and economic infrastructure. Jame Jam-e Hikmat provides the collective knowledge/resource view and coordination layer.

### Repository 9 — Takht-e Hokmrani-e Hikmat

**تخت حکمرانی حکمت — Takht-e Hokmrani-e Hikmat** is the dedicated governance and justice repository.

Its scope includes:
- wisdom-centered governance architecture;
- deliberation and decision-making processes;
- governance rules and institutional roles;
- justice and dispute-resolution specifications;
- decision records and provenance;
- accountability and review mechanisms;
- governance interfaces with WisdomPact, WisdomID, WisdomCore, WisdomChain, WisdomTreasury and Jame Jam-e Hikmat.

**Takht-e Hokmrani-e Hikmat does not replace WisdomPact.** The Charter remains the normative source. This repository implements approved governance requirements under the Charter.

## 4. Authority model

**WisdomPact does not become a software dependency of every repository.** It is the normative and documentary root.

The dependency direction is:

`Charter → Principles → Policies → Architecture → Repository Specifications → Implementations`

No implementation repository may silently redefine a Charter principle.

If an implementation requirement conflicts with the Charter, the conflict must be recorded as an architectural decision or Charter amendment proposal before it is treated as a baseline.

## 5. Repository boundaries

### WisdomPact
Owns:
- Eternal Wisdom Charter / Wisdom Pact;
- Master Registry;
- foundational policies;
- architecture principles;
- repository governance;
- ADRs;
- cross-repository standards;
- canonical terminology.

Does not own production application code, user identity databases, AI runtimes, financial assets, production wallets, or operational secrets.

### WisdomIntercessor.com
Owns:
- public website;
- public content delivery;
- Genesis / Charter gateway;
- Cosmic Realm / Wisdom Divan / WisdomCore entry surfaces;
- public documentation presentation;
- integration layer for public services.

### EternalWisdomFoundation
Owns:
- institutional stewardship;
- research and preservation;
- educational and cultural programs;
- legally established grants/support programs;
- continuity and archival functions.

### WisdomCore
Owns:
- personal/workspace core;
- operational orchestration;
- service dashboard;
- participant workspace integration;
- cross-domain user experience.

### WisdomID
Owns:
- identity;
- authentication/authorization interfaces;
- consent;
- profile and account interoperability;
- identity lifecycle specifications.

### WisdomAI
Owns:
- AI services;
- reasoning/knowledge-support components;
- collective wisdom tooling;
- AI safety and evaluation specifications.

### WisdomChain
Owns:
- protocol-level coordination;
- verifiable records;
- chain integrations;
- smart-contract/protocol specifications where approved.

### WisdomTreasury
Owns:
- treasury architecture;
- resource accounting;
- economic policies;
- incentives and allocation mechanisms;
- financial controls and audit interfaces.

### Jame Jam-e Hikmat
Owns:
- collective knowledge/resource views;
- civilization and institutional memory interfaces;
- panoramic/world-state representations;
- collective discovery and coordination surfaces;
- integration of knowledge, memory and resource information.

### Takht-e Hokmrani-e Hikmat
Owns:
- governance architecture and operating rules;
- deliberation and decision-making processes;
- justice and dispute-resolution specifications;
- governance records and decision provenance;
- institutional role and authority models;
- accountability and review mechanisms.

## 6. Cross-repository rule

Every repository must contain a `GOVERNANCE.md` or equivalent document identifying:

1. purpose;
2. scope;
3. dependencies on WisdomPact;
4. applicable Charter principles;
5. owner/maintainer model;
6. security and data boundaries;
7. release policy;
8. process for proposing changes that affect another repository.

Jame Jam-e Hikmat and Takht-e Hokmrani-e Hikmat must explicitly define their interfaces with:
- WisdomPact;
- WisdomCore;
- WisdomID;
- WisdomAI;
- WisdomChain;
- WisdomTreasury;
- WisdomIntercessor.com;
- each other.

## 7. Change propagation

A change originating in WisdomPact follows:

`WisdomPact → Registry/ADR → affected repository specification → implementation → validation → public deployment`

A change originating in an implementation repository follows:

`Implementation proposal → impact analysis → repository review → WisdomPact/ADR review when normative or cross-domain → implementation`

Git commits are not equivalent to Charter approval, public deployment, governance activation, financial activation, or production release.

## 8. Naming

The official master project name is **Wisdom Intercessor**.

The foundational document is **Eternal Wisdom Charter**, with the short name **Wisdom Pact**.

Official repository names:
- **Jame Jam-e Hikmat** — جام جم حکمت
- **Takht-e Hokmrani-e Hikmat** — تخت حکمرانی حکمت

These are independent repositories and must not be merged into a single repository.

## 9. Current state

Only **WisdomPact** is currently confirmed as an existing repository in the connected GitHub account.

The remaining repositories are planned repository targets, including **Jame Jam-e Hikmat** and **Takht-e Hokmrani-e Hikmat**.

No repository deletion or creation has been falsely represented as completed. Repository creation and initialization should proceed one repository at a time after registry approval.
