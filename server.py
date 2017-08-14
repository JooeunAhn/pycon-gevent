import socket
s = socket.socket()
s.bind(('0.0.0.0', 8000))
s.listen(5)
cs, ca = s.accept()
print(ca)
print(cs)
