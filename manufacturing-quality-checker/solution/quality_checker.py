"""Instructor reference solution for the production-line quality checker."""

import csv
from pathlib import Path


DATA_FILE = Path(__file__).parent.parent / "starter" / "sample_readings.csv"


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
    reasons = []

    if not 18.0 <= reading["temperature_c"] <= 25.0:
        reasons.append("temperature outside 18.0-25.0 C")
    if reading["vibration_mm_s"] > 4.0:
        reasons.append("vibration above 4.0 mm/s")
    if reading["defect_count"] > 2:
        reasons.append("defect count above 2")

    if reasons:
        return "REJECT", reasons
    return "PASS", []


def print_summary(results):
    """Print totals for the production shift."""
    total = len(results)
    passed = results.count("PASS")
    rejected = results.count("REJECT")
    rejection_rate = (rejected / total * 100) if total else 0

    print("-" * 40)
    print(f"Total: {total}")
    print(f"Passed: {passed}")
    print(f"Rejected: {rejected}")
    print(f"Rejection rate: {rejection_rate:.1f}%")


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
