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
            "## Prediction Coverage Checklist",
            "## Prediction Logic",
            "## Platform Share Copy",
            "## Disclaimer",
        ]
        for section in required_sections:
            with self.subTest(section=section):
                self.assertIn(section, prediction)

    def test_generated_documents_have_simplified_chinese_counterparts(self):
        repo_root = Path(__file__).resolve().parents[1]

        expected_files = [
            "predictions/match-001-mex-rsa.zh-CN.md",
            "reports/daily/2026-06-09.zh-CN.md",
            "docs/platform-copy.zh-CN.md",
            "docs/data-schema.zh-CN.md",
            "docs/sources.zh-CN.md",
        ]

        for relative_path in expected_files:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((repo_root / relative_path).exists())

    def test_platform_copy_mentions_highest_reasoning_model(self):
        repo_root = Path(__file__).resolve().parents[1]
        platform_copy = (repo_root / "docs" / "platform-copy.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("ChatGPT 最高推理模型", platform_copy)
        self.assertIn("仅为足球赛事预测，不构成任何投资建议。", platform_copy)

    def test_prediction_records_reference_existing_share_images(self):
        repo_root = Path(__file__).resolve().parents[1]

        errors = validate_repository(repo_root)

        self.assertEqual(errors, [])

    def test_prediction_and_daily_report_embed_share_image(self):
        repo_root = Path(__file__).resolve().parents[1]
        image_path = "assets/cards/match-001-mex-rsa.png"
        prediction = (repo_root / "predictions" / "match-001-mex-rsa.md").read_text(encoding="utf-8")
        daily_report = (repo_root / "reports" / "daily" / "2026-06-09.md").read_text(encoding="utf-8")

        self.assertIn(f"../{image_path}", prediction)
        self.assertIn(f"../../{image_path}", daily_report)

    def test_share_images_use_imagegen_not_code_generated_assets(self):
        repo_root = Path(__file__).resolve().parents[1]
        agent_index = (repo_root / "AGENTS.md").read_text(encoding="utf-8")
        card_svg_files = list((repo_root / "assets" / "cards").glob("*.svg"))

        self.assertIn("$imagegen", agent_index)
        self.assertFalse((repo_root / "scripts" / "generate_prediction_card.py").exists())
        self.assertEqual(card_svg_files, [])


if __name__ == "__main__":
    unittest.main()
