from dataclasses import dataclass
from typing import Any

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


@dataclass
class TrainingResult:
    model: Any
    accuracy: float
    train_size: int
    test_size: int


def train_baseline_model(
    df: pd.DataFrame,
    target_column: str = "target",
    test_size: float = 0.2,
    random_state: int = 42,
) -> TrainingResult:
    """
    Train a simple baseline classification model.

    Args:
        df: Input dataframe containing features and target.
        target_column: Name of the target column.
        test_size: Ratio of test split.
        random_state: Random seed.

    Returns:
        TrainingResult containing model and evaluation summary.
    """
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataframe.")

    X = df.drop(columns=[target_column])
    y = df[target_column]

    if X.empty:
        raise ValueError("Feature dataframe is empty after dropping target column.")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y if y.nunique() > 1 else None,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=random_state,
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return TrainingResult(
        model=model,
        accuracy=accuracy,
        train_size=len(X_train),
        test_size=len(X_test),
    )