# WQIE Relation Registry v0.2
**Status:** Draft · **Version:** 0.2 · **Applies to:** Eternal Wisdom Charter / WQIE

## 1. Normative conventions
- IDs are stable and never recycled. A retired relation type remains resolvable and is marked deprecated.
- A relation type describes the meaning of a link, not whether a particular link is true.
- Direction is semantic: `source → target`. Inverse relations must be explicitly registered; do not infer an inverse by reversing an edge.
- Every assertion instance records provenance, evidence class, confidence/uncertainty, temporal scope, and review state.
- `unknown`, `not_applicable`, and `no_relation_established` are distinct.
- Numeric scores require documented scales, calibration, method, and sensitivity analysis. No universal composite score is defined.
- Causal types require causal reasoning/design; correlation is never silently promoted to causation.
- Legal relations require jurisdiction and effective dates. Normative relations require an explicit value/principle basis.

## 2. Relation type registry

| ID | Type | Meaning / use | Default direction | Inverse or paired interpretation |
|---|---|---|---|---|
| R-FND-001 | defines | Source supplies an operational or conceptual definition of target | directed | defined-by |
| R-FND-002 | grounds | Source is a stated foundation for target | directed | grounded-in |
| R-FND-003 | constitutes | Source is a constitutive component/condition of target | directed | constituted-by |
| R-EPI-001 | supports-evidence | Evidence/source supports a claim to a stated degree | directed | supported-by-evidence |
| R-EPI-002 | contradicts-evidence | Evidence/source challenges a claim | directed | challenged-by-evidence |
| R-EPI-003 | qualifies | Source narrows the scope or conditions of target | directed | qualified-by |
| R-EPI-004 | depends-on-source | Claim depends on a source, dataset, or method | directed | source-for |
| R-EPI-005 | uncertain-about | Evidence/claim explicitly identifies uncertainty about target | directed | uncertainty-recorded-by |
| R-LOG-001 | entails | Under stated premises, source logically entails target | directed | entailed-by |
| R-LOG-002 | requires-condition | Source requires target as a necessary condition | directed | required-by |
| R-LOG-003 | sufficient-condition-for | Source is sufficient for target under explicit assumptions | directed | has-sufficient-condition |
| R-LOG-004 | incompatible-with | Source and target cannot both hold under the same stated interpretation/context | symmetric | incompatible-with |
| R-CAU-001 | causes | Source is established as a cause of target under a stated causal model | directed | caused-by |
| R-CAU-002 | contributes-to | Source is a contributing causal factor for target | directed | receives-contribution-from |
| R-CAU-003 | mediates | Source is a mediator on a specified causal path | directed/path role | mediated-by |
| R-CAU-004 | moderates | Source changes the magnitude/direction of another causal relation | contextual | moderated-by |
| R-CAU-005 | prevents | Source causally reduces/prevents target under defined conditions | directed | prevented-by |
| R-NOR-001 | supports-value | Source supports an explicitly named normative value in target | directed | value-supported-by |
| R-NOR-002 | conflicts-value | Source conflicts with a named normative value in target | directed/contextual | value-conflicted-by |
| R-NOR-003 | imposes-duty | Source establishes/grounds a duty borne by target actor | directed | duty-grounded-in |
| R-NOR-004 | protects-right | Source protects a specified right of target | directed | right-protected-by |
| R-NOR-005 | affects-right | Source has an assessed impact on a specified right | directed | right-affected-by |
| R-NOR-006 | legitimacy-condition | Source is a stated condition for legitimacy of target | directed | legitimacy-conditioned-by |
| R-LEG-001 | regulates | Legal instrument/rule governs target within jurisdiction/time | directed | regulated-by |
| R-LEG-002 | authorizes | Legal rule authorizes target action/actor | directed | authorized-by |
| R-LEG-003 | prohibits | Legal rule prohibits target action | directed | prohibited-by |
| R-LEG-004 | provides-remedy | Legal mechanism provides remedy for target violation/harm | directed | remedied-by |
| R-ECO-001 | allocates-resource | Source allocates a resource to target | directed | receives-allocation-from |
| R-ECO-002 | transfers-value | Value/resource transfer from source to target | directed | receives-transfer-from |
| R-ECO-003 | creates-incentive | Source creates an incentive affecting target | directed | incentivized-by |
| R-ECO-004 | creates-externality | Source creates an external effect borne by target | directed | bears-externality-from |
| R-SOC-001 | affects-group | Source affects a specified social group represented by target | directed | affected-by |
| R-SOC-002 | enables-participation | Source enables participation by target | directed | participation-enabled-by |
| R-SOC-003 | builds-trust | Source contributes to trust in target, with evidence/context | directed | trust-supported-by |
| R-TEC-001 | interoperates-with | Systems exchange/interpret data or services under a defined interface | usually symmetric | interoperates-with |
| R-TEC-002 | depends-technically-on | Source requires target for operation | directed | technical-dependency-of |
| R-TEC-003 | interfaces-with | Source has a specified interface to target | directed or symmetric | interface-counterpart |
| R-TEC-004 | failure-propagates-to | Failure in source can propagate to target | directed | exposed-to-propagation-from |
| R-ECOG-001 | impacts-ecosystem | Source produces an ecological effect on target | directed | impacted-by |
| R-ECOG-002 | transfers-material-flow | Material/energy/resource flow from source to target | directed | receives-material-flow-from |
| R-ECOG-003 | affects-resilience | Source changes resilience of target | directed | resilience-affected-by |
| R-X-001 | synergizes-with | Joint interaction yields a documented benefit beyond isolated effects | contextual/symmetric | synergizes-with |
| R-X-002 | conflicts-with | Source and target create an evidenced practical conflict | contextual/symmetric | conflicts-with |
| R-X-003 | trades-off-with | Improvement in one dimension entails a cost in another under stated conditions | contextual/symmetric | trades-off-with |
| R-X-004 | depends-on | Source requires target for a specified function/outcome | directed | dependency-of |
| R-X-005 | feeds-back-to | Effects of source return to influence target | directed/loop | receives-feedback-from |
| R-X-006 | transforms-into | Source transitions into target under specified mechanism | directed | transforms-from |
| R-X-007 | measured-by | Source/property is assessed using target indicator/method | directed | measures |
| R-X-008 | co-determined-with | Two or more factors jointly determine an outcome; prefer hyperedge if 3+ | contextual | co-determined-with |

