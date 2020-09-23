import time
import json
import requests


def read_file():
    # 这里读取readme就可以读到是因为我这里使用的是相对路径，相对路径相对的是我打开的文件夹
    # f = open('README.md', 'r', encoding='utf-8')

    # 我这里打开的文件夹是python-100day，所以可以读取到readme
    # fine....
    # f = open('./Day01-15/Day11/test.txt', 'r', encoding='utf-8')

    # 然后我在launch.json里面修改了cwd就可以愉快的使用相对路径了~~
    f = open('test.txt', 'r')
    print(f.read())
    f.close()
    # print(sys.path)


def read_file_plus():
    f = None
    try:
        f = open('test.txt', 'r')
        print(f.read())
    except FileExistsError:
        print('无法打开指定文件')
    finally:
        if f:
            f.close()


def read_all_file():
    with open('test.txt', 'r') as f:
        print(f.read())


def read_by_line():
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        for line in f:
            print(line, end="")
            time.sleep(0.5)
        print(lines)


def read_json():
    try:
        with open('test.json', 'r') as fs:
            print(fs.read())
    finally:
        fs.close()


def get_requests():
    res = requests.get(
        'https://www.fastmock.site/mock/a87648211a97366ddfb7a840aeecd11e/proj01/user/getUserInfo')
    data_model = json.loads(res.text)
    for news in data_model:
        print(news)
    print(data_model)


def main():
    # read_all_file()
    # read_by_line()
    # read_file_plus()
    # read_json()
    get_requests()
    pass


if __name__ == "__main__":
    main()
    pass
