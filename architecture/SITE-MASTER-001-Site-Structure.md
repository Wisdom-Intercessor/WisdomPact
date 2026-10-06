# SITE-MASTER-001 — wisdomintercessor.com Site Master Structure

Status: STRUCTURE-ONLY / page specifications pending
Version: 0.1-draft

## Navigation spine
1. Genesis / فرا دستی — gateway, Wisdom Pact vault, membership/login gateway
2. عالم کبری — living cosmic/earth gateway and time-space context
3. عالم صغری — دیوان حکمت / eight connecting halls
4. عالِم صغری — WisdomIntercessor / WisdomCore personal and ecosystem control plane
5. Wisdom Architecture — Layer 0 + eight operational layers
6. Wisdom Pact / Charter — foundational declaration and critique gateway
7. Documents — governed document vault
8. Community / Participation — contribution, critique, collaboration

## Page template contract
Every major page must contain:
- stable page ID / slug
- purpose and scope
- relationship to the three realms
- relationship to Wisdom Pact principles
- layer/product references where applicable
- primary action and next destination
- document/specification status
- accessibility and bilingual metadata
- no dead-end navigation

## Realm model
- Inner / عالِم صغری: human, wisdom, agency and personal governance
- Outer / عالم کبری: cosmos, Earth, environment and lived reality
- Connecting / عالم صغری: digital realm that connects human and cosmos

## Layer navigation
Each layer page is a container for registered products. Product pages must be generated from registry records, not invented ad hoc.

## Placeholder policy
The architecture, navigation and page slots may be implemented before the detailed documents are finalized. Empty specification panels must visibly state that the document is pending and must not imply implementation or legal status.

## Primary page slots
| ID | Page | State |
|---|---|---|
| SITE-001 | Genesis / فرا دستی | STRUCTURE |
| SITE-002 | عالم کبری | EXISTING / ALIGNMENT REQUIRED |
| SITE-003 | عالم صغری / دیوان حکمت | STRUCTURE |
| SITE-004 | عالِم صغری / WisdomCore | STRUCTURE |
| SITE-005 | Wisdom Architecture | STRUCTURE |
| SITE-006 | Wisdom Pact | EXISTING / ALIGNMENT REQUIRED |
| SITE-007 | Document Vault | STRUCTURE |
| SITE-008 | Community / Participation | STRUCTURE |

## Technical boundary
Current WordPress remains the presentation/application origin. GitHub is the source-of-truth for architecture/specification/versioning. Cloudflare remains the edge layer (DNS/CDN/WAF and future deployment integration where technically justified). Do not move the WordPress frontend to Pages/Workers merely because Git integration exists.
