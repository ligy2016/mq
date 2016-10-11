import itertools
import sys
import time
import zmq

def main():
    if len(sys.args )!= 2:
        print 'usage: publisher <bind-to>'
    sys.exit()
    bind_to = sys.argv[1]
    all_topics = ['sports.general','sports.football','sports.basketball','stocks.general','stocks.GOOG','stocks.AAPL','weather']

    ctx = zmq.Context()

