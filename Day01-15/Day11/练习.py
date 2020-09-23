from math import sqrt
# 练习写入三个文件


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    filename = ['a.txt', 'b.txt', 'c.txt']
    file_list = []
    try:
        for f in filename:
            file_list.append(open(f, 'w'))

        for i in range(1, 10000):
            if is_prime(i):
                if i < 100:
                    file_list[0].write(str(i) + '  ')
                elif i < 1000:
                    file_list[1].write(str(i) + '  ')
                else:
                    file_list[2].write(str(i) + '  ')
    except IOError as ex:
        print(ex)
    finally:
        for fs in file_list:
            fs.close()
    print('操作完成')
    pass


if __name__ == "__main__":
    main()
    pass
