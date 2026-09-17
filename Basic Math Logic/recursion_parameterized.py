def func(Sum, i, N):
    if i > N:
        print(Sum)
        return

    func(Sum + i, i + 1, N)

func(0, 1, 10)    