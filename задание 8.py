# задание 1
# подзадача 1
# def ar(f,d):
#     if f == 'круг':
#         res = 3.14*(d[0]**2)
#     if f == 'квадрат':
#         a,b = d
#         res = a*b
#     if f == 'треугольник':
#         a,b = d
#         res = (a*b)/2
#     return 'ar {} = {}'.format(f,res)
# f = input('фигуры:')
# d = [float(i) for i in input('значение:').rsplit()]
# print(ar(f,d))
# подзадача 2
# def ar(*arrays, res=[]):
#     for arr in arrays:
#         summ, arf = sum(arr), sum(arr) / len(arr)
#         res.append((summ, arf))
#     return res
# print(ar([1, 2, 3], [4, 5, 7], [3, 5, 8]))

# задание 2
# подзадача 1
# a = int(input())
# def art(a):
#     return pow(a, 2) * pow(3, 0.5) / 4
# def arh(a):
#     return art(a) * 6
# print(arh(a))
# подзадача 2
# def sp(a, b):
#     return a * b
# fa, fb = map(int, input('Введите стороны первого прямоугольника: ').split())
# sa, sb = map(int, input('Введите стороны второго прямоугольника: ').split())
# ta, tb = map(int, input('Введите стороны третьего прямоугольника: ').split())
# print('Площадь первого прямоугольника: ' + str(sp(fa, fb)))
# print('Площадь второго прямоугольника: ' + str(sp(sa, sb)))
# print('Площадь третьего прямоугольника: ' + str(sp(ta, tb)))

# задание 3
# подзадача 1
# def g2(x, y):
#     return x ** 2 + y ** 2
# a1, b1 = map(float, input("Катеты первого треугольника a1, b1 = ").split())
# a2, b2 = map(float, input("Катеты второго треугольника a2, b2 = ").split())
# c1 = g2(a1, b1)
# c2 = g2(a2, b2)
# if c1 == c2:
#     print("Гипотенузы равны")
# else:
#     print("Гипотенуза первого треугольника больше" if c1 > c2 else "Гипотенуза второго треугольника больше")
# подзадача 2
# s = 'cba cba cba'
# print(' '.join(''.join(sorted(x)) for x in s.split()))
# задание 4
# подзадача 1
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# a, b, c, d = map(int, input().split())
# x = a * d
# y = b * c
# t = gcd(x, y)
# print(x // t, '/', y // t, sep='')
#2 подзадача
# def i(x, y, a, b, R):
#     return (x - a)**2 + (y - b)**2 < R**2
# a, b, R = map(float, input().split())
# p1, p2 = map(float, input().split())
# f1, f2 = map(float, input().split())
# l1, l2 = map(float, input().split())
# p = [(p1, p2), (f1, f2), (l1, l2)]
# c = sum(1 for x, y in p if i(x, y, a, b, R))
# print(f"{c}")

# задание 5
# подзадача 1
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# a, b, c, d = map(int, input().split())
# x = a * d
# y = b * c
# t = gcd(x, y)
# print(x // t, '/', y // t, sep='')
# подзадача 2
# def f(n):
#     d = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             d.append(str(i))
#     print(' '.join(d))
# nm = int(input('введите число:'))
# f(nm)

# задание 6
# подзадача 1
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# a = int(input())
# b = int(input())
# print(gcd(a, b))
# print((a * b) // gcd(a, b))

# задание 7
# подзадача 1
# from math import *
# X, Y, Z, T = map(float, input().split())
# a1 = 0.5 * X * Y
# diag = sqrt(X*X + Y*Y)
# p = (Z + T + diag) / 2
# a2 = sqrt(p * (p - Z) * (p - T) * (p - diag))
# print(f" {a1 + a2:.2f}")
# подзадача 2
# n = int(input())
# oc = oct(n)[2:]
# r = oc.zfill(10)
# print(r)