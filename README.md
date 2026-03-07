# keiba-ai

競馬予測AIを、再現可能な小さなステップで育てる学習用プロジェクトです。

## プロジェクト概要

このリポジトリは、いきなり複雑な画像/動画モデルに進まず、まずは表データのベースラインを確立してから段階的に拡張する方針です。

## Quick Start

### 1. 依存パッケージをインストール

```bash
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. ベースライン学習を実行

```bash
python scripts/train_baseline.py
```

実行例:

```text
=== Baseline Training Result ===
accuracy: 0.5000
train size: 8
test size: 2
```

## 開発ポリシー（要約）

- まずは小さく作る（過剰設計を避ける）
- 重要ロジックは `src/` に置く（notebook 依存にしない）
- 変更理由を説明できるようにする
- 再現性を重視する（同じ手順で実行できる状態を保つ）
- 初学者が読めるコードを優先する

詳細ルールは [AGENTS.md](AGENTS.md) を参照してください。

## 現在のベースライン

- 入力: `data/processed/baseline_sample.csv`
- 学習: `src/keiba_ai/models/train_baseline.py`（RandomForestClassifier）
- 実行入口: `scripts/train_baseline.py`
- データ読み込み: `src/keiba_ai/data/load_data.py`

## ロードマップ（短期）

1. 表データベースラインの安定化（現状）
2. 特徴量エンジニアリングの追加
3. 回収率（ROI）評価の導入
4. パドック画像/動画解析へ拡張

## 主要ディレクトリ（責務ベース）

- `src/keiba_ai/data/`: データ読み込み・保存
- `src/keiba_ai/features/`: 特徴量作成
- `src/keiba_ai/models/`: 学習・推論
- `src/keiba_ai/evaluation/`: 評価指標・評価処理
- `scripts/`: 実行スクリプト
- `tests/`: テスト