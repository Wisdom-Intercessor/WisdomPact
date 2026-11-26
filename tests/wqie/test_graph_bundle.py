import json
import unittest
from pathlib import Path
from validate_graph_bundle import validate_bundle

ROOT = Path(__file__).resolve().parents[2]
CORPUS = json.loads((ROOT / "tests/wqie/wqie-v0.6-graph-bundles.json").read_text(encoding="utf-8"))

class GraphBundleIntegrityTests(unittest.TestCase):
    def test_bundle_expectations_and_exact_diagnostic_codes(self):
        for fixture in CORPUS["bundles"]:
            with self.subTest(bundle=fixture["id"]):
                diagnostics = validate_bundle(fixture["bundle"])
                codes = sorted({item["code"] for item in diagnostics})
                self.assertEqual(not diagnostics, fixture["expected_valid"])
                self.assertEqual(codes, sorted(fixture["expected_codes"]))

if __name__ == "__main__":
    unittest.main(verbosity=2)
