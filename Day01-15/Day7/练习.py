import os
import time
import random

# 练习1： 跑马灯


def house_light(content):
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]

# 练习2：生成验证码


def generate_code(code_len=4):
    code = ''
    all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(0, code_len):
        code += all_char[random.randint(0, len(all_char) - 1)]
    print(code)

# 练习3：获取文件后缀


def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if has_dot:
        suffix = filename[pos:]
    else:
        suffix = filename[pos + 1:]
    print(suffix)

# 练习4： 返回最大的两个数


def max2(_list):
    if _list[0] < _list[1]:
        m1, m2 = _list[1], _list[0]
    else:
        m2, m1 = _list[0], _list[1]

    for index in range(2, len(_list)):
        if _list[index] > m1:
            m2 = m1
            m1 = _list[index]
        elif _list[index] > m2:
            m2 = _list[index]

    print(m1, m2)


def yangThree():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


def print_board(board):
    print(board['TL'] + ' | ' + board['TM'] + ' | ' + board['TR'])
    print('- + - + -')
    print(board['ML'] + ' | ' + board['MM'] + ' | ' + board['MR'])
    print('- + - + -')
    print(board['BL'] + ' | ' + board['BM'] + ' | ' + board['BR'])


def board_game():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }

    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋， 请输入位置： ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
        choise = input('再玩一局?(yes|no)')
        begin = choise == 'yes'


def main():
    # house_light('薛宇建好帅啊好帅啊....')
    # generate_code()
    # get_suffix('test.txt', True)
    # max2([2, 3, 5, 1, 6])
    # yangThree()
    board_game()
    pass


if __name__ == "__main__":
    main()
