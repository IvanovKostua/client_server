import socket

data = b'Hello, world!'

sock = socket.socket()
sock.connect(('127.0.0.1', 8888))
sock.sendall(data)
data2 = sock.recv(1024)
sock.close()
print('Received', repr(data2))