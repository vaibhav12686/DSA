from math import sqrt

def factors(num):

    result = []
    for i in range(1, int(sqrt(num) + 1)):
        if num % 10 == 0:
            result.append(i)
            if num // i != i:
                result.append(num // i)

# but the result after append will not be sorted
# so, to sort the list

    result.sort()
    return result

print(factors(20))