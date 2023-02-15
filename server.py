import socket
import os


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(5)

    print('[+] Server started')

    client_sockets = []

    while True:
        client_socket, client_address = server_socket.accept()
        client_sockets.append(client_socket)
        print(f'[+] Client connected: {client_address}')

        current_client_index = 0
        current_client_socket = client_sockets[current_client_index]
        print(f'[+] Switched to client 0')

        while True:
            message = input('>> ')

            if message.startswith('switch'):
                try:
                    client_index = int(message.split()[1])
                    current_client_socket = client_sockets[client_index]
                    current_client_index = client_index
                    print(f'[+] Switched to client {client_index}')
                except (ValueError, IndexError):
                    print('[-] Invalid client index')
                continue

            if message.startswith('cmd'):
                command = message.split(maxsplit=1)[1]
                current_client_socket.send(command.encode())
                output = current_client_socket.recv(1024).decode()
                print(output)
                continue

            print('[-] Invalid command')


if __name__ == '__main__':
    start_server()
