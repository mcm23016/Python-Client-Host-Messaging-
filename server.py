# Server.py

#import libraries to make it work
import socket
import threading

# Local Port 
'''
0.0.0.0 is for "All interfaces"
192.168.1.10 is "Specific interface"

I am not sure what entirely either of these implicate,
so I have using local as I assume that is the safest for me to use.
''' 
HOST = "127.0.0.1"      # This host IP only allows connections on the same machine.
PORT = 65432            # A port (Make sure above 1024).

# List of clients
clients = []

# Functions to thread (Important to keep conection alive. Don't time out clients)
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break
    print(f"{client_socket.getpeername()} disconected.")
    clients.remove(client_socket)
    client_socket.close()
    

# Broadcast sends a message to all users except the user who sent it.
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message)
            except:
                print(f"{client.getpeername()} disconected.")
                clients.remove(client)
                

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Server started on {HOST}:{PORT}")

        while True:    
            # Accept the client and log them joining
            client_socket, addr = s.accept()
            log = f"{addr} connected."
            print(log)

            # Add client to the client list
            clients.append(client_socket)
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()

if __name__ == "__main__":
    main()