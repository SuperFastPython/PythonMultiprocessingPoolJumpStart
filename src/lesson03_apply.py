# SuperFastPython.com
# example of executing a one-off task and waiting
from multiprocessing import Pool

# custom function to be executed in a child process
def task():
    # report a message
    print('This is another process', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # issue a task and wait for it to complete
        pool.apply(task)
