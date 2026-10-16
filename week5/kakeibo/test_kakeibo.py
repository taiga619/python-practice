from kakeibo import Kakeibo

def test_get_total():
    k = Kakeibo()
    k.add_record("2026-10-16", "臨時収入", "バイト", "income", 5000)
    k.add_record("2026-10-16", "食費", "昼ごはん", "expense", 800)
    assert k.get_total() == {"income": 5000, "expense": 800, "balance": 4200}