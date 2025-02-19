from math import factorial


def fact(s):
    if s == 0:
        return 1
    else :
        return s * fact(s-1)

print(fact(4))



#------------------------------------------


def facto(n):
    return factorial(n)

print(facto(4))