n=int(input("商品数を入力してください"))
items=[]
for i in range(n):
 new_items = input("新しい商品名を入力してください")
 items.append(new_items)
 print("商品リストは",items, "です")

m=int(input("削除したい商品数を入力してください(品数以下に設定してください)"))
for i in range(m):
 del_items = input("削除する商品名を入力してください")
 items.remove(del_items)
 print("商品リストは",items, "です")
 print(del_items in items)

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# apple_count = 0
# banana_count = 0
# orange_count = 0
# for word in words:
#  if word == "apple":
#   apple_count = apple_count + 1
#  elif word == "banana":
#   banana_count = banana_count + 1
#  elif word == "orange":
#   orange_count = orange_count + 1

# print("リンゴの数は", apple_count, "個です")
# print("バナナの数は", banana_count, "個です")
# print("オレンジの数は", orange_count, "個です") 

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = {}
for word in words:
    if word in count:
      count[word] = count[word] + 1
    else:
      count[word] = 1
for keys, values in count.items():
    print(keys, ":", values)

del count["banana"]
print("バナナ削除後のリストは", count)