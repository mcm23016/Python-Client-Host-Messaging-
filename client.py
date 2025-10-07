# client.py
import socket
import threading

'''
# Use the below for automatic connecting.
HOST = '127.0.0.1'  # Change to the host/server IP
PORT = 65432
'''

def receive(client):
    # If a message is recieved, print it
    while True:
        try:
            message = (client.recv(1024)).decode()
            if message:
                print(f"\n {message}")
        except:
            print("[!] Disconnected from server")
            break

def send(client, username):
    # If input is given, send a message
    while True:
        message = (f"{username}: {input()}").encode()
        client.sendall(message)

def main():
    # Get Server IP and Port
    HOST = input("Enter Host IP address: ")
    PORT = int(input("Enter the Port number: "))

    # Get client's username for session
    username = input("Enter your username: ")

    # Make the connection to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print("Connected to the server!")
    except:
        print("Error connecting to server!")

    # Create threads for sending and receiving date
    recv_thread = threading.Thread(target=receive, args=(client,))
    recv_thread.start()

    send_thread = threading.Thread(target=send, args=(client, username,))
    send_thread.start()

if __name__ == "__main__":
    main()