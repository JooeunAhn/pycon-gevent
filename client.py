import socket
s = socket.socket()
s.connect(('localhost', 8000))
s.send(b'Hello socket')
s.send('안녕 세계!'.encode())