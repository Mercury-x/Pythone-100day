"""
    version: 0.1
    author: azoux
"""

# 赌博游戏
import random

money = 1000
count = random.randint(2, 13)
debt = 0
index = 1
breakGame = False

while not breakGame:
    print('您当前有%d元' % (money))
    debt = float(input('请下注：'))
    if debt > money:
        print('你不能下注超过所拥有的金额')
    elif debt < 0:
        print('下注金额不能为负数')
    else:
        count = random.randint(2, 13)
        print('第%d轮你摇出了%d点' % (index, count))
        # first
        if count == 7 and count == 11:
            print('你赢了！')
            money += debt
        elif count == 2 or count == 3 or count == 12:
            print('你输了！')
            money -= debt
        else:
            firstCount = count
            while True:
                index += 1
                count = random.randint(2, 13)
                print('第%d轮你摇出了%d点' % (index, count))
                if count == firstCount:
                    print('你赢了！')
                    money += debt
                    break
                elif count == 7:
                    print('你输了！')
                    money -= debt
                    break
    print('输入no来终止游戏')
    is_continue = input('continue = ? ')
    if is_continue == 'no':
        breakGame = True

    if money == 0:
        print('赌狗是没有未来的...')
        break

print('你当前的余额：%d元' % (money))


# 有用的练习

# 1.生成斐波那契数列

before1 = 1
before2 = 2
counter = int(input('请输入要生成的个数: '))
print('1 1 2 ', end="")
if counter > 3:
    for i in range(2, counter - 1):
        print('%d ' % (before1 + before2), end='')
        before1, before2 = before2, before1 + before2
