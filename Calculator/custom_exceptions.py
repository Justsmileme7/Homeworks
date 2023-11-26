def excpectation_zerodivision(x,y):
    result = None
    try:
        result = x/y
    except ZeroDivisionError:
        print('Something wrong! You can not zero division')
    return result

def get_not_number(x,y):
    try:
        x = int(x)
        y = int(y)
        return x, y
    except ValueError:
        print('You need enter only numbers')
        quit()

def wrong_operation(z):
    try:
        z = int(z) and z <= 5
        return z
    except Exception:
        print('You need enter only one from five numbers')
        quit()