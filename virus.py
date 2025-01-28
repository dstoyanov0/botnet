import socket
import asyncio

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1111))

    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))

if __name__ == '__main__':
    main()
