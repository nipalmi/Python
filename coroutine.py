import math
import os
import random
import re
import sys

res = math.floor(math.sqrt(28))
print(res)
res1 = math.sqrt(28)
print(res1)

def printer():
    while True:
        x = yield
        print(x)

def co_generator(n):
    for _ in range(n):
        x = int(input())
        yield x

def get_root():
    number = 0
    while True:
#        number = (yield)
#        number = yield math.floor(math.sqrt(number))
         number = yield math.sqrt(number)

def get_square():
    number = 0
    while True:
#        number = (yield)
        number = yield number**2

def accumulator():
    acum = 0
    while True:
#        acum += (yield)
        acum += yield acum

def operations_pipeline(numbers, operations, print_acum):
    for num in numbers:
        for i, w in enumerate(operations):
            num = w.send(num)
        print_acum.send(num)
    for operation in operations:
        operation.close()
    print_acum.close()

if __name__ == '__main__':
    order = input().strip()
    n = int(input())

    numbers = co_generator(n)

    print_acum = printer()
    next(print_acum)

    rooter = get_root()
    next(rooter)

    accumulate = accumulator()
    next(accumulate)

    square = get_square()
    next(square)

    operations_pipeline(numbers, eval(order), print_acum)
