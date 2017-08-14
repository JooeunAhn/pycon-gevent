import socket
from functools import reduce

def client():
    s = socket.socket()
    s.connect(('0.0.0.0', 8001))
    f = s.makefile('rw')

    while True:
        r = f.readline()
        # answer = reduce(lambda x, y: int(x)+int(y), r.split(','))
        answer = int(input("Type sum value : {}".format(r)))
        answer = str(answer)
        print(answer, file=f, flush=True)

if __name__ == "__main__":
    client()