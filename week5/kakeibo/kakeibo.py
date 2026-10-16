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