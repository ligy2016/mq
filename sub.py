import sys
import time
import zmq

def main():
    # if len(sys.argv )!= 2:
    #     print 'usage: subscriber <connect_to> [topic topic ...]'
    #     sys.exit(1)
    connect_to= 'tcp://127.0.0.1:10001'
    #topics =  ['sports.general','sports.football']
    topics = []
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)

    #managesubscriptions

    if not topics:
        print "Receiving messages on ALL topics..."
        s.setsockopt(zmq.SUBSCRIBE, '')
    else:
        print "Receiving messages on topics: %s ..." % topics
        for t in topics:
            s.setsockopt(zmq.SUBSCRIBE, t)
    #print
    try:
        while True:
            topic, msg = s.recv_pyobj()
            print '   Topic: %s, msg:%s' % (topic, msg)
    except KeyboardInterrupt:
        pass
    print "Done."
if __name__ == "__main__":
    main()

