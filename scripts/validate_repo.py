import json
from pathlib import Path


REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "assets/cards/README.md",
    "assets/cards/README.zh-CN.md",
    "docs/README.zh-CN.md",
    "docs/methodology.md",
    "docs/methodology.zh-CN.md",
    "docs/platform-copy.md",
    "docs/platform-copy.zh-CN.md",
    "docs/sources.md",
    "docs/sources.zh-CN.md",
    "docs/data-schema.md",
    "docs/data-schema.zh-CN.md",
    "data/matches.json",
    "data/teams.json",
    "data/venues.json",
    "data/players.json",
    "data/rankings.json",
    "data/predictions.json",
    "data/results.json",
    "data/review-index.json",
    "predictions/README.md",
    "predictions/README.zh-CN.md",
    "reviews/README.md",
    "reviews/README.zh-CN.md",
    "reports/daily/README.md",
    "reports/daily/README.zh-CN.md",
]

MATCH_STATUSES = {"scheduled", "predicted", "live", "final", "reviewed"}
REVIEW_RATINGS = {"correct", "partial", "wrong"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
PREDICTION_REQUIRED_SECTIONS = [
    "## Prediction",
    "## Share Image",
    "## Factual Basis",
    "## Prediction Coverage Checklist",
    "## Prediction Logic",
    "## Risk Factors",
    "## Platform Share Copy",
    "## Disclaimer",
    "## Source Snapshot",
]

BILINGUAL_DOCUMENT_PAIRS = [
    ("docs/data-schema.md", "docs/data-schema.zh-CN.md"),
    ("docs/sources.md", "docs/sources.zh-CN.md"),
    ("docs/platform-copy.md", "docs/platform-copy.zh-CN.md"),
    ("assets/cards/README.md", "assets/cards/README.zh-CN.md"),
    ("predictions/README.md", "predictions/README.zh-CN.md"),
    ("reports/daily/README.md", "reports/daily/README.zh-CN.md"),
    ("reviews/README.md", "reviews/README.zh-CN.md"),
]


def load_json(repo_root: Path, relative_path: str, errors: list[str]):
    path = repo_root / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"Missing JSON file: {relative_path}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {relative_path}: {exc}")
    return None


def validate_required_paths(repo_root: Path, errors: list[str]) -> None:
    for relative_path in REQUIRED_PATHS:
        if not (repo_root / relative_path).exists():
            errors.append(f"Missing required path: {relative_path}")


def validate_bilingual_document_pairs(repo_root: Path, errors: list[str]) -> None:
    for english_path, chinese_path in BILINGUAL_DOCUMENT_PAIRS:
        if not (repo_root / english_path).exists():
            errors.append(f"Missing English document: {english_path}")
        if not (repo_root / chinese_path).exists():
            errors.append(f"Missing Simplified Chinese document: {chinese_path}")


def has_valid_raster_header(path: Path) -> bool:
    header = path.read_bytes()[:16]
    suffix = path.suffix.lower()
    if suffix == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    if suffix == ".webp":
        return header.startswith(b"RIFF") and header[8:12] == b"WEBP"
    return False


def validate_raster_image(
    repo_root: Path,
    match_id: str | None,
    field_name: str,
    image_file: str | None,
    errors: list[str],
) -> bool:
    if not image_file:
        errors.append(f"Prediction {match_id} must include {field_name}")
        return False
    if not image_file.startswith("assets/cards/"):
        errors.append(f"Prediction {match_id} {field_name} must be under assets/cards/: {image_file}")
        return False
    if (repo_root / image_file).suffix.lower() not in IMAGE_EXTENSIONS:
        errors.append(f"Prediction {match_id} {field_name} must be a raster social card: {image_file}")
        return False
    if not (repo_root / image_file).exists():
        errors.append(f"Prediction {match_id} {field_name} missing: {image_file}")
        return False
    if not has_valid_raster_header(repo_root / image_file):
        errors.append(f"Prediction {match_id} {field_name} is not a valid raster image: {image_file}")
        return False
    return True


