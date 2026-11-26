#!/usr/bin/env python3
"""WQIE v0.6 graph-bundle integrity validator."""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
RECORD_SCHEMA_PATH = ROOT / "schemas/wqie-record-v0.2.schema.json"
BUNDLE_SCHEMA_PATH = ROOT / "schemas/wqie-graph-bundle-v0.6.schema.json"
REGISTRY_PATH = ROOT / "docs/standards/WQIE-relation-registry-v0.2.md"

def load_json(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)

def parse_registry_ids(markdown):
    in_table, ids = False, []
    for line in markdown.splitlines():
        if line.startswith("## 2. Relation type registry"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if in_table:
            match = re.match(r"^\|\s*(R-[A-Z]+-[0-9]{3})\s*\|", line)
            if match:
                ids.append(match.group(1))
    return set(ids), ids

RECORD_SCHEMA = load_json(RECORD_SCHEMA_PATH)
BUNDLE_SCHEMA = load_json(BUNDLE_SCHEMA_PATH)
Draft202012Validator.check_schema(RECORD_SCHEMA)
Draft202012Validator.check_schema(BUNDLE_SCHEMA)
RECORD_VALIDATOR = Draft202012Validator(RECORD_SCHEMA, format_checker=FormatChecker())
BUNDLE_VALIDATOR = Draft202012Validator(BUNDLE_SCHEMA, format_checker=FormatChecker())
REGISTRY_IDS, REGISTRY_ID_ROWS = parse_registry_ids(REGISTRY_PATH.read_text(encoding="utf-8"))

def parse_time(value):
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None

def diag(code, path, message):
    return {"code": code, "path": path, "message": message}

def validate_bundle(bundle):
    errors = []
    for error in BUNDLE_VALIDATOR.iter_errors(bundle):
        errors.append(diag("BUNDLE_SCHEMA_INVALID", error.json_path, error.message))
    if errors:
        return sorted(errors, key=lambda x: (x["path"], x["code"], x["message"]))

    if len(REGISTRY_ID_ROWS) != len(REGISTRY_IDS):
        errors.append(diag("DUPLICATE_REGISTRY_RELATION_ID", "registry",
                           "Canonical registry table contains duplicate relation IDs."))
    ids = {}
    for i, record in enumerate(bundle["records"]):
        path = f"$.records[{i}]"
        for error in RECORD_VALIDATOR.iter_errors(record):
            errors.append(diag("RECORD_SCHEMA_INVALID", path + error.json_path[1:], error.message))
        rid = record.get("id")
        if isinstance(rid, str):
            if rid in ids:
                errors.append(diag("DUPLICATE_RECORD_ID", path + ".id",
                                   f"Record ID also appears at $.records[{ids[rid]}].id."))
            else:
                ids[rid] = i

    nodes = {r.get("id") for r in bundle["records"] if r.get("record_type") == "NODE"}
    for i, record in enumerate(bundle["records"]):
        path, kind = f"$.records[{i}]", record.get("record_type")
        if kind == "RELATION":
            if record.get("relation_type") not in REGISTRY_IDS:
                errors.append(diag("RELATION_TYPE_NOT_IN_REGISTRY", path + ".relation_type",
                                   "Relation type is absent from the pinned canonical registry."))
            for field in ("source_id", "target_id"):
                if record.get(field) not in nodes:
                    errors.append(diag("UNRESOLVED_RELATION_NODE", path + "." + field,
                                       "Relation endpoint must resolve to a NODE in this bundle."))
        elif kind == "HYPEREDGE":
            members = record.get("member_node_ids", [])
            if len(set(members)) < 3:
                errors.append(diag("HYPEREDGE_TOO_FEW_MEMBERS", path + ".member_node_ids",
                                   "A Hyperedge requires at least three distinct NODE members."))
            if len(members) != len(set(members)):
                errors.append(diag("DUPLICATE_HYPEREDGE_MEMBER", path + ".member_node_ids",
                                   "Hyperedge member IDs must be unique."))
            for j, member in enumerate(members):
                if member not in nodes:
                    errors.append(diag("UNRESOLVED_HYPEREDGE_MEMBER",
                                       f"{path}.member_node_ids[{j}]",
                                       "Hyperedge member must resolve to a NODE in this bundle."))
            roles = record.get("role_map", {})
            if not set(roles).issubset(set(members)):
                errors.append(diag("ROLE_MAP_REFERENCES_NON_MEMBER", path + ".role_map",
                                   "Every role_map key must identify a declared member."))
            if any(not isinstance(v, str) or not v.strip() for v in roles.values()):
                errors.append(diag("INVALID_HYPEREDGE_ROLE", path + ".role_map",
                                   "Role values must be non-empty strings."))
        created, updated = parse_time(record.get("created_at")), parse_time(record.get("updated_at"))
        start, end = parse_time(record.get("valid_from")), parse_time(record.get("valid_to"))
        if created and updated and updated < created:
            errors.append(diag("UPDATED_BEFORE_CREATED", path + ".updated_at",
                               "updated_at must not precede created_at."))
        if start and end and end < start:
            errors.append(diag("INVALID_VALIDITY_INTERVAL", path + ".valid_to",
                               "valid_to must not precede valid_from."))
    return sorted(errors, key=lambda x: (x["path"], x["code"], x["message"]))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    bundle = load_json(args.bundle)
    errors = validate_bundle(bundle)
    report = {"validator_version":"0.6","graph_id":bundle.get("graph_id"),
              "record_count":len(bundle.get("records",[])),"valid":not errors,
              "diagnostic_count":len(errors),"diagnostics":errors,
              "limitations":["External evidence/source references are not resolved without a catalog.",
                             "Conformance does not establish truth, legal validity, or normative legitimacy.",
                             "No inverse relations, causal conclusions, or universal wisdom score are inferred."]}
    output = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.report:
        args.report.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0 if not errors else 1

if __name__ == "__main__":
    sys.exit(main())
