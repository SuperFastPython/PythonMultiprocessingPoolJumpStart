# SuperFastPython.com
# example of executing multiple task with Pool.map()
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
        # issue multiple tasks to the pool and process return values
        for result in pool.map(task, range(10)):
            print(result)
