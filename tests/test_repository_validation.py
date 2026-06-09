import unittest
from pathlib import Path

from scripts.validate_repo import validate_repository


class RepositoryValidationTest(unittest.TestCase):
    def test_repository_artifacts_are_valid(self):
        repo_root = Path(__file__).resolve().parents[1]

        errors = validate_repository(repo_root)

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
