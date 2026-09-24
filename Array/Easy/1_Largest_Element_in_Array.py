def largestElement(arr: list[int], n: int) -> int:
    max_num = arr[0]
    
    for num in arr:
        if num > max_num:
            max_num = num
    
    return max_num


arr = [10, 20, 4, 45, 99, 3]
n = len(arr)
print(largestElement(arr, n)) 