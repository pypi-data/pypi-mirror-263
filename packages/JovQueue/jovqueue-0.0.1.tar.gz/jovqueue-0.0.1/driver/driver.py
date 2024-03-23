# This is an example driver program which utilizes the JovQueue
import time
from JovQueue import JovQueue

# example function to turn into a queue-able function using JovQueue
def example_function(value):
    time.sleep(value)
# We should create a JovQueue of reasonable size
jovqueue = JovQueue(8, example_function)
# We should then run a bunch of things through the Queue 
for i in range(24):
    jovqueue.run(1) # this should make each of these sleep for one second
time.sleep(5) # we should delay mains closing until all our daemons are done with our loop of functions
