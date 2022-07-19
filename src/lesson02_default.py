# SuperFastPython.com
# example of reporting the details of a default multiprocessing pool
from multiprocessing import Pool

# protect the entry point
if __name__ == '__main__':
    # create a multiprocessing pool with the default number of workers
    pool = Pool()
    # report the status of the multiprocessing pool
    print(pool)
    # close the multiprocessing pool
    pool.close()
