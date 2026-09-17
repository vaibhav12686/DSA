# sum of numbers from 1 to n

def func(N):
    if N == 1:
        return 1

    return N + func(N - 1)

print(func(5))