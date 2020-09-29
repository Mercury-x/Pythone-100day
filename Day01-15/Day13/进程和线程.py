from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep
from threading import Thread

# 多线程


def download_task(filename):
    print('启动下载进程，进程号{%d}.' % getpid())
    print('开始下载...%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


class DownloadTask(Thread):
    # 通过thred创建自定义多线程
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s' % self._filename)
        sleep_time = randint(5, 10)
        sleep(sleep_time)
        print('%s下载成功..花费了...%d秒' % (self._filename, sleep_time))


def main():
    # start = time()
    # p1 = Process(target=download_task, args=('python.pdf', ))
    # p1.start()
    # p2 = Process(target=download_task, args=('javascript.pdf', ))
    # p2.start()

    # p1.join()
    # p2.join()
    # end = time()
    # print('总耗费%.2f秒' % (end - start))

    # 自定义的多线程：
    t1 = DownloadTask('python.py')
    t2 = DownloadTask('javascript.js')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # 对于IO密集型操作，多线程多进程是很有必要的
    pass


if __name__ == "__main__":
    main()
