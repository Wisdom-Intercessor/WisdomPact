# WQIE Graph-Bundle Integrity Standard v0.6

**Status:** Proposed implementation  
**Depends on:** Record schema v0.2; relation registry v0.2; validation protocol v0.3; automated diagnostics v0.5.

## 1. Purpose

Version 0.6 extends validation from isolated records to a graph bundle containing multiple NODE, RELATION, and HYPEREDGE records. It checks graph-wide identity and reference integrity while preserving the distinction between structural conformance and substantive truth.

## 2. Bundle envelope

Each bundle declares graph_id, graph_version, record_schema_version, relation_registry_version, generated_at, and a non-empty records array. The v0.6 validator supports record schema 0.2 and relation registry 0.2. A version mismatch is a validation error, not an implicit migration.

## 3. Graph-wide rules

1. Record IDs are unique across the entire bundle, regardless of record type.
2. RELATION source_id and target_id must resolve to NODE records in the same bundle.
3. RELATION relation_type must exist in canonical table rows of the pinned relation registry.
4. HYPEREDGE records require at least three distinct members; every member must resolve to a NODE.
5. Every role_map key must be a declared member, and every role value must be a non-empty string.
6. When parseable temporal bounds are supplied, updated_at must not precede created_at, and valid_to must not precede valid_from.
7. Diagnostics are sorted deterministically by path, code, and message.

## 4. External references

Evidence references, source references, URLs, and provenance references may point to external catalogs or repositories. Without a declared source-catalog contract, the validator does not classify these references as broken. A later source-catalog integration must specify namespaces, resolver behavior, access control, and availability semantics.

## 5. Execution

Run:

    python -m pip install -r requirements-wqie.txt
    python tests/wqie/validate_conformance.py
    python tests/wqie/validate_graph_bundle.py tests/wqie/wqie-v0.6-graph-bundles.json
    python -m unittest discover -s tests/wqie -p 'test_*.py'

The graph validator exits with code 0 for a valid bundle and 1 for validation errors. It prints deterministic JSON diagnostics; --report PATH also writes the report to a file.

## 6. Explicit limitations

A passing report establishes only conformance to implemented rules. It does not establish evidence truth, sufficiency, causation, legal validity, or normative legitimacy. External source/evidence IDs are not resolved without a source-catalog specification. Synthetic bundles are test fixtures, not empirical findings. No physical quantum behavior, quantum advantage, or universal wisdom score is claimed.
