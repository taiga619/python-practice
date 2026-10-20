# python-practice

ソフト開発未経験からの異動に備えた、プログラミング基礎の学習記録（2026年9月〜）。

## 構成

| フォルダ | 内容 |
|---|---|
| `week2/` | Python基礎文法（変数・条件分岐・ループ・リスト・辞書・関数） |
| `week3/` | データ構造（スタック・キュー）、木構造・再帰、良いコードの原則 |
| `week4/` | オブジェクト指向（クラス・継承・カプセル化）、pytest、デバッガ |
| `week5/` | C言語の入門（`day21_*.c`）、成果物の簡易家計簿（`kakeibo/`） |

## 成果物

- [`week5/kakeibo/`](week5/kakeibo/README.md)：収入と支出を記録し、合計を確認できる家計簿ツール（pytestのテスト付き）

## 動かし方（Python）

```bash
python -m venv venv
source venv/bin/activate
pip install pytest
cd week5/kakeibo
pytest -v
```
