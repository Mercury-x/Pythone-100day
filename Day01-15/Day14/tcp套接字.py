from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1. 创建套接字对象并指定使用哪种传输服务
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. 绑定IP地址和端口
    server.bind(('192.168.0.113', 6389))
    # 3. 开启监听
    server.listen(512)  # 512可以理解为连接队列的大小
    print('server start...')
    while True:
        # 这里按了ctrl + c 会停止，但是不知道为啥控制台没有显示
        client, addr = server.accept()
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()
    pass


if __name__ == "__main__":
    main()
