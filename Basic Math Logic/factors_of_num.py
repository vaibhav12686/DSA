from math import sqrt

def factors(num):

    result = []
    for i in range(1, int(sqrt(num) + 1)):
        if num % 10 == 0:
            result.append(i)
            if num // i != i:
                result.append(num // i)

    result.sort()
    return result

print(factors(20))