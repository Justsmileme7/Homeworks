from custom_exceptions import excpectation_zerodivision
def addition(x, y):
    result = x+y
    print(result)
    return result
def subtraction(x,y):
    result = x-y
    print(result)
    return result
def multiplication(x,y):
    result = x*y
    print(result)
    return result

def division(x,y):
    result = excpectation_zerodivision(x,y)
    print(result)
    return result
def exponentiation(x,y):
    result = pow(x,y)
    print(result)
    return result
