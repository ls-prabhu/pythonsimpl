import random

class Error(Exception):
    """Base class for other exception"""
    pass

class ValueTooSmall(Error):
    """The value is too small"""
    pass

class ValueTooLarge(Error):
    """The value is too large"""

number = random.randint(0,5)

while True:
    guess = int(input("enter a guess"))
    try:
        if(guess>number):
            raise ValueTooLarge
        elif(guess<number):
            raise ValueTooSmall
        else:
            print("you guessed right!")
            break;
    except ValueTooSmall as e:
        print("value too small")
    except ValueTooLarge as e:
        print("print value too large")