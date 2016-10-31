import zmq
c = zmq.Context()
s = c.socket(zmq.REP)
# s.bind('tcp://127.0.0.1:10002')
# s.bind('ipc://d:/tmp')
s.bind('tcp://*:5555')
while True:
    msg = s.recv_pyobj()
    print msg
    s.send_pyobj(msg+' i am server')

s.close()