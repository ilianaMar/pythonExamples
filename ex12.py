#map, filter, zip and reduce
from functools import reduce


my_list = [1,2,3]
your_list = (10,20,30)

def multiple_two(item):
    return item * 2

def find_odd(item):
    return item % 2 != 0

def accumolator(acc, item):
    print(acc, item)
    return acc + item
    


print(list(map(multiple_two, my_list)))
print(list(filter(find_odd, my_list)))
print(list(zip(your_list, my_list)))
print(reduce(accumolator, my_list, 10))