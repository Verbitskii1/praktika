# задание 1
#1 подзадача
# n = int(input())
# a = []
# for i in range(n):
#     s = input(f'введите элемент {i+1}:')
#     a.append(s)
# mx = max(a)
# print(a[::-1])
# print(mx)
#2 подзадача
# n = [1,2,3,4,5,10,0,0]
# sr = sum(n)/len(n)
# n = [sr if i == 0 else i for i in n]
# print(n)

# задание 2
#1 подзадача
# n = int(input())
# a = []
# for i in range(n):
#     x = int(input("значение:"))
#     a.append(x)
# x = min(a)
# print(f'Минимальный элемент {x} имеет индекс {a.index(x)}')
#2 подзадача
# n = int(input())
# a = []
# for i in range (n):
#     x = int(input(f'значение {i+1}:'))
#     a.append(x)
# pos = [i for i in a if i>0]
# neg = [i for i in a if i <=0]
# print('положительные:',pos)
# print('отрицательные:',neg)

# задание 3
#1 подзадача
# n = int(input())
# a = [int(input(f'значение {i+1}:')) for i in range(n)]
# sm = 0
# for i in range(1,n,2):
#     sm += a[i]
# print(a)
# print(sm)
#2 подзадача
# a = [int(input(f'значение {i+1}:')) for i in range(8)]
# print('начальный массив',a)
# for i in range(8):
#     if a[i] < 15:
#         a[i] *=2
# print('полученный массив',a)

# задание 4
#1 подзадача
# n = int(input())
# a = [int(input(f'значение {i+1}:')) for i in range(n)]
# mx = max(a)
# mxi = a.index(mx)
# print(mx)
# print(mxi)
#2 подзадача
# n = int(input())
# a = [int(input(f'значение {i+1}:')) for i in range(n)]
# nh= [i for i in a if i%2 != 0]
# if not nh:
#     print('нечетных нет')
# else:
#     nh.sort(reverse=True)
#     print(nh)

# задание 5
#1 подзадача
# a = [int(input(f'значение {i+1}:')) for i in range(10)]
# for i in range(9):
#     if a[i] < 0 and a[i+1] < 0:
#         print(f'{a[i]},{a[i+1]}')
#2 подзадача
# a = [int(input(f'значение {i+1}:')) for i in range(10)]
# print(list(set(a)))

# задание 6
#1 подзадача
# a = [int(input(f'значение {i+1}:')) for i in range(10)]
# sr = sum(a)/len(a)
# mx = max(a)
# l = 0
# g = 0
# for i in a:
#     if i < mx:
#         l +=1
#     if i > sr:
#         g += 1
# print(f'среднее арефметическое:{sr}"')
# print(f'макимальное:{mx}')
# print(f'меньше макс:{l}')
# print(f'больше среднего:{g}')
#2 подзадача
# a = [int(input(f'значение {i+1}:')) for i in range(10)]
# sm = sum(i for i in a if i > 5)
# print(a)
# print(sm)

# задание 7
#1 подзадача
# n = int(input())
# a = [int(input(f'значение {i+1}:')) for i in range(n)]
# sm = 0
# pr = 1
# for i in range(n):
#     if i % 2 == 0:
#         sm += a[i]
#     else:
#         pr *=a[i]
# print('сумма с четным числами:',sm)
# print('произведение с нечетными числами:',pr)
#2 подзадача
# n = int(input())
# a = [int(input(f'значение {i+1}:')) for i in range(n)]
# mn = a.index(min(a))
# mx = a.index(max(a))
# print('Изначальный массив',a)
# print('Конечный массив',a[::-1])

# задание 8
#1 подзадача
# from math import *
# n = int(input())
# a = [int(input(f'значение {i+1}:')) for i in range(n)]
# sm = sum(a)
# pr = prod(a)
# print('Сумма:',sm)
# print('Произведение:',pr)
#2 подзадача
# n = int(input())
# a = [int(input(f'значение {i+1}:')) for i in range(n)]
# sr = sum(a)/len(a)
# for i in range(n):
#     if a[i] == 0:
#         a[i] = sr
# print('изначальный массив',a)
# print('среднее арефметическое ',sr)
# print('конечный массив',a)


