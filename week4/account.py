class Account:
    def __init__(self, balance):
        self._balance = balance
        print("初期残高", self._balance)
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(amount, "円預金されました、残高:", self._balance)
        else:
            print(amount,":預金は正の数にしてください")
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(amount, "円引き出されました、残高:", self._balance)
        else:
            print(amount,":引き出しは正の数、かつ残高以下にしてください")
    def get_balance(self):
        return self._balance