# SuperFastPython.com
# example of executing multiple tasks one-by-one
from time import sleep
from random import random
from multiprocessing import Pool

# custom function to be executed in a child process
def task(arg):
    # block for a random fraction of a second
    sleep(random())
    # report a message
    print(f'From another process {arg}', flush=True)
    # return a value
    return arg * 2

# protect the entry point
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool(4) as pool:
        # issue multiple tasks and process return values
        for result in pool.imap(task, range(10)):
            print(result)
