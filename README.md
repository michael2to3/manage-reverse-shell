# Reverse Shell Manager Server

This is a simple Python-based reverse shell manager server that allows you to manage multiple reverse shell clients. The server runs on your local machine and listens for incoming connections from reverse shell clients. Once a client connects, the server allows you to switch between connected clients and execute shell commands on them remotely.
## Requirements
- Python 3.x

## Installation
- Clone this repository to your local machine.
- Open a terminal and navigate to the cloned repository directory.
- Start the server by running the following command: python server.py
- This will start the server and listen for incoming connections on port 8888.

## Usage

Once the server is running, you can connect to it using a reverse shell client. You can use the nc command to connect to the server from a remote machine. For example:

```bash
nc localhost 8888
```

This will connect to the server and open a reverse shell on the remote machine. You can then use the following commands to manage the connected clients:
- switch {INDEX CLIENT}: Switch to the client with the specified index. For example, switch 2 will switch to the second connected client.
- cmd {COMMAND}: Execute the specified command on the current client and display the output.

Note that the cmd command is executed on the current client, so you must first switch to the desired client using the switch command.
## License

This project is licensed under the MIT License.
## Acknowledgments

This project was inspired by various other reverse shell manager implementations. Special thanks to the following resources:
- [Black Hat Python by Justin Seitz](https://nostarch.com/black-hat-python2E)
- [A Reverse Shell Cheat Sheet by HighOn.Coffee](https://highon.coffee/blog/reverse-shell-cheat-sheet/)
