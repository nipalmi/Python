import math
import os
import random
import re
import sys

print('prova 6')
class IncreasingList(list):

    def append(self, val):
        """
        first, it removes all elements from the list that have greater values than val, starting from the last one, and once there are no greater element in the list, it appends val to the end of the list
        """
        if self == []:
            self.extend([val])
        else:
            while self[-1] > val:
                self.pop()
            self.extend([val])

    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise, if the list is empty, it does nothing
        """
        if len(self) != 0:
            del self[-1]

    def __len__(self):
        """
        returns the number of elements in the list
        """
        count = 0
        for i in self:
            count = count + 1

        return count


lst1 = IncreasingList([5,8,12,28])

lst1.append(35)

print(lst1)

numbelem = lst1.__len__()

print(numbelem)


#
# strdir =  r"C:\Users\nicnic\Desktop\programmi python\esercizi python\provalista.txt"

#
# fptr = open(strdir, 'w')
lst = IncreasingList()
q = int(input())
print (q)

for _ in range(q):
    op = input().split()
    op_name = op[0]
    if op_name == "append":
        val = int(op[1])
        print(val)
        lst.append(val)
        print(lst)
    elif op_name == "pop":
        lst.pop()
    elif op_name == "size":
        numberlem = lst.__len__()
        print(numberlem)
#        fptr.write("%d\n" % len(lst))
    else:
        raise ValueError("invalid operation")
# fptr.close()

#
