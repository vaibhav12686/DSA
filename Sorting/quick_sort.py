# lowest element as pivot

def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1

        while j >= low + 1 and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j




def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


arr = [9, 4, 2, 6, 8, 4, 1, 6, 9, 4, 2, 6, 8]
quick_sort(arr, 0, len(arr) - 1)

print(arr)



# when highest element as pivot


# def partition(arr, low, high):
#     pivot = arr[high] 
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# arr = [9, 4, 2, 6, 8, 4, 1, 6, 9, 4, 2, 6, 8]
# quick_sort(arr, 0, len(arr) - 1)

# print(arr)