
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = ROOT / "experiments" / "results" / "baseline_results.jsonl"
OUTPUT_FILE = ROOT / "experiments" / "results" / "baseline_scoring_template.csv"


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    results = []

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            record = json.loads(line)

            # Ignore earlier failed/empty responses
            if not record.get("response", "").strip():
                continue

            results.append(record)

    if not results:
        print("No valid responses found.")
        return

    fieldnames = [
        "model",
        "question_id",
        "category",
        "prompt",
        "response",
        "score_1_to_5",
        "scoring_rationale",
        "evaluator",
        "rubric_version",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for record in results:
            writer.writerow({
                "model": record["model"],
                "question_id": record["question_id"],
                "category": record["category"],
                "prompt": record["prompt"],
                "response": record["response"],
                "score_1_to_5": "",
                "scoring_rationale": "",
                "evaluator": "human_1",
                "rubric_version": "1.0",
            })

    print(f"Scoring template created: {OUTPUT_FILE}")
    print(f"Valid responses extracted: {len(results)}")


if __name__ == "__main__":
    main()
