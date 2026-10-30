from kakeibo import Kakeibo

k = Kakeibo()
k.add_record("2026-10-16", "食費", "昼ごはん", "expense", 800)
print(k.get_total())
print(k.list_records())
k.save("data.json")

k2 = Kakeibo()
k2.load("data.json")
print(k2.list_records())