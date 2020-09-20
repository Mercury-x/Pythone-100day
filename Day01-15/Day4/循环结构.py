"""
version: 0.1
author: azoux
"""


# python构建循环结构有两种做法，一种是for in ， 另一种是while
# break 可以提前终止循环

# for in
# for x in range(1, 10, 2):  # 其中2是步长，可以是负数
#     print(x)

# while
# 猜数游戏

# import random

# answer = random.randint(1, 100)
# count = -1
# counter = 0

# while count != answer:
#     count = int(input('count = '))
#     counter += 1
#     if count > answer:
#         print('太大了')
#     else:
#         print('太小了')

# print('猜对啦~！')
# print('你一共猜了%d次' % (counter))

# 练习1：判断一个正整数是不是素数
# from math import sqrt
# x = int(input('x = '))
# end = int(sqrt(x))
# flag = True

# for i in range(2, end):
#     if x % i == 0:
#         flag = False
#         break

# if flag:
#     print('%d是素数' % (x))
# else:
#     print('%d不是素数' % (x))


# 练习2： 计算两个正整数的最大公约数和最小公倍数
# x = int(input('x = '))
# y = int(input('y = '))

# if x > y:
#     x, y = y, x

# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, i))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // i))
#         break


# 练习3： 打印三角形
star = '*'
line = 4
space = int(line / 2) + 2
for i in range(1, line + 1):
    for j in range(1, space):
        print(end=' ')
    space -= 1
    print(star)
    star += '*'
