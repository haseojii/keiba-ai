# Data Notes

このファイルは、実データを理解しながら更新する作業メモです。
確定していない内容は断定せず、仮説として記録します。

## Dataset Source
- Source name: （要確認・未記入）
- URL: （要確認・未記入）
- Download date: 2026-03-08（手元配置日）
- License / usage notes: （要確認・未記入）

## Current Primary File
- `data/raw/19860105-20210731_race_result.csv`
- 形状: 1,626,811 rows x 66 columns

## Row Unit Assumption
- 仮説: **1行 = 1頭のレース出走結果（horse-race-entry）**
- 根拠（暫定）:
  - `レースID` と `馬番` の組み合わせで出走馬単位に見える
  - `着順`, `騎手`, `斤量`, `単勝`, `人気` などが同一行にある
- 確認が必要な点:
  - 同一 `レースID` 内で `馬番` の一意性
  - 取消/除外/失格時の扱い（`着順注記`）

## Important Columns (Grouped)

### ID / Join Keys
- `レース馬番ID`
- `レースID`
- `レース日付`

### Race Context (Before race)
- `競馬場コード`, `競馬場名`
- `芝・ダート区分`
- `距離(m)`
- `天候`
- `馬場状態1`
- `レース番号`

### Horse / Entry Info (Before race)
- `枠番`
- `馬番`
- `性別`
- `馬齢`
- `斤量`
- `騎手`

### Market Info (Before race but conceptually different)
- `人気`
- `単勝`

### Post-race / Outcome Info (Leakage risk)
- `着順`
- `タイム`
- `着差`
- `1コーナー`, `2コーナー`, `3コーナー`, `4コーナー`
- `上り`
- `賞金(万円)`

## Possible Target Columns
- 候補A: `着順 == 1`（win flag）
- 候補B: `着順 <= 3`（top-3 flag）

### Initial target recommendation (for first real-data baseline)
- 推奨: **top-3 flag (`着順 <= 3`)**
- 理由:
  - 勝利フラグ (`着順 == 1`) より正例が多く、初期学習が安定しやすい
  - 2値分類として理解しやすく、初学者に扱いやすい
  - 将来、win flag へ段階的に狭める比較もしやすい
- 注意:
  - `着順` 欠損/注記付き行の扱いルールを先に決める

## First Minimal Usable Feature Set (Proposal)

### Allowed early features (first-pass)
- `距離(m)`
- `斤量`
- `枠番`
- `馬番`
- `性別`
- `馬齢`
- `競馬場コード`
- `芝・ダート区分`
- `天候`
- `馬場状態1`

### Leakage / excluded now
- `着順`, `タイム`, `着差`
- `1コーナー`, `2コーナー`, `3コーナー`, `4コーナー`
- `上り`
- `賞金(万円)`

### Postpone for later (useful but扱い要注意)
- `人気`, `単勝`（市場情報として強いが、馬固有能力とは別軸）
- `騎手`（高カードinalityへのエンコード方針を決めてから）
- `馬名`, `調教師`, `馬主`（高カードinality）

## Possible Leakage Risks
- レース後に確定する情報（着順系・通過順位・上り・賞金）混入
- 未来情報を含む列の誤利用
- 学習時点で利用不可の情報を特徴量に含めること

## Questions for Later Investigation
- `着順` 欠損行（取消/除外等）をどう扱うか
- 時系列分割の基準（`レース日付`）をどう固定するか
- `人気` / `単勝` を初回で使うか、比較用に分けるか
- カテゴリ列（騎手・競馬場名など）の最小エンコード方針
