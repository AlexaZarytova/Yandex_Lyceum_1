import socket

sock = socket.socket()
sock.connect(('84.201.141.205', 8088))
for i in range(10):
    sock.send("2 минуты до урока".encode("utf-8"))

data = sock.recv(1024)
print("[RECEIVED]:", str(data, 'utf-8'))
sock.close()