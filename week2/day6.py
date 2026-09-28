name = "太雅"
age = 28
height = 174.3
is_sutend = False
print(type(name), type(age), type(height), type(is_sutend))

price_str = input("商品の値段を入力してください")
price = int(price_str)
quantity_str = input("商品の個数を入力してください")
quantity = int(quantity_str)
total = price * quantity
print(f"合計金額は{total}円です")

tax_rate = 0.1
total_with_tax = total * (1 + tax_rate)
print(f"税込み価格は{total_with_tax}円です")

is_expensive = total_with_tax > 5000
print(f"5000円超えているか：{is_expensive}")