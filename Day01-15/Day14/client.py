from socket import socket


def main():
    client = socket()
    client.connect(('192.168.0.113', 6389))
    print(client.recv(1024).decode('utf-8'))
    pass


if __name__ == "__main__":
    main()
