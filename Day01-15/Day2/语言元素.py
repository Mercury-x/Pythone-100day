"""
  version: 0.1
  author: azoux
"""

# a = 2
# b = 1.2
# c = 'Hello world'
# d = 1 + 5j
# e = False

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d)) # complex
# print(type(e))


"""
  version: 0.2
  author: azoux
"""

# a = 2
# b = 1.2
# c = 'Hello world'
# d = 1 + 5j
# e = False

# print(int(b))
# print(float(a))
# print(str(e))
# print(ord(str(a)))  # ord()进字符串转换成对应的编码

"""
  version: 0.3
  author: azoux
"""

# 输入输出
# a = int(input('a = '))
# b = int(input('b = '))

# print('a = %d' % (a))
# print('b = %d' % (b))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d ** %d = %d' % (a, b, a ** b))  # a^b
# print('%d // %d = %d' % (a, b, a // b))  # a取余b

# %是取余的意思， %f是小数的占位符 %%表示百分号


# 关系运算符
# 值得注意的有 and , or , not

"""
  version: 0.4
  author: azoux
"""

# 练习1 将华氏温度转为摄氏温度
# 公式：$C = (F - 32)/1.8$

# h_temp = float(input('h_temp = '))
# s_temp = (h_temp - 32) / 1.8
# print('%f' % (s_temp))

# 练习2 输入圆的半径计算周长和面积

# PI = 3.14
# r = float(input('r = '))
# print('周长 =  %.2f' % (r * 2 * PI))
# print('面积 =  %.3f' % (r**2 * PI))


# 练习3 输入年份判断是否为闰年

year = int(input('year = '))

if (year % 4 == 0) and (year % 100 != 0):
    print('%d是闰年' % (year))
else:
    if year % 400 == 0:
        print('%d是闰年' % (year))
    else:
        print('%d不是闰年' % (year))
