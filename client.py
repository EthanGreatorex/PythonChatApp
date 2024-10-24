import socket
import threading

HOST_TARGET = '127.0.0.1'
PORT_TARGET = 1234


# * Function to handle receiving messages from the server
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                #* If the server closes the connection
                print("Connection closed by the server.")
                break
        except:
            print("Error occurred while receiving message.")
            break


# * Function to handle sending messages to the server
def send_messages(client):
    while True:
        message = input()
        client.send(message.encode('utf-8'))


# * Main client function
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST_TARGET, PORT_TARGET))
        print(f"Connected to {HOST_TARGET}:{PORT_TARGET}")

        # * Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.start()

        # * Send the username to the server
        username = input("Enter your username: ")
        client.send(username.encode('utf-8'))

        # * Start a thread to send messages to the server
        send_thread = threading.Thread(target=send_messages, args=(client,))
        send_thread.start()

    except Exception as e:
        print(f"Unable to connect to {HOST_TARGET}:{PORT_TARGET}. Error: {str(e)}")


if __name__ == "__main__":
    main()
