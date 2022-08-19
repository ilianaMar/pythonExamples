# lambda expressions
from functools import reduce
from itertools import count


my_list = [1, 2, 3]
new_list = [5, 4, 3]
a =  b = [(0,2), (4,3), (9,9), (10, -1)]
another_list = [char for char in 'hellloo']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100)]
my_list4 = [num for num in range(0, 100) if num % 2 == 0 ]
my_list5 = {char for char in 'hellloo'}
simple_dict = {
    'a' :1, 
    'b' : 2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2 == 0}
my_dict2 = {num:num*2 for num in [1,2,3]}
some_list = ['a', 'b', 'c', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])

print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list, 10))
print(list(map(lambda item: item ** 2, new_list)))
print(list(sorted(a, key=lambda tup: (tup[1],tup[0]))))
b.sort(key=lambda x: x[1])
print(b)
print(another_list)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)
print(my_dict)
print(my_dict2)
print(duplicates)
