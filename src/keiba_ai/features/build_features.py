import pandas as pd


def split_target_column(
    df: pd.DataFrame,
    target_column: str = "target",
) -> tuple[pd.DataFrame, pd.Series]:
    """Split input dataframe into feature columns and target column."""
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataframe.")

    feature_df = df.drop(columns=[target_column]).copy()
    target_series = df[target_column].copy()

    if feature_df.empty:
        raise ValueError("Feature dataframe is empty after dropping target column.")

    return feature_df, target_series


def build_feature_table(
    df: pd.DataFrame,
    target_column: str = "target",
) -> pd.DataFrame:
    """
    Build a training table for the baseline model.

    For now this function keeps features almost unchanged, but it acts as
    the single entry point for future feature engineering.
    """
    feature_df, target_series = split_target_column(df, target_column=target_column)
    return pd.concat([feature_df, target_series.rename(target_column)], axis=1)
