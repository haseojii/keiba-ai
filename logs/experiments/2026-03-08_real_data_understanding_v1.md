# Experiment Log: real_data_understanding_v1

- Date: 2026-03-08
- Purpose: 実データの行単位仮説・target候補・リーク候補・初期特徴量候補を明確化する
- Stage: Real-data understanding

## Dataset inspected
- File: `data/raw/19860105-20210731_race_result.csv`
- Shape: 1,626,811 rows x 66 columns
- Working row-unit assumption: 1行 = 1頭のレース出走結果（仮説）

## What was learned
- 大規模な表データで、学習対象として十分な行数がある
- レース後確定情報（着順/タイム/着差/コーナー通過順/上り/賞金）が多く、リーク管理が重要
- いきなり全列投入は避けるべき

## Target candidates
- `着順 == 1`（win）
- `着順 <= 3`（top-3）

## Initial target recommendation
- first real-data baseline は `着順 <= 3` を推奨
- 理由: 正例不足が緩和され、初期比較がしやすい

## Leakage candidates
- `着順`, `タイム`, `着差`, `1-4コーナー`, `上り`, `賞金(万円)`

## First feature candidates (small)
- `距離(m)`, `斤量`, `枠番`, `馬番`, `性別`, `馬齢`, `競馬場コード`, `芝・ダート区分`, `天候`, `馬場状態1`

## Likely next step
- `features/` に最小の実データ向け前処理を追加し、
  上記特徴量 + `top-3 target` で最初の real-data baseline を実行する
