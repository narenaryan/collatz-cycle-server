#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print 'Connecting to Collatz cycle server'

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


number = raw_input("please give a no to calculate collatz conjecture max cycle: ")
print 'Sending request %s ' % number
#Send number to server
socket.send(number)
#Wait and print result
message = socket.recv()
print 'Collatz Conjecture max cycle of %s  is <[ %s ]>' % (number, message)