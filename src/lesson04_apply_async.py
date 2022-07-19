# SuperFastPython.com
# example of executing a task with Pool.apply_async()
from multiprocessing import Pool

# a task to execute in another process
def task():
    print('This is another process', flush=True)

# entry point for the program
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # issue a task asynchronously
        async_result = pool.apply_async(task)
        # wait for the task to complete
        async_result.wait()
