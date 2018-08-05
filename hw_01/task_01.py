#Function factorial with inner cache

def cache_decorator(func):
    cache = {}
    def wrapped(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapped

@cache_decorator
def my_factorial(x):
    assert x >= 0
    if x == 0:
        return 1
    return x * my_factorial(x - 1)


print(my_factorial(8))
