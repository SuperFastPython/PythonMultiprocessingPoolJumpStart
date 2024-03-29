# SuperFastPython.com
# example of callback function for a one-off async task
from random import random
from time import sleep
from multiprocessing.pool import Pool

# custom function to be executed in a child process
def result_callback(return_value):
    # report a message
    print(f'Callback got: {return_value}', flush=True)

# task executed in a worker process
def task(identifier):
    # generate a value
    value = random()
    # report a message
    print(f'Task {identifier} executing with {value}',
        flush=True)
    # block for a moment
    sleep(value)
    # return the generated value
    return value

# protect the entry point
if __name__ == '__main__':
    # create and configure the multiprocessing pool
    with Pool() as pool:
        # issue tasks to the multiprocessing pool
        result = pool.apply_async(task, args=(0,),
            callback=result_callback)
        # close the multiprocessing pool
        pool.close()
        # wait for all tasks to complete
        pool.join()
