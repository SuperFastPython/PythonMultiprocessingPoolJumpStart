# SuperFastPython.com
# example of running a function in a new process
from multiprocessing import Process

# custom function to be executed in a child process
def task():
    # report a message
    print('This is another process', flush=True)

# protect the entry point
if __name__ == '__main__':
    # define a task to run in a new process
    process = Process(target=task)
    # start the task in a new process
    process.start()
    # wait for the child process to terminate
    process.join()
