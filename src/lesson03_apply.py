# SuperFastPython.com
# example of executing a task with Pool.apply()
from multiprocessing import Pool

# a task to execute in another process
def task():
    print('This is another process', flush=True)

# entry point for the program
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # issue a task and wait for it to complete
        pool.apply(task)
