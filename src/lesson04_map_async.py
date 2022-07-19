# SuperFastPython.com
# example of executing multiple task with Pool.map_async()
from multiprocessing import Pool

# a task to execute in another process
def task(arg):
    # report a message
    print(f'This is another process with {arg}', flush=True)
    # return a value
    return arg * 2

# entry point for the program
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # issue multiple tasks to the pool
        async_result = pool.map_async(task, range(10))
        # process return values once all issued tasks have completed
        for result in async_result.get():
            print(result)
