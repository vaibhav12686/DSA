# recursion using parameters

# Print x, N number of times

def func1(x, N):
    if N == 0:
        return

    print(x)
    func1(x, N - 1)

func1(15, 4)


# Print 1 to N using HEAD Recursion

# HEAD recursion
def func2(i, N):
    if i > N:
        return

    print(i)
    func2(i + 1, N)

func2(3, 8)    


# Print 1 to N using TAIL Recursion

def func5(i, N):
    if N < 1:
        return

    func5(i, N -1)
    print(N)

func5(1,5)    


# TAIL recursion / BACKTRACKING

# Print N to 1 

def func3(i, N):
    if i > N:
        return

    func3(i + 1, N)
    print(i)

func3(1, 4)


# N to 1 using HEAD  recursion

def func4(N):
    if N == 0:
        return

    print(N)
    func4(N-1)

func4(4)    