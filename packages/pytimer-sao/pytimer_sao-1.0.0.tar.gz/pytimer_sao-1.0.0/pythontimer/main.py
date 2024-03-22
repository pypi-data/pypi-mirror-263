import timeit
import time
import functools


def start_end(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        result = end - start
        result = "{:.8f}".format(result)
        print(f"{func.__name__} : {result} seconds")
        return result
    return wrapper


@start_end
def times2(x):
    print(x*2)


times2(5)
# f_result = times2(2)
# print(f_result)
