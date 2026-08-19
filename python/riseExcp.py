# rise custom exception

class Error(Exception):
    """
    base class for all exception
    """
    pass

class PasswordTooShort(Error):
    """
    the password is too small,retry.
    """
    pass

class PasswordTooLong(Error):
    """
    The password is too long, retry.
    """
    pass

class PasswordNotHasDigit(Error):
    """
    the password should have atleast one digit.
    """
    pass


try:
    password = input("enter the password :")
    if(len(password)>16):
        raise PasswordTooLong("The password is too long, retry.")
        
    elif(len(password)<8):
        raise PasswordTooShort("the password is too small,retry.")
    elif(not(any(i.isdigit() for i in password))):
        raise PasswordNotHasDigit("the password should have atleast one digit.")
except Exception as e:
    print(e)