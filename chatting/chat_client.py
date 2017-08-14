import socket
from functools import reduce

def client():
    s = socket.socket()
    s.connect(('0.0.0.0', 8003))
    f = s.makefile('rw')

    while True:
        message = input("Type Message\n")
        print(message, file=f, flush=True)

if __name__ == "__main__":
    client()

# nc localhost 8003