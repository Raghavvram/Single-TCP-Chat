This script implements the client-side counterpart of a simple TCP communication system using Python's `socket` module. The client connects to a server, sends and receives messages, and can terminate the connection by sending or receiving the message `'quit'`.

### Code Explanation:

```python
import socket
```
- **Imports the `socket` module**: This provides access to the network interfaces, allowing you to create sockets and establish network connections.

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- **Creates a client socket**:
  - `AF_INET` sets the address family to IPv4.
  - `SOCK_STREAM` sets the socket type to TCP, which is connection-oriented and reliable.

```python
client.connect(('192.168.226.136', 9999))
```
- **Connects to the server**:
  - The client connects to the server running at IP address `'192.168.226.136'` on port `9999`.
  - This IP address should be the server's IP, and port `9999` must be the one on which the server is listening.

```python
while True:
```
- **Starts an infinite loop**: This loop is used to facilitate continuous message exchanges between the client and the server.

```python
    msg = input("Enter Msg (type 'quit' to exit): ")
```
- **Takes input from the user**:
  - The user is prompted to enter a message. If the user wants to terminate the connection, they can type `'quit'`.

```python
    client.send(msg.encode('utf-8'))
```
- **Sends the message to the server**:
  - The user's message is encoded into a UTF-8 byte stream and sent to the server via the socket.

```python
    if msg.lower() == 'quit':
        print("Ending the connection.")
        break
```
- **Checks if the user wants to end the connection**:
  - If the message is `'quit'` (case-insensitive), the client prints a message and exits the loop, ending the connection.

```python
    server_msg = client.recv(1024).decode('utf-8')
```
- **Receives a message from the server**:
  - The client waits to receive a message from the server, reading up to 1024 bytes.
  - The message is then decoded from a UTF-8 byte stream into a string.

```python
    if server_msg.lower() == 'quit':
        print("Server has ended the connection.")
        break
```
- **Checks if the server wants to end the connection**:
  - If the server sends the message `'quit'`, the client prints a message and exits the loop, ending the connection.

```python
    else:
        print("\nServer: ", server_msg)
```
- **Displays the received message from the server**.

```python
client.close()
```
- **Closes the client socket**: This releases the resources allocated to the socket and formally closes the connection.

---

### Documentation:

#### Overview
This script acts as the client-side of a basic TCP communication system. It connects to a server via a specified IP address and port, exchanges messages, and terminates the connection when either the client or the server sends a `'quit'` message.

#### Functionality
- **Socket Creation**: 
  - A client TCP socket is created using `socket.AF_INET` for IPv4 and `socket.SOCK_STREAM` for TCP connections.
- **Server Connection**: 
  - The client connects to a server running at a specific IP address (in this case, `'192.168.226.136'`) and port (`9999`).
- **Communication Loop**:
  - The client enters an infinite loop where it sends messages to the server and receives replies.
  - If either the client or server sends `'quit'`, the connection is terminated.
- **Cleanup**: 
  - After communication ends, the socket is properly closed.

#### Example Usage
1. Run the server script on one machine.
2. Run this client script on another machine or the same machine, specifying the server’s IP and port in the `client.connect()` line.
3. The client can send messages to the server, and both parties can exchange messages until one sends `'quit'` to end the communication.

#### Notes:
- Ensure the client IP and port match the server’s IP and port to establish the connection.
- If the server is running behind a firewall or router, proper port forwarding or firewall rules might be required.
