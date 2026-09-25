# To find the second largest distinct element without sorting


# 2 passes 


from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    # -------- Pass 1 : absolute min & max --------
    for i in range(0, len(a)):
        small = min(small, a[i])
        large = max(large, a[i])

    # -------- Pass 2 : second min & second max --------
    for i in range(0, len(a)):
        if a[i] < second_small and a[i] != small:      # candidate > min
            second_small = a[i]
        if a[i] > second_large and a[i] != large:      # candidate < max
            second_large = a[i]

    return [second_large, second_small]

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    n = len(arr)

    result = getSecondOrderElements(n, arr)
    print("Input array:", arr)
    print("Output [second_largest, second_smallest]:", result)




# OPTIMAL: 1 pass
 

from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    # -------- Single pass updates everything --------
    for i in range(0, len(a)):
        # ----- smaller side -----
        if a[i] < small:                       # new absolute min
            second_small = small
            small = a[i]
        elif a[i] < second_small and a[i] != small:
            second_small = a[i]

        # ----- larger side -----
        if a[i] > large:                       # new absolute max
            second_large = large
            large = a[i]
        elif a[i] > second_large and a[i] != large:
            second_large = a[i]

    return [second_large, second_small]


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    n = len(arr)

    result = getSecondOrderElements(n, arr)
    print("Input:", arr)
    print("Output [second_largest, second_smallest]:", result)