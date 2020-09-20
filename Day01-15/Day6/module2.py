def module2():
    print('I am module 2')
    pass


if __name__ == '__main__':
    print('yoyoyo')
    print('I am in module2')

# 直接import整个文件会执行下面的代码，所以需要加一个判断，这样只有不是被引入的时候才会执行下面的代码
