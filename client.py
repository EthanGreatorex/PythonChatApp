#* import all the required modules
import socket
import threading

HOST_TARGET = '127.0.0.1'
PORT_TARGET = 1234

def main():
    #* create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #* connect to the server
    try:
        client.connect((HOST_TARGET, PORT_TARGET))
        print(f"Connected to {HOST_TARGET}:{PORT_TARGET}")
    except:
        print(f"Unable to connect to {HOST_TARGET}:{PORT_TARGET}")


if __name__ == "__main__":
    main()