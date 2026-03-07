# Experiment Log: data_intake_prep_v1

- Date: 2026-03-08
- Purpose: 実データ受け入れ前の最小準備（raw配置・列確認・メモ運用）を整える
- Stage: Data intake preparation

## What Was Added
- `data/raw/` の受け入れ構成（`.gitkeep` と `.gitignore` ルール）
- `scripts/inspect_data.py`（CSVの形状・列・サンプル・欠損を確認）
- `docs/data_notes.md`（データ理解メモのひな形）

## Baseline Impact
- `scripts/train_baseline.py` の既存フローは変更なし
- 既存サンプルデータベースラインに影響なし

## Notes
- 実データ投入時にまず `inspect_data.py` で列構造を確認する運用を想定
- 複雑な評価ロジックや重いデータ管理ツールはまだ導入しない
- 次は、実データ列の意味整理と最小特徴量追加の比較実験が自然