def validate_image_order(
    text: str,
    match_id: str | None,
    label: str,
    lead_image_file: str | None,
    result_image_file: str | None,
    errors: list[str],
) -> None:
    if not lead_image_file or not result_image_file:
        return
    lead_index = text.find(lead_image_file)
    result_index = text.find(result_image_file)
    if lead_index == -1:
        errors.append(f"{label} {match_id} must embed lead image file: {lead_image_file}")
    if result_index == -1:
        errors.append(f"{label} {match_id} must embed result image file: {result_image_file}")
    if lead_index != -1 and result_index != -1 and lead_index > result_index:
        errors.append(f"{label} {match_id} must embed lead image before result image")


def validate_matches(repo_root: Path, errors: list[str]) -> set[str]:
    data = load_json(repo_root, "data/matches.json", errors)
    if not data:
        return set()

    matches = data.get("matches")
    if not isinstance(matches, list):
        errors.append("data/matches.json must contain a matches array")
        return set()

    match_ids = set()
    required = {
        "match_id",
        "stage",
        "kickoff_utc",
        "venue_id",
        "home_team_code",
        "away_team_code",
        "status",
        "source_urls",
        "last_verified_at",
    }
    for match in matches:
        missing = sorted(required - set(match))
        if missing:
            errors.append(f"Match {match.get('match_id', '<unknown>')} missing fields: {', '.join(missing)}")
        status = match.get("status")
        if status not in MATCH_STATUSES:
            errors.append(f"Match {match.get('match_id', '<unknown>')} has invalid status: {status}")
        match_id = match.get("match_id")
        if match_id in match_ids:
            errors.append(f"Duplicate match_id: {match_id}")
        if match_id:
            match_ids.add(match_id)
        if not match.get("source_urls"):
            errors.append(f"Match {match.get('match_id', '<unknown>')} must include source URLs")

    return match_ids


def validate_predictions(repo_root: Path, match_ids: set[str], errors: list[str]) -> None:
    data = load_json(repo_root, "data/predictions.json", errors)
    if not data:
        return

    predictions = data.get("predictions")
    if not isinstance(predictions, list):
        errors.append("data/predictions.json must contain a predictions array")
        return

    for prediction in predictions:
        match_id = prediction.get("match_id")
        if match_id not in match_ids:
            errors.append(f"Prediction references unknown match_id: {match_id}")
        prediction_file = prediction.get("prediction_file")
        prediction_file_zh = prediction.get("prediction_file_zh")
        lead_image_file = prediction.get("lead_image_file")
        result_image_file = prediction.get("image_file")
        if not prediction_file or not (repo_root / prediction_file).exists():
            errors.append(f"Prediction file missing for match {match_id}: {prediction_file}")
        else:
            prediction_text = (repo_root / prediction_file).read_text(encoding="utf-8")
            for section in PREDICTION_REQUIRED_SECTIONS:
                if section not in prediction_text:
                    errors.append(f"Prediction {match_id} missing required section: {section}")
            if "investment advice" not in prediction_text.lower():
                errors.append(f"Prediction {match_id} must include an investment advice disclaimer")
            if "投资建议" not in prediction_text:
                errors.append(f"Prediction {match_id} must include a Chinese investment advice disclaimer")
            validate_image_order(
                prediction_text,
                match_id,
                "Prediction",
                lead_image_file,
                result_image_file,
                errors,
            )
        if not prediction_file_zh or not (repo_root / prediction_file_zh).exists():
            errors.append(f"Prediction {match_id} missing Simplified Chinese prediction file: {prediction_file_zh}")
        else:
            prediction_text_zh = (repo_root / prediction_file_zh).read_text(encoding="utf-8")
            validate_image_order(
                prediction_text_zh,
                match_id,
                "Chinese prediction",
                lead_image_file,
                result_image_file,
                errors,
            )
            if "## 预测覆盖检查" not in prediction_text_zh:
                errors.append(f"Chinese prediction {match_id} missing required section: ## 预测覆盖检查")
            if "投资建议" not in prediction_text_zh:
                errors.append(f"Chinese prediction {match_id} must include a Chinese investment advice disclaimer")
        lead_image_valid = validate_raster_image(repo_root, match_id, "lead_image_file", lead_image_file, errors)
        result_image_valid = validate_raster_image(repo_root, match_id, "image_file", result_image_file, errors)
        if lead_image_file and result_image_file and lead_image_file == result_image_file:
            errors.append(f"Prediction {match_id} lead_image_file and image_file must be different")
        if lead_image_valid and result_image_valid:
            published_at = prediction.get("published_at")
            if isinstance(published_at, str) and "T" in published_at:
                report_date = published_at.split("T", 1)[0]
                daily_report = repo_root / "reports" / "daily" / f"{report_date}.md"
                if daily_report.exists():
                    daily_report_text = daily_report.read_text(encoding="utf-8")
                    validate_image_order(
                        daily_report_text,
                        match_id,
                        f"Daily report {report_date}",
                        lead_image_file,
                        result_image_file,
                        errors,
                    )
                    daily_report_zh = repo_root / "reports" / "daily" / f"{report_date}.zh-CN.md"
                    if not daily_report_zh.exists():
                        errors.append(f"Daily report {report_date} missing Simplified Chinese file")
                    else:
                        validate_image_order(
                            daily_report_zh.read_text(encoding="utf-8"),
                            match_id,
                            f"Chinese daily report {report_date}",
                            lead_image_file,
                            result_image_file,
                            errors,
                        )
        probabilities = [
            prediction.get("home_win_probability"),
            prediction.get("draw_probability"),
            prediction.get("away_win_probability"),
        ]
        if not all(isinstance(value, (int, float)) for value in probabilities):
            errors.append(f"Prediction {match_id} must include numeric probabilities")
        elif round(sum(probabilities), 2) != 1:
            errors.append(f"Prediction {match_id} probabilities must sum to 1.00")


