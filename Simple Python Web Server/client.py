import sys
from socket import *

# Get the server host, port, and filename from command line arguments
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP socket and connect to the server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Construct the HTTP request message and send it to the server
request_message = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
client_socket.send(request_message.encode())

# Receive the server's response and display it as an output
response_message = client_socket.recv(4096).decode()
print(response_message)

# Close the client socket
client_socket.close()
