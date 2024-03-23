from queue import Queue
from threading import Thread
import logging # for debug if needed

# Queue implementation (named it JovQueue for fun!)
class JovQueue:
    def __init__(self, thread_count, target_func):
        if thread_count < 1:
            raise ValueError("thread_count must be greater than 0")
        if thread_count > 99:
            raise ValueError("thread_count must be lower than 100")
        # create the Queue itself
        self.queue = Queue()
        # define a new function from target_func to interface with queue
        def mod_func(thread_no, queue):
            while True:
                logging.debug('Thread %d/%d waiting for next request', thread_no + 1, thread_count)
                request = queue.get() # get next available request
                logging.debug('Thread %d/%d performing the request', thread_no + 1, thread_count)
                target_func(request) # perform desired (inputted) business logic
                queue.task_done() # exclaim task completion
        # Set up the threads
        for iter in range(thread_count):
            worker = Thread(target=mod_func, args=(iter, self.queue,))
            worker.daemon = True
            worker.start()
    def run(self, args):
        self.queue.put(args, block=False)