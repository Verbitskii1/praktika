# задание 1
# a = int(input())
# b = int(input())
# c = int(input())
# sum = a + b + c
# print(sum)


# задание 2
# a = int(input())
# b = int(input())
# s = 1/2 * a * b
# print(s)


# задание 3
# n = int(input())
# h = n//60%24
# m = n%60
# print(h,m)


# задание 4
# a = int(input())
# b = int(input())
# l = int(input())
# n = int(input())
# print(2 * l + (2 * n - 1) * a + 2 * (n - 1) * b)


# задание 5
# def m(a, b, c):
#     if a <= b and a <= c:
#         return a
#     elif b <= a and b <= c:
#         return b
#     else:
#         return c
# print(m(10, 5, 15))

# def m():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     minimum = min(a, b, c)
#     print(minimum)
# m()


# задание 6
# def ch():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     cl1 = (a + b) % 2
#     cl2 = (c + d) % 2
#     if cl1 == cl2:
#         print('да')
#     else:
#         print('нет')
# ch()


# задание 7
# def y(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return "Да"
#     else:
#         return "Нет"
# print(y(2025))

# def y():
#    year = int(input())
#    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#      print("Да")
#    else:
#      print("Нет")
# y()


# задание 8
# def ct():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     if a == b == c:
#      print(3)
#     elif a == b or a == c or b == c:
#      print(2)
#     else:
#      print(0)
# ct()


# задание 9
# def ch():
#    n = int(input())
#    m = int(input())
#    k = int(input())
#    if k % n == 0 or k % m == 0 and k <= n * m:
#      print("Да")
#    else:
#      print("Нет")
# ch()