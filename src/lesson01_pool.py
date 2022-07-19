# SuperFastPython.com
# example of running a function in the multiprocessing pool
from multiprocessing import Pool

# a task to execute in another process
def task():
    print('This is another process', flush=True)

# entry point for the program
if __name__ == '__main__':
    # create the multiprocessing pool
    pool = Pool()
    # issue the task
    async_result = pool.apply_async(task)
    # wait for the task to finish
    async_result.wait()
    # close the multiprocessing pool
    pool.close()
