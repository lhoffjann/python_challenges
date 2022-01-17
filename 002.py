


def fact(x):
    if x >= 1:
        return x * fact(x-1)
    elif x ==0:
        return 1

x =int(input("What Number? "))
print(fact(x))
