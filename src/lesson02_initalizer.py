# SuperFastPython.com
# example of initializing worker processes in the multiprocessing pool
from time import sleep
from multiprocessing import Pool

# task executed in a worker process
def task():
    # report a message
    print('Worker executing task...', flush=True)
    # block for a moment
    sleep(1)

# initialize a worker in the multiprocessing pool
def initialize_worker():
    # report a message
    print('Initializing worker...', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create and configure the multiprocessing pool
    with Pool(2, initializer=initialize_worker) as pool:
        # issue tasks to the multiprocessing pool
        for _ in range(4):
            pool.apply_async(task)
        # close the multiprocessing pool
        pool.close()
        # wait for all tasks to complete
        pool.join()
