# class Account:
#     def __init__(self, balance):
#         self.balance = balance

# acct = Account(1000)
# acct.balance -= 5000
# print("悪い場合", acct.balance)

# class Account:
#     def __init__(self, balance):
#         self._balance = balance
#         print("初期残高", self._balance)
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(amount, "円預金されました、残高:", self._balance)
#         else:
#              print(amount,":預金は正の数にしてください")
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self._balance:
#             self._balance -= amount
#             print(amount, "円引き出されました、残高:", self._balance)
#         else:
#             print(amount,":引き出しは正の数、かつ残高以下にしてください")
#     def get_balance(self):
#             return self._balance
#             print("残高:", self._balance)

# acct = Account(1000)
# acct.deposit(500)
# acct.deposit(-100)
# acct.withdraw(300)
# acct.withdraw(99999)
# print("残高", acct.get_balance())

# class Score_manager:
#     def __init__(self):
#         self.scores = []
#     def add_score(self, score):
#         self.scores.append(score)
#     def calc_average(self):
#         return sum(self.scores) / len(self.scores)
#     def judge(self):
#         avg = self.calc_average()
#         if avg >= 80:
#             return "優"
#         elif avg >= 60:
#             return "良"
#         else:
#             return "不可"
#     def print_report(self):
#         print("=== 成績レポート ===")
#         for s in self.scores:
#             print("点数:", s)
#         print("平均:", self.calc_average())
#         print("評価:", self.judge())

# manager = ScoreManager()
# manager.add_score(70)
# manager.add_score(90)
# manager.print_report()

class ScoreBook:
    def __init__(self):
        self.scores = []
    def add_score(self, score):
        self.scores.append(score)
    def calc_average(self):
        return sum(self.scores) / len(self.scores)
    def judge(self):
        avg = self.calc_average()
        if avg >= 80:
            return "優"
        elif avg >= 60:
            return "良"
        else:
            return "不可"
class Reporter:
    def print_report(self, book):
        print("=== 成績レポート ===")
        for s in book.scores:
            print("点数:", s)
        print("平均:", book.calc_average())
        print("評価:", book.judge())

book = ScoreBook()
book.add_score(70)
book.add_score(90)
reporter = Reporter()
reporter.print_report(book)

# お題3
# 1. カプセル化とは：
#    インスタンスの属性に外部から直接値を代入するのではなく、メソッドを経由して代入する設計思想。
#    メソッドの中のifチェックで不正な値を弾けるので、やらないと不正な値が入っても通ってしまう。
#    (例：Accountで bad.balance -= 999999 と直接書き換えたら、残高が -998999 になった)
# 2. 責務が明確な設計のよさ：
#    責務が明確だと、必要箇所のみの修正で対応でき、不具合の原因も特定しやすくなる。
#    例えば、出力レポートの形式を変えるときは、Reporterクラスだけの修正で済み、ScoreBookには触れずに済んだ。
#    (そうでないと、無関係な機能まで一緒に壊す可能性がある)