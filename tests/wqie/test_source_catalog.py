import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schemas/wqie-source-catalog-v0.1.schema.json").read_text(encoding="utf-8"))
CORPUS = json.loads((ROOT / "tests/wqie/wqie-v0.1-source-catalog-fixtures.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

def catalog_for(entry):
    return {
        "catalog_id": "CATALOG-SYNTHETIC-TEST",
        "catalog_version": "0.1.0",
        "contract_version": "0.1",
        "generated_at": "2026-11-26T08:00:00Z",
        "entries": [entry],
    }

class SourceCatalogSchemaTests(unittest.TestCase):
    def test_fixture_expectations(self):
        for fixture in CORPUS["fixtures"]:
            with self.subTest(fixture=fixture["id"]):
                errors = list(VALIDATOR.iter_errors(catalog_for(fixture["entry"])))
                self.assertEqual(not errors, fixture["expected_valid"],
                    msg="; ".join(f"{e.json_path}: {e.message}" for e in errors))

    def test_source_ids_are_unique_in_corpus(self):
        ids = [f["entry"]["source_id"] for f in CORPUS["fixtures"]]
        self.assertEqual(len(ids), len(set(ids)))

if __name__ == "__main__":
    unittest.main(verbosity=2)
