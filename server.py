import socket
soc = socket.socket()
soc.bind(('157.51.197.46', 12345))
soc.listen()
conn, _ = soc.accept()
print(conn.recv(1024).decode())
