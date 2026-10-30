import json

class Kakeibo:
    def __init__(self):
        self._records = []
    def add_record(self, date, genre, title, kind, amount):
        self._records.append({"date": date, "genre": genre, "title": title, "kind": kind, "amount": amount})
    def get_total(self):
        income = 0
        expense = 0
        for record in self._records:
            if(record["kind"] == "income"):
                income += record["amount"]
            elif(record["kind"] == "expense"):
                expense += record["amount"]
        return {"income": income, "expense": expense, "balance": income - expense}
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self._records, f, ensure_ascii=False)
    def load(self,filename):
        with open(filename, "r", encoding="utf-8") as f:
            self._records = json.load(f)
    def list_records(self):
        lines = []
        for i, record in enumerate(self._records, start=1):
            lines.append(f"{i}: {record['date']} {record['genre']} {record['title']} {record['amount']}円 ({record['kind']})")
        return lines
    def delete_record(self, num):
        del self._records[num - 1]