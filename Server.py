import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen()

print("Waiting for client connection...")
client, addr = server.accept()
print(f"Client connected from {addr}")

while True:
    # Receive message from the client
    msg = client.recv(1024).decode('utf-8')
    
    if msg.lower() == 'quit':
        print("Client has ended the connection.")
        break
    else:
        print("\nClient: ", msg)
    
    # Send message to the client
    server_msg = input("Enter Msg (type 'quit' to exit): ")
    client.send(server_msg.encode('utf-8'))
    
    if server_msg.lower() == 'quit':
        print("Ending the connection.")
        break

client.close()
server.close()
