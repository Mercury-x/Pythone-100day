import sys


def str_option():
    print('----------------------str option start--------------------------------')
    str1 = 'hello, world! azoux, only ytes'
    # 通过内置函数len计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!
    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title())  # Hello, World!
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!
    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8 -> r的位置
    print(str1.find('shit'))  # -1
    # 与find类似但找不到子串时会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  azoux@qq.com '
    print(str3)
    # 获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())
    print('----------------------str option end----------------------------------')


def array():
    list_1 = [1, 2, 3, 'asd']
    for i in list_1:
        print(i, end='')

    print()
    list_2 = ['Hello'] * 3
    for index, elem in enumerate(list_2):  # 用enumerate函数处理之后可以得到index
        print(f'list_2[{index}] = {elem}')

    print(list_2)


def list_option():
    list_1 = [1, 2, 3, 4]
    list_1.append('test')  # push
    print(list_1)
    list_1.insert(2, 'test2')  # 指定位置插入
    print(list_1)

    list_1.pop(len(list_1) - 1)
    list_1.pop(2)  # 指定位置
    print(list_1)

    list_1.clear()
    print(list_1)


def sort():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, reverse=False, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


def generator_obj():
    # 生成式 和 生成器
    f = [x for x in range(1, 10)]
    print(f)
    f2 = [x + y for x in range(1, 10) for y in range(10, 1, -1)]
    print(f2)
    print(sys.getsizeof(f2))

    f3 = (x ** 2 for x in range(1, 100))
    # f3 output: <generator object generator_obj.<locals>.<genexpr> at 0x000001E861547660>
    print(f3)
    for val in f3:
        print(val)

    data = '1234'
    for index in range(len(data)-1, -1, -1):
        print(index)


def _turple():
    t = ('azoux', 19, ('azoux2', 1919), ['list1'])
    print(t[3][0])
    list_1 = list(t)
    print(list_1)


def _set():
    set1 = {1, 2, 3, 1}
    print(set1)
    set2 = set(range(1, 10))

    set2.update([10])  # update只能用 [] 来添加
    print(set2)

    # 集合的并、交、补、对称差
    print(set1 & set2)
    print(set1 | set2)
    print(set2 - set1)
    print(set1 ^ set2)

    print(set2 <= set1)


def _dict():
    # 字典
    scores = {
        'name': 'azoux',
        'age': 19,
    }
    print(scores['name'])
    item2 = dict(zip(['a', 2, 'c', 'd'], [1, 2, 3, 5]))
    print(item2)


def main():
    # print(r'\/\/\/\/\/He;;p/n')  # 加上r后面的/就都不会转义
    # print('\n\\Hello world\\\n')

    # str = 'Hello world, I am azoux!'
    # print(str[2])  # 字符串切片
    # print(str[2:])
    # print(str[2:5])
    # print(str[2::2])
    # print(str[::2])
    # print(str[-1::-2])

    # str_option()

    # 简洁地打印字符串
    # a, b = 5, 10
    # print('{0} * {1} = {2}'.format(a, b, a * b))
    # print(f'{a} * {b} = {a * b}')  # 类似JavaScript的模板字符串

    # 列表
    # array()
    # list_option()

    # 列表也可以做切片操作,会返回处理完的列表

    # 排序
    # sort()

    # 生成式和生成器
    # generator_obj()

    # 元组
    # _turple()

    # 集合
    # _set()

    # 字典
    _dict()

    pass


if __name__ == "__main__":
    main()
