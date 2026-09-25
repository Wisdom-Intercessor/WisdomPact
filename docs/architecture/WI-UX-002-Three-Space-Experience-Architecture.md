# WI-UX-002 — Three-Space Experience Architecture

**Status:** Final baseline  
**Version:** 1.0.0  
**Date:** 2026-09-25

## Experience map

```text
                 Eternal Wisdom Charter
                    رستاخیز حکمت
                         │
                     Gateway
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
        عالم کبری     دیوان حکمت   WisdomCore
      Cosmic Realm    Wisdom Divan  Personal Core
             │           │           │
       world/time     8 Halls     8 service layers
       space/place    governance   tools/services
             │           │           │
             └───────────┼───────────┘
                         │
                    WisdomSpace
                 Personal Showcase
```

## Cosmic Realm

The Cosmic Realm is the primary world-facing interface. It begins at cosmic scale and allows progressive focus toward Earth and geographic detail.

The mature target includes:

- animated Earth
- orbital/cosmic context
- zoom and focus
- temporal controls
- geographic context
- live data layers
- environmental context
- a visible gateway into the Wisdom System

## Wisdom Divan

The Divan is the central governance surface. Its eight halls are:

| Hall | Domain |
|---|---|
| WisdomNetwork | communication and connection |
| WisdomChain | exchange and value infrastructure |
| WisdomTreasury | resources and wealth |
| WisdomKnowledge | knowledge, science and creation |
| WisdomGuard | security and protection |
| Governance & Justice | governance, law and justice |
| WisdomLife & Health | life and health |
| Wisdom of Existence & Time | existence, memory and time |

## WisdomCore

WisdomCore is the participant's operational center. Its eight service/tool domains map to the same broad concerns but serve a different function from the Divan.

The Core must support:

- personal tasks
- learning and knowledge work
- resources and assets
- economic activity
- security
- participation and governance
- life and health workflows
- time, memory and long-term planning

## WisdomSpace

WisdomSpace is the participant-owned interactive presence inside the Core.

It should allow a member to move from private workspace to public or selectively shared showcase without creating a separate architectural universe.

## UX rule

The user should experience the system as one connected world, while the implementation remains modular:

**World → Governance → Personal Agency → Personal/Community Presence**

## Implementation boundary

The current WordPress implementation establishes the navigation and visual shells. Real-time planetary rendering, live data, advanced 3D interaction, identity infrastructure and service backends are separate implementation concerns and must attach to these stable experience contracts.

