import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.226.136', 9999))

while True:
    # Send message to the server
    msg = input("Enter Msg (type 'quit' to exit): ")
    client.send(msg.encode('utf-8'))

    if msg.lower() == 'quit':
        print("Ending the connection.")
        break
    
    # Receive message from the server
    server_msg = client.recv(1024).decode('utf-8')
    if server_msg.lower() == 'quit':
        print("Server has ended the connection.")
        break
    else:
        print("\nServer: ", server_msg)

client.close()
