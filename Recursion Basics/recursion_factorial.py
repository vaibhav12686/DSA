# find the factorial of a number

def factorial(Num):
    if Num == 1:
        return 1

    return Num * factorial(Num - 1)

print(factorial(5))