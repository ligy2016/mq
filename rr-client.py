import zmq
c = zmq.Context()
s = c.socket(zmq.REQ)
# s.bind('tcp://127.0.0.1:10002')
# s.bind('ipc://d:/tmp')
s.connect('tcp://localhost:5555')
# while True:
s.send_pyobj('hello')
msg = s.recv_pyobj()
print msg