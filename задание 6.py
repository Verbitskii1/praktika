# задание 1
# t = input()
# c = 0
# for w in t.split():
#     if w[0] == "е":
#         c += 1
# print(c)

# задание 2
# t = input()
# nt = t.replace(':','%')
# c  = t.count(':')
# print(nt)
# print(c)

# задание 3
# t = input()
# c = t.count('.')
# t1 = t.replace('.','')
# print(c)

# задание 4
# t = input()
# nt = t.replace('а','о')
# c = t.count('а')
# print(nt)
# print(c)

# задание 5
# t = input()
# nt = t.lower()
# print(nt)

# задание 6
# t = input()
# nt = t.replace('а','')
# c = t.count('а')
# print(nt)
# print(c)

# задание 7
# t = input()
# nt =  t.replace('п','*')
# print(nt)

# задание 8
# t = input()
# w = t.split()
# c = len(w)
# print(c)

# задание 9
# t = input()
# c = t.count('помидор')
# print(c)

# задание 10
# t = input()
# s = " ".join([s[0].upper() + s[1:] for s in t.lower().split()])
# print(s)

# задание 11
# n = input()
# def s(text):
#     m = max(len(seq) for seq in text.split('н') if seq == 'н' * len(seq))
#     new_text = text.replace('!', '.')
#     return m, new_text
# print(n)


# задание 12
# t = input().split()
# for i in t:
#     if i[-1] == 'я':
#         print(i)

# задание 13
# def text_inside_brackets(text):
#     start = text.find('(')
#     end = text.find(')')
#     if start != -1 and end != -1 and start < end:
#         return text[start+1:end]
#     return ''

# задание 14
# t = input().split()
# for i in t:
#     if i[0] == 'а' or i[-1] == 'я':
#         print(i)

# задание 15
# t = input()
# n = 0
# for i in t:
#     if i == 'т':
#         n += 1
# print(n)
