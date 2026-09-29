# stack_list = []
# word = input("()を含む文字列を入力してください")
# is_valid = "True"

# for char in word:
#     if char == "(":
#         stack_list.append(char)
#     elif char == ")":
#         if (len(stack_list) != 0) and (is_valid == "True"):
#             stack_list.pop()
#         else:
#             is_valid = "False"
#     print(stack_list)

# if (len(stack_list) == 0) and (is_valid == "True"):
#     print("True")
# else:
#     print("False")

from collections import deque
queue = deque()
n = int(input("入力人数を設定してください"))

for i in range(n):
    name = input("名前を入力してください")
    queue.append(name)

for j in range(n):
    call_name = queue.popleft()
    print(call_name, "さん、どうぞ")