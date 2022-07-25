# SuperFastPython.com
# example executing multiple tasks asynchronously
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
        # issue multiple tasks to the pool
        async_result = pool.map_async(task, range(10))
        # process return values once all tasks completed
        for result in async_result.get():
            print(result)
