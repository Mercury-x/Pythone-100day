"""
    version: 0.1
    author: azoux
"""

# 分段函数求值

x = float(input('x = '))
if x < -1:
    y = 5*x + 3
elif x <= 1:
    y = x + 2
else:
    y = 3*x - 5

print(y)


# 分支这方面只要记得同一个代码块的缩进要一样就可以了
# 几个空格都可以，但是我用的lint工具是四个空格，所以就是四个空格了
