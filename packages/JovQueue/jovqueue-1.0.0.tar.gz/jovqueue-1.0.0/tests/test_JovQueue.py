from src.JovQueue import JovQueue
import pytest
import time
import threading

def example_test(value):
    time.sleep(value)

# We should throw an exception if someone attempts to create a 0 thread JovQueue
def test_no_threads():
    with pytest.raises(Exception):
        JovQueue(0, example_test)

# We should also throw an exception if someone attempts to create more than 99 threads
def test_100_threads():
    with pytest.raises(Exception):
        JovQueue(100, example_test)

# We want to make sure the correct number of threads is created when we run an example_test
def test_correct_thread_counts():
    jovqueue = JovQueue(8, example_test)
    # We should then run a bunch of things through the Queue 
    assert threading.active_count() == 9