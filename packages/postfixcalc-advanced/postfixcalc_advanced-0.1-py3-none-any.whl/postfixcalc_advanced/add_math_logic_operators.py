import operator
import math

def int_from_float(a):
    if a is not None:
        return operator.floordiv(a, 1)
    else:
        return None

def qudric(a):
    if a is None:
        return None
    return operator.pow(a, 2)

def start_solving(something):
    print('= in expression')
    return None

def unary_minus(a):
    if a is None:
        return None
    return -a

def sin(a):
    if a is None:
        return None
    a = math.radians(a)
    return math.sin(a)

def cos(a):
    if a is None:
        return None
    a = math.radians(a)
    return math.cos(a)

def tan(a):
    if a is None:
        return None
    a = math.radians(a)
    return math.tan(a)

def atan(a):
    if a is None:
        return None
    a = math.atan(a)
    return math.degrees(a)

def arccos(a):
    if a is None:
        return None
    a = math.acos(a)
    return math.degrees(a)


def arcsin(a):
    if a is None:
        return None
    a = math.asin(a)
    return math.degrees(a)


def divide(a, b):
    if b != 0:# and a is not None and b is not None:
        return operator.truediv(a, b)
    else:
        print('None or infinity')
        return None

#def multy(a, b):
#    if a is None or b is None:
#        return None
#    return operator.mul

#def sum_(a, b):
#    if a is None or b is None:
#        return None
#    return operator.add

#def sub_(a, b):
#    if a is None or b is None:
#        return None
#    return operator.sub

def pow_(a, b):
    if a is None or b is None:
        return None
    return operator.pow(a, b)
