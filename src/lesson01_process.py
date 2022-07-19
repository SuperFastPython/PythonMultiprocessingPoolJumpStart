# SuperFastPython.com
# example of running a function in a new process
from multiprocessing import Process

# a task to execute in another process
def task():
    print('This is another process', flush=True)

# entry point for the program
if __name__ == '__main__':
    # define a task to run in a new process
    process = Process(target=task)
    # start the task in a new process
    process.start()
    # wait for the task to complete
    process.join()
