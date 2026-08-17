import math
import sys

def num_stat(x):
    if not isinstance(x,(int)):
        raise TypeError("works with only numbers")
    if x<=0:
        raise ValueError("should be positive number")
    print(f'{x} square is {x*x}')
    print(f'{x} square root is {math.sqrt(x)}')

def indexerr(lst):
    try:
        print(lst[0])
        print(lst[5])
    except IndexError as e:
        print(e)

def nameerror():
    try:
        name = "hello_world"
        # return hello_world
    except NameError as e:
        print(e)

def typeerror():
    iterator = [0,1,'2',3,4,5]
    fruits=["apple", "orange","banana","grapes","kiwi","lichi"]
    for i in range(len(iterator)):
        try:
            print(fruits[iterator[i]])
        except TypeError as e:
            print(e)

def zerodiverror(num1,num2):
    try:
        result = num1/num2
        print(result)
    except ZeroDivisionError as e:
        print(e)



if __name__ == "__main__":
    # num_stat("hello")
    num_stat(50)
    # indexerr([2,4,5,6,6])
    # nameerror()
    # typeerror()
    # zerodiverror(10,2)
    # zerodiverror(3,0)