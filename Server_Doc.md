This Python script implements a basic TCP server using the `socket` module, allowing communication between a server and a client over a network. Here’s a line-by-line explanation, followed by the documentation.

### Code Explanation:

```python
import socket
```
- **Imports the `socket` module**: This module provides access to the Berkeley sockets API, allowing the creation of network connections.

```python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- **Creates a socket object**: 
  - `AF_INET` indicates the use of IPv4.
  - `SOCK_STREAM` sets the socket type to TCP, a reliable connection-oriented protocol.

```python
server.bind(('0.0.0.0', 9999))
```
- **Binds the server to an IP and port**:
  - `'0.0.0.0'` allows the server to accept connections from any available network interface.
  - `9999` is the port number the server listens on. It can be any unused port.

```python
server.listen()
```
- **Puts the server in listening mode**: It tells the operating system to queue incoming connection requests.

```python
print("Waiting for client connection...")
```
- **Prints a message**: Indicates that the server is now waiting for a client to connect.

```python
client, addr = server.accept()
```
- **Accepts an incoming connection**:
  - Blocks the execution until a client connects.
  - `client` is the new socket object for communication with the client.
  - `addr` contains the client’s address (IP and port).

```python
print(f"Client connected from {addr}")
```
- **Displays the address of the connected client**.

```python
while True:
```
- **Starts an infinite loop**: The loop is used to handle communication with the client until the connection is terminated.

```python
    msg = client.recv(1024).decode('utf-8')
```
- **Receives a message from the client**:
  - `recv(1024)` reads up to 1024 bytes of data from the client socket.
  - `decode('utf-8')` converts the received byte data into a string using UTF-8 encoding.

```python
    if msg.lower() == 'quit':
        print("Client has ended the connection.")
        break
```
- **Checks if the client wants to end the connection**:
  - If the received message is `'quit'` (case-insensitive), the server prints a message and exits the loop.

```python
    else:
        print("\nClient: ", msg)
```
- **Displays the received message from the client**.

```python
    server_msg = input("Enter Msg (type 'quit' to exit): ")
```
- **Takes input from the server operator**: Asks the server user to type a message to send to the client.

```python
    client.send(server_msg.encode('utf-8'))
```
- **Sends the message to the client**: The message is encoded as a UTF-8 byte stream before sending it over the socket.

```python
    if server_msg.lower() == 'quit':
        print("Ending the connection.")
        break
```
- **Checks if the server wants to end the connection**:
  - If the server types `'quit'`, the server prints a message and exits the loop.

```python
client.close()
```
- **Closes the client socket**: Terminates the connection to the client.

```python
server.close()
```
- **Closes the server socket**: Shuts down the server and releases any resources.

---

### Documentation:

#### Overview
This script creates a simple TCP server that waits for incoming client connections, receives and sends messages, and terminates the connection when either the server or the client sends a "quit" message.

#### Functionality
- **Socket Creation**: 
  - A TCP socket is created using `socket.AF_INET` (IPv4) and `socket.SOCK_STREAM` (TCP).
- **Binding**: 
  - The server binds to IP address `'0.0.0.0'` (all available interfaces) and port `9999`.
- **Listening**: 
  - The server listens for incoming connection requests.
- **Accepting Connections**: 
  - When a client connects, the server accepts the connection and prints the client’s address.
- **Communication Loop**:
  - The server enters a loop where it waits for messages from the client, displays them, and sends back responses.
  - If either the server or the client sends `'quit'`, the connection is terminated.
- **Cleanup**:
  - The client and server sockets are properly closed to release system resources.

#### Example Usage
1. Run the server script on a machine. The server will start listening for incoming client connections on port 9999.
2. When a client connects, the server will print the client’s address.
3. Both the client and server can exchange messages by typing into their respective consoles.
4. Either the client or the server can end the connection by sending the message `'quit'`.

#### Notes:
- This example only handles one client at a time.
- Make sure port `9999` is not blocked by a firewall.
- The server needs to be restarted to accept another client after the connection is closed.