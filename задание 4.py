# задание 1
# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     print(i)

# задание 2
# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a,b+1):
#         print(i)
# else:
#     for j in range(a,b-1,-1):
#         print(j)


# задание 3
# a = int(input())
# b = int(input())
# for i in range(a,b-1,-1):
#     if i % 2 != 0:
#         print(i)


# задание 4
# n = int(input())
# s = 0
# for i in range(n):
#     s += int(input())
# print(s)



# задание 5
# x = 1
# n = int(input())
# while x <= n:
#     x += 1
#     if x!=n:
#         continue
#     print(x**3)

# n = int(input())
# x = 0
# for i in range(1, n + 1):
#     x += i ** 3
# print(x)

# задание 6
# x = 1
# n = int(input())
# for i in range(1, n + 1):
#     x *= i
# print(x)


# задание 7
# n = int(input())
# f = 1
# s = 1
# for i in range(2, n + 1):
#     s += f * i
#     f *=i
# print(s)


# задание 8
# n = int(input())
# for i in range(1,n + 1):
#     for j in range(1,i + 1):
#         print(j,end='')
#     print()


# задание 9
# f1 = f2 = 1
# n = int(input())
# print(f1, f2, end=' ')
# for i in range(2, n):
#     f1, f2 = f2, f1 + f2
#     print(f2, end=' ')


# задание 10
# N = int(input())
# K = int(input())
# if K == 1:
#     a, b = 0, 1
# elif K == 2:
#     a, b = 1, 1
# else:
#     a, b = 1, 1
#     for i in range(3, K + 1):
#         a, b = b, a + b
#
# x = b
# for i in range(1, N):
#     a, b = b, a + b
#     x += b
# print(x)
