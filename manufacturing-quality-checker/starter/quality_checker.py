"""Production-line quality checker.

CLINE PROMPT
Open starter/quality_checker.py and starter/sample_readings.csv. Complete only
the code marked TODO 1 and TODO 2 in starter/quality_checker.py.

Requirements:
- Modify only starter/quality_checker.py.
- Do not change existing code outside the two TODO sections.
- Use only the Python standard library.
- Do not add dependencies or create new files.
- A reading passes when temperature is 18.0-25.0 C inclusive, vibration is
  at most 4.0 mm/s, and defect_count is at most 2.
- For rejected readings, list every failed rule as a short reason.
- The summary must show total, passed, rejected, and rejection rate.
- Keep the program simple and under 120 lines.
- After editing, summarize the changes in no more than five bullets.
"""

import csv
from pathlib import Path


DATA_FILE = Path(__file__).with_name("sample_readings.csv")


def load_readings(path):
    """Load production readings and convert numeric fields."""
    readings = []
    with path.open(newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            readings.append(
                {
                    "item_id": row["item_id"],
                    "temperature_c": float(row["temperature_c"]),
                    "vibration_mm_s": float(row["vibration_mm_s"]),
                    "defect_count": int(row["defect_count"]),
                }
            )
    return readings


def evaluate_reading(reading):
    """Return a status and a list of reasons for one production item."""
    # TODO 1: Check the three quality rules and collect every failed reason.
    # Return ("PASS", []) when there are no failures.
    # Return ("REJECT", reasons) when one or more rules fail.
    raise NotImplementedError("Ask Cline to complete TODO 1")


def print_summary(results):
    """Print totals for the production shift."""
    # TODO 2: Print total, passed, rejected, and rejection rate.
    raise NotImplementedError("Ask Cline to complete TODO 2")


def main():
    readings = load_readings(DATA_FILE)
    results = []

    print("Production Line Quality Report")
    print("-" * 40)

    for reading in readings:
        status, reasons = evaluate_reading(reading)
        results.append(status)
        detail = "; ".join(reasons) if reasons else "within all limits"
        print(f"{reading['item_id']}: {status} - {detail}")

    print_summary(results)


if __name__ == "__main__":
    main()
