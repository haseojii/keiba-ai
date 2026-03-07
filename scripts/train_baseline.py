from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.append(str(SRC_ROOT))

from keiba_ai.data.load_data import load_csv
from keiba_ai.features import build_feature_table
from keiba_ai.models.train_baseline import train_baseline_model


def main() -> None:
    csv_path = PROJECT_ROOT / "data" / "processed" / "baseline_sample.csv"

    df = load_csv(csv_path)
    feature_table = build_feature_table(df, target_column="target")
    result = train_baseline_model(feature_table, target_column="target")

    print("=== Baseline Training Result ===")
    print(f"accuracy: {result.accuracy:.4f}")
    print(f"train size: {result.train_size}")
    print(f"test size: {result.test_size}")


if __name__ == "__main__":
    main()