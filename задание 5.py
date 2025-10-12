# задание 1
# n = int(input())
# f = 1
# while f ** 2 <= n:
#     print(f **2 )
#     f+=1


# задание 2
# n = int(input())
# i = 1
# while i  <= n:
#     i = i + 1
#     if n % i == 0:
#         print(i)
#         break


# задание 3
# n = int(input())
# i = 1
# while 2 ** i <= n:
#     i += 1
#     print(i - 1,2 ** (i - 1))


# задание 4
# x = int(input())
# y = int(input())
# d = 0
# while y - x > 0:
#     x = x + (x * 0.1)
#     d += 1
# print(d)


# задание 5
# n = []
# while(True):
#     x = int(input())
#     if x == 0:
#         break
#     n.append(x)
# print(len(n))


# задание 6
# s = 0
# l = 0
# el = int(input())
# while el != 0:
#     s += el
#     l +=1
#     el = int(input())
# print(s / l)


# задание 7
# n = int(input())
# x = 0
# while n != 0:
#     f = int(input())
#     if f != 0 and n < f:
#         x += 1
#     n = f
# print(x)


# задание 8
# n = int(input())
# c = 1
# b = 1
# while n != 0:
#     v = int(input())
#     if v == n:
#         if v == 0:
#             break
#         c += 1
#     else:
#         if c > b:
#             b = c
#         n = v
#         c = 1
# print(b)
