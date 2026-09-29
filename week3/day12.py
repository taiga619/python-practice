# def factorial(n):
#     if n <= 0:
#         print("階乗終了")
#         return 1
#     print("n=",n)
#     return n*factorial(n-1)
# print(factorial(6))

# def sum_list(lst):
#     if lst == []:
#         print("計算終了")
#         return 0
#     return lst[0] +sum_list(lst[1:])
# print(sum_list([1, 2, 3, 4, 5, 10]))

def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]
print(reverse_string("abcdefg"))