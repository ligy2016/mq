import zmq
import random
import time

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5577")

# Socket with direct access to the sink: used to syncronize start of batch
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print "Press Enter when the workers are ready: "
_ = raw_input()
print "Sending tasks to workers..."
print "1"
# sender.send(b'0')
print "2"
random.seed()
total_msec = 0
for task_nbr in range(100):
    workload = random.randint(1, 100)
    total_msec += workload
    print "hhh"

    sender.send(str(workload))
    # sender.send_string(u'%i' % workload)

print "Total expected cost: %s msec" % total_msec
time.sleep(1)