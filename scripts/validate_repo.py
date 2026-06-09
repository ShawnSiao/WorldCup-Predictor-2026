import json
from pathlib import Path


REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "docs/README.zh-CN.md",
    "docs/methodology.md",
    "docs/methodology.zh-CN.md",
    "docs/sources.md",
    "docs/data-schema.md",
    "data/matches.json",
    "data/teams.json",
    "data/venues.json",
    "data/players.json",
    "data/rankings.json",
    "data/predictions.json",
    "data/results.json",
    "data/review-index.json",
    "predictions/README.md",
    "reviews/README.md",
    "reports/daily/README.md",
]

MATCH_STATUSES = {"scheduled", "predicted", "live", "final", "reviewed"}
REVIEW_RATINGS = {"correct", "partial", "wrong"}
PREDICTION_REQUIRED_SECTIONS = [
    "## Prediction",
    "## Factual Basis",
    "## Prediction Logic",
    "## Risk Factors",
    "## Platform Share Copy",
    "## Disclaimer",
    "## Source Snapshot",
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


def validate_repository(repo_root: Path) -> list[str]:
    errors: list[str] = []
    validate_required_paths(repo_root, errors)
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
