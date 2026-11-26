# WQIE Validation Protocol v0.3

**Status:** Draft · **Version:** 0.3 · **Applies to:** Eternal Wisdom Charter / WQIE  
**Depends on:** `docs/standards/WQIE-relation-registry-v0.2.md` and `schemas/wqie-record-v0.2.schema.json`

## 1. Purpose and validation layers

WQIE validation is a quality-control process for structured assertions. Passing validation does not establish that a claim is true, legitimate, fair, or sufficiently evidenced.

Validation has three distinct layers:

1. **Syntax validation:** the file parses as JSON.
2. **Schema validation:** each record conforms to JSON Schema Draft 2020-12.
3. **Semantic validation:** cross-field, registry, graph-integrity, evidence, temporal, and governance rules are checked by application logic.

A record must not be described as fully conformant when only JSON parsing has succeeded.

## 2. Required validation sequence

1. Parse the JSON document and reject duplicate object keys where the implementation supports detection.
2. Load the exact schema version identified by the test run; pin the validator implementation and version.
3. Validate each fixture against Draft 2020-12. Enable format assertion for `date-time`; do not assume every validator asserts formats by default.
4. Run semantic checks in Section 3.
5. Produce a machine-readable report containing fixture ID, schema result, semantic result, error codes, validator/version, schema digest, and test timestamp.
6. Preserve the test corpus and report with the release candidate.

## 3. Semantic validation rules

The v0.2 schema does not by itself enforce all domain rules. Implementations must check:

- **Registry membership:** `relation_type` must exist in the selected relation-registry release. A pattern match alone is insufficient.
- **Endpoint integrity:** `source_id` and `target_id` must resolve to existing records of permitted types. A self-edge must be rejected unless a relation definition explicitly allows it.
- **Direction:** relation direction follows the registered definition. Never generate an inverse edge merely by reversing endpoints.
- **Evidence:** evidence class, scope, limitations, and source reference must be meaningful for the assertion. `UNVERIFIED-ASSERTION` records a pending claim; it is not supporting evidence.
- **Causality:** causal relation types require a stated causal method and assumptions. Correlation alone is insufficient.
- **Legal scope:** legal relations require jurisdiction and temporal validity.
- **Normative scope:** normative relations identify the value, right, duty, or principle basis and affected parties as appropriate.
- **Uncertainty:** uncertainty is distinct from confidence and evidence quality. Missing information is not zero.
- **Temporal consistency:** `valid_to` must not precede `valid_from`; review dates and assertion validity must be checked.
- **Hyperedges:** at least three distinct members are required, all members must resolve, role assignments must refer to members, and `why_not_pairwise` must explain the information lost by pairwise decomposition.
- **Privacy:** personal or restricted data must not be placed in public fixtures or exposed through public graph exports.

## 4. Conformance corpus

The companion file `tests/wqie/wqie-v0.3-conformance.json` contains illustrative fixtures. It separates expected schema validity from expected semantic validity because some constraints are intentionally outside the v0.2 JSON Schema.

Expected fixture classes:

- Schema-valid and semantically valid: one NODE, one RELATION, one HYPEREDGE.
- Schema-invalid: missing required uncertainty, out-of-range confidence, and a hyperedge with fewer than three members.
- Schema-valid but semantically invalid: unregistered relation ID and unresolved graph endpoint.

The examples are synthetic test data, not empirical findings, legal advice, or endorsed policy.

## 5. Known v0.2 schema limitations

The schema is a structural contract, not a complete graph validator. In particular:

- Registry membership cannot be guaranteed by the relation-ID regular expression.
- Cross-record references and endpoint types require graph-level validation.
- Temporal ordering between `valid_from` and `valid_to` requires application logic.
- `format: date-time` may be treated as annotation unless format assertion is enabled.
- Causal, legal, and normative adequacy require domain-specific review; structural validity cannot establish them.
- The schema does not define a universal confidence scale or composite score.

Do not silently modify the v0.2 schema in this task. Schema changes require a separately versioned proposal and migration note.

## 6. Test result vocabulary

Use these independent outcomes:

- `JSON_PARSE_PASS|FAIL`
- `SCHEMA_PASS|FAIL`
- `SEMANTIC_PASS|FAIL|NOT_RUN`

A fixture can pass schema validation and fail semantic validation. Overall conformance is `PASS` only when all required layers pass.

## 7. Release gate

A WQIE release candidate must include:

- the exact schema and registry versions;
- validator name/version and format-assertion configuration;
- all conformance fixture results;
- unresolved defects and accepted limitations;
- a review record and change history.

No validation result should be presented as a truth score, wisdom score, or automatic authorization for a policy or decision.
