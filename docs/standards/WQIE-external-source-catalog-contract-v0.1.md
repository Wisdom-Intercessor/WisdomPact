# WQIE External Source-Catalog Contract v0.1

**Status:** Proposed specification  
**Scope:** Identity, catalog metadata, retrieval state, integrity metadata, and safe resolution boundaries for external sources referenced by WQIE records.  
**Compatibility:** Record schema v0.2 and graph-bundle schema v0.6 remain unchanged.

## 1. Purpose and governing distinctions

WQIE records currently carry source references as strings. This contract defines how an optional, separately versioned catalog may describe those references without changing existing records.

Four questions MUST remain separate:

1. **Identity:** Which source or source manifestation is being referenced?
2. **Resolution:** Can a resolver currently locate or access it?
3. **Integrity:** Does the retrieved representation match a recorded fingerprint?
4. **Epistemic assessment:** Is the source credible, relevant, methodologically sound, authoritative for the claim, or sufficient evidence?

A positive answer to one question MUST NOT be treated as an answer to another. In particular, a resolvable URL does not establish credibility, and a matching hash does not establish truth.

## 2. Catalog envelope and versioning

A catalog is a versioned data artifact with:
- `catalog_id`: stable identifier for the catalog;
- `catalog_version`: semantic version of the catalog dataset;
- `contract_version`: version of this contract;
- `generated_at`: UTC date-time when the catalog snapshot was generated;
- `entries`: source entries with unique `source_id` values.

A consumer MUST pin the catalog version or immutable snapshot digest used for a validation or research operation. Updating a catalog MUST NOT silently rewrite the historical meaning of a prior report.

## 3. Stable source identity

Each entry MUST have an opaque, stable `source_id` in the `SRC-...` namespace. The identifier MUST NOT encode a mutable URL, access status, credibility score, or user identity.

An entry MAY include one or more namespaced external identifiers, such as DOI, ISBN, arXiv identifier, repository object ID, or a publisher's identifier. The namespace and identifier are data, not instructions. Consumers MUST NOT infer equivalence between two entries solely because their titles or URLs look similar.

A source identity may refer to a work, dataset, legal instrument, repository object, or a specific manifestation/version. The `source_kind` and optional `version_label` make this distinction explicit.

## 4. Required entry fields

- `source_id`: stable catalog key.
- `source_kind`: controlled category such as publication, dataset, legal-instrument, standard, repository-object, web-page, archival-record, or other.
- `title`: human-readable title or label.
- `identifiers`: one or more typed identifiers.
- `access_class`: PUBLIC, INTERNAL, RESTRICTED, or PERSONAL-DATA.
- `resolution_status`: NOT-CHECKED, RESOLVED, NOT-FOUND, AMBIGUOUS, UNAVAILABLE, RESTRICTED, or DEPRECATED.
- `recorded_at`: date-time when this catalog entry was recorded.

Optional metadata includes publisher/issuer, creators, publication date, language, canonical URI, version label, rights note, last resolution check, and content fingerprint.

## 5. Resolution status semantics

- **NOT-CHECKED:** no resolution attempt is asserted.
- **RESOLVED:** a resolver located the declared source identity at the recorded check time.
- **NOT-FOUND:** the resolver received a result indicating that the requested identifier/resource was not found.
- **AMBIGUOUS:** multiple candidates remain and identity cannot safely be selected.
- **UNAVAILABLE:** resolution could not be completed due to transient or service/network conditions.
- **RESTRICTED:** access is blocked by permissions, authentication, licensing, or other access controls.
- **DEPRECATED:** the source has been withdrawn, superseded, or explicitly marked as no longer maintained; replacement information may be recorded separately.

A status is time-bound. It MUST be accompanied by `last_checked_at` when it represents an attempted resolution. A resolver MUST NOT convert timeouts, rate limits, or authentication barriers into NOT-FOUND.

## 6. Content integrity metadata

A content fingerprint MAY record a cryptographic digest of a retrieved representation. The algorithm and digest MUST be explicit; v0.1 supports SHA-256. A fingerprint MUST identify what was hashed (for example, raw bytes of a downloaded file or a normalized text export) and, where applicable, the media type.

A changed fingerprint indicates a changed representation, not necessarily a changed underlying work. A missing fingerprint means integrity was not established. Hash matching proves byte-level agreement with the recorded representation only.

## 7. Resolver contract

A future resolver implementation MUST:
- operate against an explicit catalog snapshot and declared resolver policy;
- record check time, resolver implementation/version, and outcome;
- distinguish not-found from unavailable, restricted, and ambiguous outcomes;
- preserve redirect history and final URI when redirects are followed;
- enforce bounded timeouts, response-size limits, and redirect limits;
- reject unsafe schemes by default and prevent access to loopback, private, link-local, and cloud-metadata network ranges;
- avoid forwarding credentials, cookies, or authorization headers across origins;
- avoid executing downloaded content;
- respect access controls, licensing, robots/terms constraints where applicable, and privacy classification;
- make no network request merely because a graph record contains a URI.

The current WQIE validators remain offline and MUST NOT fetch arbitrary external references. This contract specifies future behavior; it does not implement a resolver.

## 8. Privacy and access control

Catalog entries MUST NOT embed passwords, access tokens, session cookies, private keys, or other secrets. PERSONAL-DATA and RESTRICTED entries MUST NOT be exposed in public fixtures or public graph exports unless an authorized disclosure policy explicitly permits the specific fields.

A public catalog may expose a stable opaque reference while withholding sensitive metadata and the target URI. Access decisions MUST be enforced by the catalog service, not inferred from obscurity of an identifier.

## 9. Compatibility with WQIE v0.2/v0.6

Existing `evidence[].ref`, `provenance.source_refs[]`, and other string references remain valid and unchanged. A catalog integration MAY resolve those strings only when an explicit mapping to a catalog `source_id` or namespaced identifier exists.

No automatic URL interpretation, title matching, or identifier guessing is permitted. Unmapped strings receive an explicit UNMAPPED result in any future mapping report; they are not silently discarded or treated as invalid WQIE records.

The v0.6 graph-bundle schema and record schema are not modified by this proposal. A future schema integration requires a separately versioned proposal and migration plan.

## 10. Reporting and epistemic limits

A future source-resolution report SHOULD include catalog ID/version, entry ID, resolution status, check timestamp, resolver version, final URI where disclosure is permitted, fingerprint result, and diagnostics.

Reports MUST separately label:
- identity match;
- retrieval/access outcome;
- content-integrity outcome;
- evidence-quality assessment, if separately performed.

Catalog presence, successful resolution, publisher identity, or hash verification MUST NOT automatically increase confidence or evidence quality. Assessment of relevance, bias, methodology, authority, currency, and sufficiency remains a separately reviewable process.

## 11. Synthetic conformance fixtures

The accompanying fixture corpus is synthetic and tests schema shape only. It is not an evidence corpus and does not establish source quality. CI MUST validate fixtures offline without dereferencing any URI.

## 12. Change control

Changes to controlled values, identifier semantics, privacy rules, resolver security requirements, or fingerprint semantics require a new contract version and migration note. Implementations MUST declare the contract version they support and MUST reject unsupported major versions rather than guessing.
