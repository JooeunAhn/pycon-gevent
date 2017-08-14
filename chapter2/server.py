from gevent.server import StreamServer


def make_q():
    import random
    x = random.randrange(100)
    y = random.randrange(100)
    return (x, y)

def handler(cs, ca):

    f = cs.makefile('rw')

    while True:
        x, y = make_q()
        answer = x + y
        q = "{},{}".format(x, y)
        print("question: {}".format(q))

        print(q, file=f, flush=True)

        string = f.readline()

        if answer == int(string):
            flag = True
        else:
            flag = False

        print("answer {}".format(answer))
        print("answer from client: ", flag)
        print("==========================")

server = StreamServer(('0.0.0.0', 8001), handler)
server.serve_forever()