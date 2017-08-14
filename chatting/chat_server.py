from gevent.server import StreamServer

connected_socket = []

def special(msg):
    ml = msg.split(' ')

    keyword = ml[0]

    if keyword == "/dice":
        try:
            import random
            num = int(ml[1].replace("\n", ""))
            num = random.randrange(num)
            return num
        except:
            return "nonumber"

def handler(cs, ca):
    import random
    f = cs.makefile('rw')
    connected_socket.append(f)
    try:
        while True:
            message = f.readline()
            print("got message:", message)

            if message[0] == "/":
                message = special(message)
                print(message)

            for fs in connected_socket:
                if f != fs:
                    print(message, file=fs, flush=True)
    except:
        connected_socket.remove(f)

server = StreamServer(('0.0.0.0', 8003), handler)
server.serve_forever()