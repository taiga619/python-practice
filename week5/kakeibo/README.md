# 簡易家計簿（kakeibo）

毎日の収入と支出を記録し、合計と残高を確認できるPython製の家計簿ツール。

## 機能

- 収入・支出の記録の追加（`add_record`）
- 合計（収入・支出・残高）の確認（`get_total`）
- 記録の一覧表示（`list_records`）、番号を指定した削除（`delete_record`）
- ファイルへの保存・読み込み（`save` / `load`、JSON形式）

## 使い方

```python
from kakeibo import Kakeibo

k = Kakeibo()
k.add_record("2026-10-16", "食費", "昼ごはん", "expense", 800)
print(k.get_total())       # {'income': 0, 'expense': 800, 'balance': -800}
print(k.list_records())    # ['1: 2026-10-16 食費 昼ごはん 800円 (expense)']
k.save("data.json")

k2 = Kakeibo()
k2.load("data.json")       # 保存したデータを、別のインスタンスに読み込む
```

`add_record` の引数は、`(日付, ジャンル, タイトル, 種別, 金額)` の順。種別は `"income"`（収入）か `"expense"`（支出）。

削除は、`list_records()` で見た番号を渡す。

```python
k.delete_record(1)         # 「1: ...」の記録を消す（後ろの番号は繰り上がる）
```

## テスト

```bash
pytest -v test_kakeibo.py
```

## 学んだこと

- 設計では、まず「何がしたいか」を決め、それをどんな機能で実現するかに落とし込む（要件を必須／あれば良い／やらない、に絞る）
- 記録は辞書のリストで持ち、表示するときに `enumerate` で番号を付け、その番号で削除する
- JSONで辞書のリストを保存・読み込みできる。`"w"` は上書きなので、毎回すべてを保存する設計に合う
