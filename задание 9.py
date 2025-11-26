#задание 1
#1 подзадача
# N = 3
# A = [[1, -2, 3],
#      [4, 5, -6],
#      [7, 8, 9]]
# count = 0
# total = 0
# for i in range(N):
#     for j in range(i + 1, N):
#         if A[i][j] > 0:
#             count += 1
#             total += A[i][j]
# print(f"Сумма: {total}, Количество: {count}")
#2 подзадача
# import random
# def task2():
#     N, M = 4, 6
#     B = [[random.randint(-10, 10) for _ in range(M)] for _ in range(N)]
#
#     print("\nИсходная матрица B:")
#     for row in B:
#         print(row)
#
#     for i in range(N):
#         row = B[i]
#         min_idx = row.index(min(row))
#         max_idx = row.index(max(row))
#
#         row[min_idx], row[-1] = row[-1], row[min_idx]
#         row[max_idx], row[0] = row[0], row[max_idx]
#
#     print("\nМатрица B после преобразований:")
#     for row in B:
#         print(row)
# task2()


#задание 2
# 1 подзадача
# def is_magic(matrix):
#     summ = sum(matrix[0])
#     for i in range(len(matrix)):
#         temp = 0
#         for j in range(len(matrix)):
#             temp += matrix[j][i]
#         if temp != summ or sum(matrix[i]) != summ:
#             return False
#     return True
#
#
# mat = [[4, 3, 3], [3, 4, 3], [3, 3, 4]]
# print(is_magic(mat))
#
# mat = [[4, 3, 4], [3, 4, 3], [3, 3, 4]]
# print(is_magic(mat))
# 2 подзадача
# N = 3
# M = 4
# A = [
# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9,10,11,12]]
# for i in range(N):
#     tmp = A[i][0]
#     A[i][0] = A[i][M-1]
#     A[i][M-1] = tmp
# for i in range(N):
#     for j in range(M):
#         print("%2d " % A[i][j], end='')
#     print()

#задание 3
# 1 подзадача
# N = 3
# A = [
# [1, 2, 3],
# [2, 5, 6],
# [3, 6, 4]]
# b = "YES"
# for i in range(N):
#     for j in range(N):
#         if A[i][j] != A[j][i]:
#             b = "NO"
#             break
# print(b)
# 2 подзадача
# n = int(input("Введите количество строк: "))
# matrix = [[int(j) for j in input("Введите все элементы одной строки (разделенные пробелом): ").split()] for i in range(n)]
# print("Твоя матрица : ", *matrix, sep='\n')
# tmax = matrix[0][0]
# row = col = 0
# for i, v in enumerate(matrix):
#     emax = max(v)
#     if emax > tmax:
#         row, col, tmax = i, v.index(emax), emax
#
# matrix[0], matrix[row] = matrix[row], matrix[0]
# for i in range(len(matrix)):
#     matrix[i][0], matrix[i][col] = matrix[i][col], matrix[i][0]
# print("Новая матрица : ", *matrix, sep='\n')
#задание 4
# 1 подзадача
# import random
#
# def task1_simple():
#     n, m = 4, 3
#     matrix = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
#
#     print("Матрица:")
#     for row in matrix:
#         print(row)
#
#     sums = [sum(row) for row in matrix]
#     max_idx = sums.index(max(sums))
#     min_idx = sums.index(min(sums))
#
#     print(f"\nСтрока с наибольшей суммой: {matrix[max_idx]} (сумма: {sums[max_idx]})")
#     print(f"Строка с наименьшей суммой: {matrix[min_idx]} (сумма: {sums[min_idx]})")
# task1_simple()
# 2 подзадача
# import random
#
# def task2_simple():
#     N = 4
#     matrix = [[random.randint(-5, 5) for _ in range(N)] for _ in range(N)]
#
#     print("\nИсходная матрица:")
#     for row in matrix:
#         print(row)
#     for i in range(N):
#         for j in range(N):
#             if matrix[i][j] < 0:
#                 matrix[i][j] = 0
#             elif matrix[i][j] > 0:
#                 matrix[i][j] = 1
#
#     print("\nПосле замены (0 и 1):")
#     for row in matrix:
#         print(row)
#
#     print("\nНижняя треугольная матрица:")
#     for i in range(N):
#         for j in range(N):
#             if i >= j:
#                 print(matrix[i][j], end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
# task2_simple()
#задание 5
# 1 подзадача
# from random import randint
#
# N, M = 3, 4
# a = [[randint(-50, 50) for _ in range(M)] for _ in range(N)]
# for i in a:
#     print(*sorted(i))
# 2 подзадача
# import random
# n = int(input("Введите количество строк (n): "))
# m = int(input("Введите количество столбцов (m): "))
# matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]
# flat_list = [item for sublist in matrix for item in sublist]
# while len(set(flat_list)) != n * m:
#     matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]
#     flat_list = [item for sublist in matrix for item in sublist]
# print("Исходная матрица:")
# for row in matrix:
#     print(row)
# for i in range(n):
#     min_value = min(matrix[i])
#     min_index = matrix[i].index(min_value)
#     if min_value % 2 == 0:
#         matrix[i][min_index] = 0
#     else:
#         matrix[i][min_index] = 1
# print("\nПреобразованная матрица:")
# for row in matrix:
#     print(row)
#задание 6
# 1 подзадача
# from random import randint
# m = int(input("Введите количество строк"))
# n = int(input("Введите количество столбцов"))
# print("Элементы массива:")
# a = [[randint(1, 21) for j in range(n)] for i in range(m)]
# for i in range(m):
#     print(a[i], max(a[i]))
# for i in range(n):
#     x = [x[i] for x in a]
#     print(min(x), end=" ")
# # 2 подзадача

#задание 7
# 1 подзадача
# n = 3
# mas = []
# i = 0
# j = 0
# while i < n:
#     b = []
#     i += 1
#     while j < n:
#         j += 1
#         if j >= i:
#             print("Введите [", i, ",", j, "] элемент")
#             b.append(int(input()))
#         else:
#             print(end=" ")
#         mas.append(b)
# i = 1
# while i < n:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         mas[i][j] = mas[j][i]
# print("Полученная матрица: ")
# while i < n:
#     i += 1
#     while j < i:
#         j += 1
#         print(mas[i][j], end=" ")
#     print()
# 2 подзадача
# n = int( input( 'Размер матрицы: ' ) )
# k = (n*n - n)//2 + n
# print( f'Введите {k} элементов матрицы: ' )
# m = []
# for i in range(n):
#     m.append( [0]*n )
#     for j in range(i,n):
#         m[i][j] = int(input() )
# for i in range(n):
#     for j in range(i,n):
#         m[j][i] = m[i][j]
# for row in m:
#    print( row, sep='\t' )
#задание 8
# 1 подзадача
# 2 подзадача
# import random
# N = int(input())
# b =[[random.randint(0, 10) for i in range(N)] for e in range(N)]
# a = np.transpose(b)
# for e in b:
#     print(e)
# print(a)