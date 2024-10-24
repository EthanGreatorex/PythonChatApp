import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
clients = []  #* List to keep track of all connected clients


# * Broadcast messages to all connected clients
def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:  #* Don't send the message to the sender
            try:
                client.send(message)
            except:
                #* Remove client if unable to send message
                clients.remove(client)


# * Handle individual client connections
def handle_client(client, address):
    print(f"Connection established with {address}")

    # * Receive and set username
    username = client.recv(1024).decode('utf-8')
    print(f"{username} has joined the chat!")
    broadcast(f"{username} has joined the chat!\n".encode('utf-8'), client)

    # * Handle messages sent by the client
    while True:
        try:
            message = client.recv(1024)
            if message:
                # * Format the message with time and username
                current_time = datetime.now().strftime("%H:%M")
                formatted_message = f"({current_time} {username}) {message.decode('utf-8')}"
                print(formatted_message)
                broadcast(formatted_message.encode('utf-8'), client)
            else:
                #* If client disconnects, break the loop
                print(f"{username} has disconnected.")
                clients.remove(client)
                broadcast(f"{username} has left the chat.\n".encode('utf-8'), client)
                break
        except:
            #* Handle exceptions (e.g., client disconnects)
            clients.remove(client)
            print(f"{username} has disconnected.")
            broadcast(f"{username} has left the chat.\n".encode('utf-8'), client)
            break


# * Main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Server is listening on {HOST}:{PORT}")
    except Exception as e:
        print(f"Unable to bind to host {HOST} and port {PORT}. Error: {e}")
        return

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()


if __name__ == "__main__":
    main()
