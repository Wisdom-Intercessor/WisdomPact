import json
import re
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas" / "wqie-record-v0.2.schema.json"
CORPUS_PATH = ROOT / "tests" / "wqie" / "wqie-v0.3-conformance.json"
REGISTRY_PATH = ROOT / "docs" / "standards" / "WQIE-relation-registry-v0.2.md"

with SCHEMA_PATH.open(encoding="utf-8") as stream:
    SCHEMA = json.load(stream)
with CORPUS_PATH.open(encoding="utf-8") as stream:
    CORPUS = json.load(stream)
REGISTRY_TEXT = REGISTRY_PATH.read_text(encoding="utf-8")


def parse_registry_ids(markdown):
    """Read IDs only from canonical Markdown table rows in section 2."""
    in_registry_table = False
    ids = set()
    for line in markdown.splitlines():
        if line.startswith("## 2. Relation type registry"):
            in_registry_table = True
            continue
        if in_registry_table and line.startswith("## "):
            break
        if in_registry_table:
            match = re.match(r"^\|\s*(R-[A-Z]+-[0-9]{3})\s*\|", line)
            if match:
                ids.add(match.group(1))
    return ids


REGISTRY_IDS = parse_registry_ids(REGISTRY_TEXT)
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
FIXTURES = CORPUS["fixtures"]
RECORDS = [fixture["record"] for fixture in FIXTURES]
NODE_IDS = {record["id"] for record in RECORDS if record.get("record_type") == "NODE"}


def semantic_errors(record):
    errors = []
    kind = record.get("record_type")
    if kind == "RELATION":
        if record.get("relation_type") not in REGISTRY_IDS:
            errors.append("RELATION_TYPE_NOT_IN_REGISTRY")
        if record.get("source_id") not in NODE_IDS:
            errors.append("UNRESOLVED_SOURCE_NODE")
        if record.get("target_id") not in NODE_IDS:
            errors.append("UNRESOLVED_TARGET_NODE")
    elif kind == "HYPEREDGE":
        members = record.get("member_node_ids", [])
        if len(members) < 3:
            errors.append("HYPEREDGE_REQUIRES_AT_LEAST_THREE_MEMBERS")
        if len(set(members)) != len(members):
            errors.append("DUPLICATE_HYPEREDGE_MEMBER")
        if any(member not in NODE_IDS for member in members):
            errors.append("UNRESOLVED_HYPEREDGE_MEMBER")
        role_map = record.get("role_map", {})
        if not set(role_map).issubset(set(members)):
            errors.append("ROLE_MAP_REFERENCES_NON_MEMBER")
        if any(not isinstance(role, str) or not role.strip() for role in role_map.values()):
            errors.append("EMPTY_OR_INVALID_HYPEREDGE_ROLE")
    return errors


class WQIEConformanceTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self):
        Draft202012Validator.check_schema(SCHEMA)

    def test_registry_parser_reads_only_canonical_table_rows(self):
        sample = """## 2. Relation type registry
| ID | Type |
|---|---|
| R-TST-001 | test |
Example mention R-TST-999 is not a registry row.
## 3. Other section
| R-TST-002 | outside |
"""
        self.assertEqual(parse_registry_ids(sample), {"R-TST-001"})

    def test_registry_ids_are_unique_in_source(self):
        rows = re.findall(r"^\|\s*(R-[A-Z]+-[0-9]{3})\s*\|", REGISTRY_TEXT, flags=re.MULTILINE)
        self.assertEqual(len(rows), len(set(rows)))
        self.assertTrue(REGISTRY_IDS, "No canonical registry IDs were parsed")

    def test_schema_validity_matches_fixture_expectations(self):
        for fixture in FIXTURES:
            with self.subTest(fixture=fixture["id"]):
                errors = list(VALIDATOR.iter_errors(fixture["record"]))
                self.assertEqual(not errors, fixture["expected_schema_valid"],
                    msg="; ".join(f"{error.json_path}: {error.message}" for error in errors))

    def test_semantic_validity_matches_fixture_expectations(self):
        for fixture in FIXTURES:
            with self.subTest(fixture=fixture["id"]):
                errors = semantic_errors(fixture["record"])
                self.assertEqual(not errors, fixture["expected_semantic_valid"], msg=", ".join(errors))

    def test_exact_semantic_failure_codes(self):
        for fixture in FIXTURES:
            if "semantic_failure_codes" not in fixture:
                continue
            with self.subTest(fixture=fixture["id"]):
                self.assertEqual(sorted(semantic_errors(fixture["record"])),
                                 sorted(fixture["semantic_failure_codes"]))

    def test_fixture_ids_are_unique(self):
        ids = [fixture["id"] for fixture in FIXTURES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_record_ids_are_unique(self):
        ids = [record["id"] for record in RECORDS]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
