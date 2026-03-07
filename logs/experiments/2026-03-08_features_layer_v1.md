# Experiment Log: features_layer_v1

- Date: 2026-03-08
- Purpose: 学習フローに最小のfeatures層を追加し、責務分離を明確にする
- Stage: Feature engineering (skeleton)

## Input
- Data: `data/processed/baseline_sample.csv`
- Target column: `target`
- New feature module: `src/keiba_ai/features/build_features.py`

## Run Command
```bash
python scripts/train_baseline.py
```

## Result
- accuracy: `0.5000`
- train size: `8`
- test size: `2`
- Note: 既存サンプルデータで従来どおり実行できることを確認

## Notes
- 追加した `build_feature_table` は現時点でほぼ素通し。
- ただし、target分離と特徴量テーブル構築の責務を明示できた。
- 次回以降の特徴量追加を `features/` に集中させやすくなった。
