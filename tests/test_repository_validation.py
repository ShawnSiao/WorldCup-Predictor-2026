import unittest
import re
from collections import Counter
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
        lead_image_path = "assets/cards/match-001-mex-rsa-lead.png"
        result_image_path = "assets/cards/match-001-mex-rsa.png"
        prediction = (repo_root / "predictions" / "match-001-mex-rsa.md").read_text(encoding="utf-8")
        daily_report = (repo_root / "reports" / "daily" / "2026-06-09.md").read_text(encoding="utf-8")

        self.assertIn(f"../{lead_image_path}", prediction)
        self.assertIn(f"../{result_image_path}", prediction)
        self.assertLess(prediction.index(lead_image_path), prediction.index(result_image_path))
        self.assertIn(f"../../{lead_image_path}", daily_report)
        self.assertIn(f"../../{result_image_path}", daily_report)
        self.assertLess(daily_report.index(lead_image_path), daily_report.index(result_image_path))

    def test_share_images_use_imagegen_not_code_generated_assets(self):
        repo_root = Path(__file__).resolve().parents[1]
        agent_index = (repo_root / "AGENTS.md").read_text(encoding="utf-8")
        card_svg_files = list((repo_root / "assets" / "cards").glob("*.svg"))

        self.assertIn("$imagegen", agent_index)
        self.assertIn("lead_image_file", agent_index)
        self.assertIn("不输出比分", agent_index)
        self.assertFalse((repo_root / "scripts" / "generate_prediction_card.py").exists())
        self.assertEqual(card_svg_files, [])

    def test_public_markdown_files_do_not_repeat_section_headings(self):
        repo_root = Path(__file__).resolve().parents[1]
        repeated_headings = []

        for markdown_file in repo_root.rglob("*.md"):
            relative_path = markdown_file.relative_to(repo_root).as_posix()
            if relative_path.startswith("docs/local/"):
                continue

            text = markdown_file.read_text(encoding="utf-8")
            headings = re.findall(r"^(#{2,3})\s+(.+?)\s*$", text, flags=re.MULTILINE)
            counts = Counter((level, title.strip()) for level, title in headings)
            for (level, title), count in counts.items():
                if count > 1:
                    repeated_headings.append(f"{relative_path}: {level} {title}")

        self.assertEqual(repeated_headings, [])

    def test_prediction_files_have_single_header_navigation(self):
        repo_root = Path(__file__).resolve().parents[1]
        problems = []
        generated_files = list((repo_root / "predictions").glob("match-*.md"))
        generated_files.extend((repo_root / "reports" / "daily").glob("20*.md"))

        for generated_file in sorted(generated_files):
            text = generated_file.read_text(encoding="utf-8")
            body_after_title = text.split("\n# ", 1)[-1]
            pre_first_section = body_after_title.split("\n## ", 1)[0]
            nav_lines = [
                line
                for line in pre_first_section.splitlines()
                if line.startswith("[") and "](" in line and " | " in line
            ]

            relative_path = generated_file.relative_to(repo_root).as_posix()
            if len(nav_lines) != 1:
                problems.append(f"{relative_path}: expected 1 navigation line, found {len(nav_lines)}")
            elif generated_file.name.endswith(".zh-CN.md") and "[English]" not in nav_lines[0]:
                problems.append(f"{relative_path}: navigation line must link English counterpart")
            elif not generated_file.name.endswith(".zh-CN.md") and "[简体中文]" not in nav_lines[0]:
                problems.append(f"{relative_path}: navigation line must link Simplified Chinese counterpart")

        self.assertEqual(problems, [])

    def test_current_artifact_sections_do_not_repeat_entries(self):
        repo_root = Path(__file__).resolve().parents[1]
        sections = [
            (repo_root / "README.md", "Current Artifacts"),
            (repo_root / "docs" / "README.zh-CN.md", "当前产物"),
        ]
        problems = []

        for path, heading in sections:
            text = path.read_text(encoding="utf-8")
            match = re.search(rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)", text, flags=re.MULTILINE | re.DOTALL)
            self.assertIsNotNone(match, f"{path.name} must contain ## {heading}")
            entries = [line.strip() for line in match.group("body").splitlines() if line.startswith("- ")]
            duplicates = sorted(entry for entry, count in Counter(entries).items() if count > 1)
            for duplicate in duplicates:
                problems.append(f"{path.relative_to(repo_root).as_posix()}: duplicate artifact entry {duplicate}")

        self.assertEqual(problems, [])

    def test_markdown_tables_do_not_repeat_source_or_coverage_rows(self):
        repo_root = Path(__file__).resolve().parents[1]
        problems = []

        table_checks = [
            (repo_root / "docs" / "sources.md", "Current Source Snapshot"),
            (repo_root / "docs" / "sources.zh-CN.md", "当前来源快照"),
        ]
        table_checks.extend(
            (prediction_file, "Prediction Coverage Checklist")
            for prediction_file in sorted((repo_root / "predictions").glob("match-*.md"))
            if not prediction_file.name.endswith(".zh-CN.md")
        )
        table_checks.extend(
            (prediction_file, "预测覆盖检查")
            for prediction_file in sorted((repo_root / "predictions").glob("match-*.zh-CN.md"))
        )
        for daily_report in sorted((repo_root / "reports" / "daily").glob("20*.md")):
            text = daily_report.read_text(encoding="utf-8")
            if daily_report.name.endswith(".zh-CN.md"):
                heading = "近期比赛" if "## 近期比赛" in text else "下一场比赛"
            else:
                heading = "Next Matches" if "## Next Matches" in text else "Next Match"
            table_checks.append((daily_report, heading))

        for path, heading in table_checks:
            text = path.read_text(encoding="utf-8")
            match = re.search(rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)", text, flags=re.MULTILINE | re.DOTALL)
            self.assertIsNotNone(match, f"{path.name} must contain ## {heading}")
            first_column_values = []
            for line in match.group("body").splitlines():
                if not line.startswith("|"):
                    continue
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if not cells or set(cells[0]) <= {"-", ":"} or cells[0] in {"Dimension", "维度", "Topic", "主题"}:
                    continue
                first_column_values.append(cells[0])

            duplicates = sorted(value for value, count in Counter(first_column_values).items() if count > 1)
            for duplicate in duplicates:
                problems.append(f"{path.relative_to(repo_root).as_posix()}: duplicate table row {duplicate}")

        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
