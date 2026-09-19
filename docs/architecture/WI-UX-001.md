# WI-UX-001 — Outdoor / Indoor / WisdomSpace Experience Architecture

**Project:** WisdomIntercessor  
**Repository:** Wisdom-Intercessor/WisdomPact  
**Document ID:** WI-UX-001  
**Version:** 0.1.0  
**Status:** Draft  
**Language priority:** Persian-first; English-aligned  
**Authority:** Controlled architecture document under WI-MR-001 and WI-MA-001

## 1. Purpose

This document defines the experience architecture for the WisdomIntercessor website and future ecosystem interfaces.

It establishes the relationship between the three primary experience modes:

- Outdoor — the living public/Genesis experience.
- Indoor — the operational/dashboard experience.
- WisdomSpace — participant-specific working and contribution space.

This document defines experience boundaries, navigation logic, interaction principles, and release constraints. It does not replace visual design specifications.

## 2. Experience principles

1. The interface must communicate WisdomIntercessor as an ecosystem and civilizational project, not as an ordinary blog.
2. The Genesis experience should invite participation without falsely implying that the ecosystem is already fully operational.
3. Symbolic elements must support orientation and meaning rather than obscure basic usability.
4. Users must understand what is concept, service, and product.
5. Primary actions must be visible and comprehensible.
6. Persian is the primary interface language; English is a parallel experience.
7. Outdoor, Indoor, and WisdomSpace are modes of the same ecosystem, not unrelated websites.
8. The interface must progressively disclose complexity.

## 3. Outdoor experience

The Outdoor mode is the public threshold and Genesis environment of WisdomIntercessor.

Its conceptual visual language includes:

- Tree of Wisdom;
- grave and the Wisdom Treasury / گنجینه حکمت beneath or associated with it;
- lions;
- phoenix;
- small hill/landscape;
- portal representation;
- living environmental and temporal background.

These elements are symbolic experience components. They must not prevent normal navigation, accessibility, performance, or content discovery.

## 4. Outdoor interaction hierarchy

The Outdoor mode should establish this general sequence:

1. Recognition of WisdomIntercessor.
2. Genesis declaration / invitation.
3. Explanation of the central purpose at a concise level.
4. Primary participation action: «پیوستن به حکمت».
5. Access to foundational documents.
6. Review/acceptance of the applicable Charter/Pact and participation terms where required.
7. Appearance or activation of the Wisdom Portal according to the actual implementation state.
8. Choice between creating/using Wisdom ID and entering the operational ecosystem when those capabilities are available.

The interface must never imply that an unavailable capability is already active.

## 5. Grave and Wisdom Treasury

The grave is a symbolic access point for foundational knowledge, not the sole entry mechanism.

Interaction should provide access to:

- foundational charter/pact material;
- controlled project documents;
- the Wisdom Treasury / گنجینه حکمت;
- historical/versioned project records where appropriate.

The grave itself must not be represented as a technical authentication mechanism.

## 6. Portal logic

The portal is an experience metaphor for transition from the public Genesis environment into the ecosystem.

A portal may expose:

- create Wisdom ID;
- enter عالم صغری / WisdomIntercessor;
- access available services;
- view current ecosystem status.

The portal must be state-aware. If identity, dashboard, wallet, governance, or other functionality is not implemented, the interface must label it as planned, unavailable, or coming soon rather than simulate completion.

## 7. Indoor experience

Indoor is the operational visual environment.

Its visual language is conceptually informed by:

- تخت جمشید / collective governance;
- جام جم / resources and collective wealth;
- structured spaces for governance, knowledge, life, protection, and participation.

Indoor navigation should provide a comprehensible representation of the active ecosystem layers rather than a decorative collection of symbols.

## 8. Layer navigation

The Indoor experience should expose the logical architecture progressively:

Layer 0 — WisdomCore  
Layer 1 — WisdomNetwork / WisdomHub  
Layer 2 — WisdomChain  
Layer 3 — WisdomTreasury / جام جم  
Layer 4 — WisdomKnowledge / WisdomPlay  
Layer 5 — WisdomGuard  
Layer 6 — WisdomGovernance & Justice / تخت حکمت  
Layer 7 — WisdomLife  
Layer 8 — WisdomExistence & Time

Unavailable functions must have a clear state.

## 9. WisdomSpace

WisdomSpace is the participant-oriented workspace layer.

A participant may have:

- personal desk/workspace;
- profile and identity controls;
- showcase/portfolio;
- authored content;
- products or offerings where applicable;
- contribution history;
- collaboration and participation tools.

The experience should support different participant types without forcing every participant into a commercial marketplace model.

