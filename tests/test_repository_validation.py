import unittest
from pathlib import Path

from scripts.validate_repo import validate_repository


class RepositoryValidationTest(unittest.TestCase):
    def test_repository_artifacts_are_valid(self):
        repo_root = Path(__file__).resolve().parents[1]

        errors = validate_repository(repo_root)

        self.assertEqual(errors, [])

    def test_ai_work_index_exists(self):
        repo_root = Path(__file__).resolve().parents[1]

        self.assertTrue((repo_root / "AGENTS.md").exists())

    def test_prediction_files_include_required_explanation_sections(self):
        repo_root = Path(__file__).resolve().parents[1]
        prediction = (repo_root / "predictions" / "match-001-mex-rsa.md").read_text(encoding="utf-8")

        required_sections = [
            "## Factual Basis",
            "## Prediction Logic",
            "## Platform Share Copy",
            "## Disclaimer",
        ]
        for section in required_sections:
            with self.subTest(section=section):
                self.assertIn(section, prediction)


if __name__ == "__main__":
    unittest.main()
