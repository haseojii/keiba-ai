from pathlib import Path
import argparse

import pandas as pd


def inspect_csv(csv_path: Path, head_rows: int = 5, show_missing: bool = True) -> None:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    # low_memory=False にして列型推定の分割読み込み警告を減らす
    df = pd.read_csv(csv_path, low_memory=False)

    print("=== Dataset Inspection ===")
    print(f"path: {csv_path}")
    print(f"shape: {df.shape}")

    print("\n[columns]")
    for idx, col in enumerate(df.columns, start=1):
        print(f"{idx:>3}. {col}")

    print(f"\n[head: {head_rows} rows]")
    print(df.head(head_rows).to_string(index=False))

    if show_missing:
        print("\n[missing values]")
        missing_counts = df.isna().sum().sort_values(ascending=False)
        print(missing_counts.to_string())


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect a CSV dataset with basic shape/column/missing-value info.",
    )
    parser.add_argument("csv_path", help="Path to the CSV file to inspect")
    parser.add_argument(
        "--head",
        type=int,
        default=5,
        help="Number of sample rows to display (default: 5)",
    )
    parser.add_argument(
        "--no-missing",
        action="store_true",
        help="Disable missing-value summary",
    )

    args = parser.parse_args()
    inspect_csv(
        csv_path=Path(args.csv_path),
        head_rows=args.head,
        show_missing=not args.no_missing,
    )


if __name__ == "__main__":
    main()
