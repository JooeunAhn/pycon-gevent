import socket
s = socket.socket()
s.connect(('ipkn.me', 10000))
s.send(b'Hello socket')
s.send('MMT MMT'.encode())
