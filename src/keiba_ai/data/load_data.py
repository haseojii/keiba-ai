from pathlib import Path
import pandas as pd


def load_csv(csv_path: str | Path) -> pd.DataFrame:
    """
    Load a CSV file and return a pandas DataFrame.

    Args:
        csv_path: Path to the input CSV file.

    Returns:
        Loaded DataFrame.
    """
    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    return pd.read_csv(path)