**Important:** the “inverse” column gives a reading aid, not an automatically generated edge. Store one canonical directed assertion unless the inverse itself is independently meaningful and supported.

## 3. Evidence classes
- `EMPIRICAL-OBSERVATION`: measured or observed data.
- `EXPERIMENTAL`: controlled experimental evidence.
- `QUASI-EXPERIMENTAL`: natural experiment or quasi-experimental design.
- `CAUSAL-INFERENCE`: explicit causal identification strategy and assumptions.
- `SYSTEMATIC-REVIEW`: systematic synthesis with search and inclusion method.
- `THEORETICAL-MODEL`: formal or explanatory model, assumptions disclosed.
- `LOGICAL-ARGUMENT`: proof or explicit inference.
- `PHILOSOPHICAL-ARGUMENT`: conceptual/ontological/epistemological argument.
- `NORMATIVE-JUSTIFICATION`: ethical or political justification with value premises.
- `LEGAL-AUTHORITY`: primary legal text/case/official interpretation, jurisdiction/date.
- `HISTORICAL-RECORD`: archival or historical evidence.
- `EXPERT-ELICITATION`: structured expert judgment, method and panel limits.
- `STAKEHOLDER-TESTIMONY`: situated experience/testimony; consent and privacy apply.
- `UNVERIFIED-ASSERTION`: recorded claim awaiting validation; not treated as evidence.

## 4. Review and assertion states
`DRAFT`, `PROPOSED`, `EVIDENCE-REVIEW`, `CONTESTED`, `ACCEPTED-WORKING`, `REJECTED`, `EXPIRED`, `SUPERSEDED`, `WITHDRAWN`.
These are workflow states, not binary truth labels. “Accepted-working” is provisional and must carry a review date/trigger.

## 5. Impact dimensions
`HUMAN`, `RIGHTS`, `HEALTH`, `SOCIAL`, `GOVERNANCE`, `ECONOMIC`, `CULTURAL`, `TECHNOLOGICAL`, `SECURITY`, `ECOLOGICAL`, `INTERGENERATIONAL`, `GLOBAL`, `SPIRITUAL-EXISTENTIAL`.
Multiple dimensions may apply. Do not infer a common scale across them.

## 6. Confidence and uncertainty policy
Confidence is an assessor's calibrated judgment about a specific assertion, not a universal probability unless calibration supports probabilistic interpretation. Evidence quality is recorded separately. Uncertainty should identify type (measurement, sampling, model, causal, interpretive, legal, temporal, value disagreement, missing evidence), range/alternatives where possible, and what would reduce it. Unknown is not zero.

## 7. Hyperedge policy
Use a hyperedge when the proposition depends on a joint configuration of three or more members, roles, or conditions and pairwise links would lose essential meaning. Record member roles (actor, affected party, condition, mechanism, outcome, context), joint statement, conditions, evidence, uncertainty, and time. Document why pairwise decomposition is inadequate.

## 8. Example assertions (illustrative; not empirical findings)
- A draft AI procurement policy **R-LEG-001 regulates** an AI procurement process only after its jurisdiction and effective date are supplied.
- An independently reviewed study may **R-EPI-001 support-evidence** a narrowly scoped claim; it does not automatically establish a universal rule.
- A proposed automated decision system may **R-NOR-005 affect-right** to explanation or appeal; the assessment must identify the right basis, affected people, and evidence.
- A multi-domain AI deployment involving rights, education, labor, security, environment, and governance may warrant a hyperedge if the joint configuration matters.

## 9. Change control
New types require a proposal, duplicate check, definition, scope, direction, inverse policy, examples, validation rules, and review. Do not silently redefine an existing ID. Changes that alter semantics require a new ID or major version and migration note.
