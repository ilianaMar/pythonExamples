from typing import List


class SuperList(list):
    def __len__(self):
        return 1000
        

super_list = SuperList()
super_list.append(5)
print(len(super_list))
print(super_list[0])
print(issubclass(SuperList, List))