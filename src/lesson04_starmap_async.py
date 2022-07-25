# SuperFastPython.com
# example many tasks multiple arguments asynchronously
from multiprocessing import Pool

# custom function to be executed in a child process
def task(arg1, arg2, arg3):
    # report a message
    print(f'From another process {arg1}, {arg2}, {arg3}',
        flush=True)
    # return a value
    return arg1 + arg2 + arg3

# protect the entry point
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # prepare task arguments
        args = [(i, i*2, i*3) for i in range(10)]
        # issue multiple tasks to the pool
        async_result = pool.starmap_async(task, args)
        # process return values
        for result in async_result.get():
            print(result)
