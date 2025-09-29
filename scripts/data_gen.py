#!/usr/bin/env python3
"""
Generate synthetic data for the Student Retention dashboard example.
"""

import argparse, json
import numpy as np, pandas as pd
from pathlib import Path

def main(seed: int):
    np.random.seed(seed)
    out_dir = Path(__file__).resolve().parents[1] / "data"
    out_dir.mkdir(exist_ok=True)

    # 1. Retention KPI
    kpi = {"retention_rate": 91}
    with open(out_dir / "retention_kpi.json", "w") as f:
        json.dump(kpi, f)

    # 2. Student composition CSV
    comp_df = pd.DataFrame({
        "Category": ["Returning", "New"],
        "Count":    [3600,         1600]
    })
    comp_df.to_csv(out_dir / "student_composition.csv", index=False)

    # 3. Retention by school CSV
    schools = [
        "Campus 2", "Campus 1", "Campus 3", "Campus 4",
        "Campus 8", "Campus 6", "Campus 5", "Campus 7"
    ]
    rates = [92, 91, 94, 84, 92, 92, 92, 85]
    school_df = pd.DataFrame({
        "Campus":         schools,
        "Retention Rate": rates
    })
    school_df.to_csv(out_dir / "retention_by_school.csv", index=False)

    # 4. District withdrawals CSV
    district_withdrawals_data = [
        # - August 2022 (total 62) -
        {"Month": "August",  "Year":2022, "Reason": "ADMIN WITHDRAW", "Count":0},
        {"Month": "August", "Year": 2022, "Reason": "Elementary With", "Count": 41},
        {"Month": "August", "Year": 2022, "Reason": "Enroll in Other", "Count": 1},
        {"Month": "August", "Year": 2022, "Reason": "EXP CAN'T RET", "Count": 4},
        {"Month": "August", "Year": 2022, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "August", "Year": 2022, "Reason": "OTHER (UNKNOWN)", "Count": 10},
        {"Month": "August", "Year": 2022, "Reason": "Transferred to", "Count": 6},

        # - September 2022 (total 72) -
        {"Month": "September", "Year": 2022, "Reason": "ADMIN WITHDRAW", "Count": 0},
        {"Month": "September", "Year": 2022, "Reason": "Elementary With", "Count": 51},
        {"Month": "September", "Year": 2022, "Reason": "Enroll in Other", "Count": 0},
        {"Month": "September", "Year": 2022, "Reason": "EXP CAN'T RET", "Count": 8},
        {"Month": "September", "Year": 2022, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "September", "Year": 2022, "Reason": "OTHER (UNKNOWN)", "Count": 13},
        {"Month": "September", "Year": 2022, "Reason": "Transferred to", "Count": 0},

        # - October 2022 (total 77) -
        {"Month": "October", "Year": 2022, "Reason": "ADMIN WITHDRAW", "Count": 0},
        {"Month": "October", "Year": 2022, "Reason": "Elementary With", "Count": 50},
        {"Month": "October", "Year": 2022, "Reason": "Enroll in Other", "Count": 0},
        {"Month": "October", "Year": 2022, "Reason": "EXP CAN'T RET", "Count": 17},
        {"Month": "October", "Year": 2022, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "October", "Year": 2022, "Reason": "OTHER (UNKNOWN)", "Count": 10},
        {"Month": "October", "Year": 2022, "Reason": "Transferred to", "Count": 0},

        # - November 2022 (total 58) -
        {"Month": "November", "Year": 2022, "Reason": "ADMIN WITHDRAW", "Count": 0},
        {"Month": "November", "Year": 2022, "Reason": "Elementary With", "Count": 42},
        {"Month": "November", "Year": 2022, "Reason": "Enroll in Other", "Count": 0},
        {"Month": "November", "Year": 2022, "Reason": "EXP CAN'T RET", "Count": 3},
        {"Month": "November", "Year": 2022, "Reason": "HOME SCHOOLING", "Count": 1},
        {"Month": "November", "Year": 2022, "Reason": "OTHER (UNKNOWN)", "Count": 12},
        {"Month": "November", "Year": 2022, "Reason": "Transferred to", "Count": 0},

        # - December 2022 (total 21) -
        {"Month": "December", "Year": 2022, "Reason": "ADMIN WITHDRAW", "Count": 0},
        {"Month": "December", "Year": 2022, "Reason": "Elementary With", "Count": 15},
        {"Month": "December", "Year": 2022, "Reason": "Enroll in Other", "Count": 1},
        {"Month": "December", "Year": 2022, "Reason": "EXP CAN'T RET", "Count": 1},
        {"Month": "December", "Year": 2022, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "December", "Year": 2022, "Reason": "OTHER (UNKNOWN)", "Count": 4},
        {"Month": "December", "Year": 2022, "Reason": "Transferred to", "Count": 0},

        # - January 2023 (total 98) -
        {"Month": "January", "Year": 2023, "Reason": "ADMIN WITHDRAW", "Count": 2},
        {"Month": "January", "Year": 2023, "Reason": "Elementary With", "Count": 60},
        {"Month": "January", "Year": 2023, "Reason": "Enroll in Other", "Count": 2},
        {"Month": "January", "Year": 2023, "Reason": "EXP CAN'T RET", "Count": 15},
        {"Month": "January", "Year": 2023, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "January", "Year": 2023, "Reason": "OTHER (UNKNOWN)", "Count": 19},
        {"Month": "January", "Year": 2023, "Reason": "Transferred to", "Count": 0},

        # - February 2023 (total 49) -
        {"Month": "February", "Year": 2023, "Reason": "ADMIN WITHDRAW", "Count": 0},
        {"Month": "February", "Year": 2023, "Reason": "Elementary With", "Count": 29},
        {"Month": "February", "Year": 2023, "Reason": "Enroll in Other", "Count": 1},
        {"Month": "February", "Year": 2023, "Reason": "EXP CAN'T RET", "Count": 4},
        {"Month": "February", "Year": 2023, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "February", "Year": 2023, "Reason": "OTHER (UNKNOWN)", "Count": 15},
        {"Month": "February", "Year": 2023, "Reason": "Transferred to", "Count": 0},

        # - March 2023 (total 40) -
        {"Month": "March", "Year": 2023, "Reason": "ADMIN WITHDRAW", "Count": 0},
        {"Month": "March", "Year": 2023, "Reason": "Elementary With", "Count": 18},
        {"Month": "March", "Year": 2023, "Reason": "Enroll in Other", "Count": 2},
        {"Month": "March", "Year": 2023, "Reason": "EXP CAN'T RET", "Count": 7},
        {"Month": "March", "Year": 2023, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "March", "Year": 2023, "Reason": "OTHER (UNKNOWN)", "Count": 12},
        {"Month": "March", "Year": 2023, "Reason": "Transferred to", "Count": 1},

        # - April 2023 (total 5) -
        {"Month": "April", "Year": 2023, "Reason": "ADMIN WITHDRAW", "Count": 0},
        {"Month": "April", "Year": 2023, "Reason": "Elementary With", "Count": 3},
        {"Month": "April", "Year": 2023, "Reason": "Enroll in Other", "Count": 0},
        {"Month": "April", "Year": 2023, "Reason": "EXP CAN'T RET", "Count": 1},
        {"Month": "April", "Year": 2023, "Reason": "HOME SCHOOLING", "Count": 0},
        {"Month": "April", "Year": 2023, "Reason": "OTHER (UNKNOWN)", "Count": 1},
        {"Month": "April", "Year": 2023, "Reason": "Transferred to", "Count": 0}
    ]

    district_df = pd.DataFrame(district_withdrawals_data)
    district_df.to_csv(out_dir / "district_withdrawals.csv", index=False)

    # 5. Withdrawal reasons summary CSV
    # Load the detailed withdrawals into a DataFrame
    df = pd.DataFrame(district_withdrawals_data)

    #5a. Sum counts by Reason
    summary = (
        df.groupby("Reason", as_index=False)["Count"]
        .sum()
    )

    # 5b. Compute percentage of total for each Reason
    total = summary["Count"].sum()
    summary["Percentage"] = (summary["Count"] / total * 100).round(1)


    # 5c. Write out to CSV
    summary.to_csv(out_dir / "withdrawal_reasons.csv", index=False)

    reasons_df = pd.DataFrame({
        "Reason": [
            "Elementar...",
            "Enroll in Ot...",
            "EXP CAN'...",
            "OTHER (U...",
            "Transferre...",
        ],
        "Percentage": [65.3, 1.5, 11.9, 19.9, 1.5]
    })
    reasons_df.to_csv(out_dir / "pie_data.csv", index=False)

    # 6. Confirmation Printout
    print("Data generation complete. Files saved in 'data/' directory:")
    print("- retention_kpi.json")
    print("- student_composition.csv")
    print("- retention_by_school.csv")
    print("- district_withdrawals.csv")
    print("- withdrawal_reasons.csv")

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    main(args.seed) 

