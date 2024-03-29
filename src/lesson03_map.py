# SuperFastPython.com
# example of executing multiple tasks and waiting
from multiprocessing import Pool

# custom function to be executed in a child process
def task(arg):
    # report a message
    print(f'From another process {arg}', flush=True)
    # return a value
    return arg * 2

# protect the entry point
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # issue multiple tasks and process return values
        for result in pool.map(task, range(10)):
            print(result)
