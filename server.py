#* import all the required modules
import socket
import threading

HOST = '127.0.0.1'
#* any port between 0 and 65535
PORT = 1234
LISTENER_LIMIT = 5

#* main function
def main():
    #* creating the server socket class object
    #* AF_INET: uses the IPv4 addresses
    #* SOCK_STREAM: use the TCP packets for the communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #* bind the HOST and PORT to the server
    try:
        #* pass a tuple into the server bind method
        server.bind((HOST, PORT))
        print(f"Server is listening on {HOST}:{PORT}")
    except:
        print(f"Unable to find to host {HOST} and port {PORT}")

    #* set a server client connection limit
    server.listen(LISTENER_LIMIT)

    #* while loop to keep listening to client connections
    while True:
        #* address is a tuple with (HOST, PORT)
        client, address = server.accept()
        print(f"Connection established with {address}")

if __name__ == "__main__":
    main()