def validate_reviews(repo_root: Path, match_ids: set[str], errors: list[str]) -> None:
    data = load_json(repo_root, "data/review-index.json", errors)
    if not data:
        return

    reviews = data.get("reviews")
    if not isinstance(reviews, list):
        errors.append("data/review-index.json must contain a reviews array")
        return

    for review in reviews:
        match_id = review.get("match_id")
        if match_id not in match_ids:
            errors.append(f"Review references unknown match_id: {match_id}")
        review_file = review.get("review_file")
        if not review_file or not (repo_root / review_file).exists():
            errors.append(f"Review file missing for match {match_id}: {review_file}")
        rating = review.get("review_rating")
        if rating not in REVIEW_RATINGS:
            errors.append(f"Review {match_id} has invalid rating: {rating}")


def validate_share_image_policy(repo_root: Path, errors: list[str]) -> None:
    agent_index = repo_root / "AGENTS.md"
    if agent_index.exists():
        agent_text = agent_index.read_text(encoding="utf-8")
        if "$imagegen" not in agent_text:
            errors.append("AGENTS.md must require $imagegen for prediction share images")
        if "简体中文" not in agent_text:
            errors.append("AGENTS.md must require Simplified Chinese match information for Chinese prediction images")
        if "lead_image_file" not in agent_text:
            errors.append("AGENTS.md must require a lead_image_file for first prediction share images")
        if "不输出比分" not in agent_text or "胜负" not in agent_text:
            errors.append("AGENTS.md must state that first prediction share images omit scoreline and winner/result")

    generator_script = repo_root / "scripts" / "generate_prediction_card.py"
    if generator_script.exists():
        errors.append("Prediction share images must not depend on code-generated image scripts")

    cards_dir = repo_root / "assets" / "cards"
    if cards_dir.exists():
        svg_files = sorted(path.as_posix() for path in cards_dir.glob("*.svg"))
        if svg_files:
            errors.append(f"Prediction share images must not be SVG files: {', '.join(svg_files)}")


def validate_repository(repo_root: Path) -> list[str]:
    errors: list[str] = []
    validate_required_paths(repo_root, errors)
    validate_bilingual_document_pairs(repo_root, errors)
    validate_share_image_policy(repo_root, errors)
    match_ids = validate_matches(repo_root, errors)
    validate_predictions(repo_root, match_ids, errors)
    validate_reviews(repo_root, match_ids, errors)
    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors = validate_repository(repo_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
