#Decorator
from time import time
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***********')
        func(*args, **kwargs)
        print('***********')
    return wrap_func

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}')
        return result
    return wrapper

@my_decorator
def hello(greeting, emoji = ':)'):
    print(greeting, emoji)
    

@performance
def long_time():
    for i in range(10000):
        i*5

hello('hhiiii')
long_time()
# my_decorator(hello)()


