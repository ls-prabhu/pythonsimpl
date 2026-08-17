# using try catch finilly 

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("you can't devide by zero")
    else:
        print(result)
    finally:
        print("this statement will always execute!!!")

while True:
    x = int(input(" enter the first number :"))
    y = int(input("enter the second number :"))
    divide(x,y)