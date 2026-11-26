# WQIE v0.5 Validation and Test Reporting

**Status:** Proposed implementation accompanying PR #16  
**Scope:** Automated structural and semantic conformance checks for the v0.2 record schema, v0.2 relation registry, and synthetic v0.3 fixture corpus.

## Validation layers
1. **Schema:** JSON parsing, Draft 2020-12 meta-schema validity, and fixture validation with the pinned jsonschema implementation and explicit date-time format checking.
2. **Semantic:** relation-type membership in canonical registry table rows; relation endpoint resolution; Hyperedge cardinality, uniqueness, member resolution, and role-map membership/role validity.
3. **Corpus integrity:** unique fixture IDs and record IDs, plus exact expected semantic failure codes for negative fixtures.

Schema and semantic outcomes are independent. A record may be schema-valid but semantically invalid, as demonstrated by the unknown relation-type, unresolved endpoint, and invalid Hyperedge role-map fixtures.

## Registry parsing
Relation IDs are read only from Markdown table rows inside section 2, “Relation type registry”. Mentions in prose, examples, or other sections do not register a relation type. Duplicate canonical IDs fail the test suite.

## Diagnostic policy
Each failing test identifies its fixture and validation layer. Schema diagnostics include the JSON path and validator message. Semantic diagnostics use stable error codes. Passing conformance means only that tested records meet the implemented structural and semantic rules.

## Synthetic fixture coverage
The corpus contains positive and negative NODE, RELATION, and HYPEREDGE examples. These are synthetic test data, not empirical findings, legal conclusions, normative legitimacy, or proof of factual truth.

## Explicit limitations
- Evidence truth, sufficiency, bias, and currency are not adjudicated.
- Endpoint resolution is limited to NODE records in this fixture corpus; production graph storage requires repository-wide or service-level resolution.
- The runner does not infer inverse relations or causal claims.
- Passing tests confer no authority on a Charter interpretation or decision.
- No physical quantum behavior or quantum advantage is claimed.

## Reproducible command
```bash
python -m pip install -r requirements-wqie.txt
python tests/wqie/validate_conformance.py
```

CI executes the same command on relevant pull-request and main-branch changes. Actual GitHub Actions results, not file commits or local review, determine whether CI is green.
