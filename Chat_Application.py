# server code
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = []

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break

            print(f"{addr}: {message}")
            broadcast(message, conn)

        except:
            break

    clients.remove(conn)
    conn.close()
    print(f"[DISCONNECTED] {addr}")

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(msg.encode())
            except:
                pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server is running...")

    while True:
        conn, addr = server.accept()
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()

# Client Code
import socket
import threading

SERVER_IP = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

name = input("Enter your name: ")

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            break

def send_messages():
    while True:
        message = input()
        full_msg = f"{name}: {message}"
        client.send(full_msg.encode())

threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
