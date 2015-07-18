import zmq
import gevent
from gevent import monkey

monkey.patch_all()

#Create context
context = zmq.Context()
#Set type of socket
socket = context.socket(zmq.REP)
#Bind socket to port 5555
socket.bind("tcp://*:5555")

#Algorithm for finding collatz conjecture
def do_collatz(n):
    def collatz(n,cycle=''):
        while True:
            if n == 1:
                cycle += str(n)
                break
            else:
                if n % 2 == 1:
                    n = ( 3 * n ) + 1
                    cycle += str(n)
                else:
                    n = n/2
                    cycle += str(n)
        return len(cycle)

    #This Gevent code is for speeding up the calculation of cycles
    jobs = [ gevent.spawn(collatz, x) for x in range(1,n) ]
    gevent.joinall(jobs)
    return max([g.value for g in jobs])

while True:
    #  Wait for next request from client
    number = int(socket.recv())
    print("Received request for finding max collatz cycle between 1..... %s" % number)
    #  Send reply back collatz conjecture to client
    num = str(do_collatz(number))
    socket.send(num)


