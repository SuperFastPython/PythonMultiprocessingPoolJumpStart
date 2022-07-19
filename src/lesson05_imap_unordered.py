# SuperFastPython.com
# example executing multiple task with imap_unordered()
from time import sleep
from random import random
from multiprocessing import Pool

# a task to execute in another process
def task(arg):
    # block for a random fraction of a second
    sleep(random())
    # report a message
    print(f'From another process {arg}', flush=True)
    # return a value
    return arg * 2

# entry point for the program
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool(4) as pool:
        # issue multiple tasks and process return values
        for rs in pool.imap_unordered(task, range(10)):
            print(rs)
