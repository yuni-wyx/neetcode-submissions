import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("refresh", Path(__file__).resolve().parents[1] / "scripts/refresh_submissions.py")
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)

class MappingTests(unittest.TestCase):
    def test_unknown_and_multiple_aliases(self):
        mapped, unknown = refresh.classify([{"id": 1}], {"1": ["a", "b"]}, {"a": [], "b": [], "other": []})
        self.assertEqual(mapped[1], ["a", "b"])
        self.assertEqual(unknown, ["other"])

    def test_collisions_rejected(self):
        with self.assertRaises(ValueError):
            refresh.classify([{"id": 1}, {"id": 2}], {"1": ["a"], "2": ["a"]}, {})

    def test_two_sum_mapping(self):
        rows = refresh.read_json("data/problems.json")
        aliases = refresh.read_json("data/slug-aliases.json")
        mapped, unknown = refresh.classify(rows, aliases, {"two-integer-sum": [], "two-integer-sum-ii": []})
        self.assertEqual(mapped[1], ["two-integer-sum"])
        self.assertEqual(mapped[167], ["two-integer-sum-ii"])
        self.assertEqual(unknown, [])
        self.assertEqual(len(rows), 150)

if __name__ == "__main__":
    unittest.main()
