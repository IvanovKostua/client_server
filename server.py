import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(10)
print('All is ready!')

try:

    while True:

        conn, addr = sock.accept()
        print(f'{time.time()} connected by {addr}')

        while True:

            data = conn.recv(1024)
            if not data:
                break
            data = data.upper()
            conn.sendall(data)

        conn.close()

except KeyboardInterrupt:

    conn.close()
    sock.close()