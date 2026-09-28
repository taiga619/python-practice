fizzbuzz = 0
while fizzbuzz < 30:
    fizzbuzz += 1
    print(fizzbuzz)
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print("Not Fizz or Buzz")

n = int(input("数字をいくつ入力しますか？"))
total = 0
for i in range(n):
    num = int(input("数字を入力してください"))
    total = total + num
    average = total / (i + 1)
    print("合計は", total, "です")
    print("平均は", average, "です")

correct_password = "jaguar1234"
user_password = input("パスワードを入力してください")

while user_password != correct_password:
    print("パスワードが違います。パスワードを入力しなおしてください")
    user_password = input("パスワードを入力してください")
print("正解です。ログインしました")