Examples include artisans, writers, researchers, artists, musicians, designers, programmers, educators, and community contributors.

## 10. Direct participation

The experience should support direct production, presentation, discovery, exchange, and collaboration where the corresponding services are implemented.

Intermediaries should not be assumed as mandatory architectural actors.

However, direct participation does not remove the need for:

- moderation;
- safety controls;
- intellectual-property rules;
- transaction controls;
- dispute handling;
- privacy controls;
- applicable legal requirements.

## 11. Wisdom ID

Wisdom ID is the primary conceptual identity entry point.

UX requirements:

- identity status must be visible;
- registration and sign-in must be distinct from general content browsing;
- users must understand what information is public;
- account recovery and security controls must be discoverable;
- a user must not be forced to create an identity merely to read public foundational content unless a documented requirement exists.

## 12. Language switching

The interface is Persian-first.

Language switching must support:

- Persian RTL;
- English LTR;
- persistent user language preference where technically appropriate;
- translation of navigation and interface elements;
- preservation of content meaning and document version identity.

The language switcher may be positioned according to the active directionality, including left/right mirroring, but its behavior must remain consistent.

## 13. Navigation model

Primary navigation should remain shallow.

Recommended top-level experience:

Outdoor:
- Genesis
- Charter / Documents
- About
- Join Wisdom

Indoor:
- Core
- Network
- Chain
- Treasury
- Knowledge
- Guard
- Governance & Justice
- Life
- Existence & Time

WisdomSpace:
- Desk
- Showcase
- Contributions
- Knowledge/Works
- Services/Products where applicable
- Settings / Identity

Actual labels may be refined through usability testing without changing the architectural boundaries.

## 14. Visual system

The current visual direction is Dark Cinematic with controlled symbolic illumination.

The visual system should support:

- strong hierarchy;
- readable Persian typography;
- restrained use of metallic/symbolic visual motifs;
- responsive layouts;
- accessible contrast;
- meaningful animation only;
- reduced-motion behavior.

The Outdoor environment may be visually dynamic, including seasonal/day/time changes, but dynamic effects must not compromise performance or readability.

## 15. Temporal environment

Time-based visual changes may represent:

- day/night;
- season;
- month;
- year;
- longer historical/temporal cycles where appropriate.

The implementation must use deterministic rules based on actual time and relevant location/context rather than arbitrary random changes.

Temporal decoration must not change core content or user data.

## 16. Responsive behavior

The experience must be designed for:

- mobile;
- tablet;
- desktop.

Symbolic scenes must degrade gracefully on smaller screens.

Critical actions must remain usable without hover, pointer precision, large screens, or animation.

## 17. Accessibility

Minimum requirements include:

- keyboard access;
- semantic headings and landmarks;
- accessible labels;
- sufficient contrast;
- focus visibility;
- text alternatives for meaningful visual elements;
- reduced-motion support;
- no critical information conveyed only through animation or color.

## 18. State design

Every major experience component should define at least:

- available;
- unavailable;
- planned;
- coming soon;
- loading;
- empty;
- error;
- restricted.

The interface must not present a mock capability as a functioning service.

## 19. Content architecture

The experience should distinguish:

- Genesis/public narrative;
- foundational documents;
- project architecture;
- active services;
- products/offerings;
- participant content;
- system status.

Content status should be visible where necessary: draft, review, approved, superseded, archived, or deprecated.

## 20. WordPress implementation boundary

The initial WordPress implementation may host the Outdoor and public content experience and the initial Indoor shell.

Interactive ecosystem capabilities should be introduced only when their underlying technical services exist.

Theme, plugin, custom-code, and external-service choices must be recorded separately from this UX architecture.

## 21. Performance

The Outdoor visual experience must be optimized for practical web delivery.

Requirements include:

- compressed media;
- lazy loading where appropriate;
- minimized blocking scripts;
- graceful fallback when rich visual effects cannot load;
- mobile-conscious asset sizes;
- no unnecessary autoplay media.

## 22. UX acceptance criteria

The draft UX architecture is acceptable as a baseline when:

- Outdoor, Indoor, and WisdomSpace have distinct purposes;
- the user journey from Genesis to participation is understandable;
- symbolic elements do not replace functional navigation;
- unavailable functions are clearly represented;
- Persian RTL and English LTR are both supported;
- Wisdom ID has a defined UX role;
- participant desks/showcases are represented without assuming every contribution is a product;
- accessibility and responsive requirements are explicit.

## 23. Change control

Changes must follow WI-MR-001.

Visual mockups, theme changes, WordPress configuration, and production publication do not automatically change this architectural document.

**End of WI-UX-001 — Draft v0.1.0**
