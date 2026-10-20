from kakeibo import Kakeibo

def test_get_total():
    k = Kakeibo()
    k.add_record("2026-10-16", "臨時収入", "バイト", "income", 5000)
    k.add_record("2026-10-16", "食費", "昼ごはん", "expense", 800)
    assert k.get_total() == {"income": 5000, "expense": 800, "balance": 4200}

def test_save_and_load(tmp_path):
    k = Kakeibo()
    k.add_record("2026-10-16", "食費", "昼ごはん", "expense", 800)
    path = tmp_path / "data.json"
    k.save(path)
    k2 = Kakeibo()
    k2.load(path)
    assert k2.get_total() == k.get_total()

def test_list_records():
    k = Kakeibo()
    k.add_record("2026-10-15", "臨時収入", "ボーナス", "income", 1200)
    k.add_record("2026-10-16", "食費", "昼ごはん", "expense", 800)
    assert k.list_records() == ["1: 2026-10-15 臨時収入 ボーナス 1200円 (income)", "2: 2026-10-16 食費 昼ごはん 800円 (expense)"]

def test_delete_record():
    k = Kakeibo()
    k.add_record("2026-10-15", "臨時収入", "ボーナス", "income", 1200)
    k.add_record("2026-10-16", "食費", "昼ごはん", "expense", 800)
    k.delete_record(1)
    assert k.list_records() == ["1: 2026-10-16 食費 昼ごはん 800円 (expense)"]