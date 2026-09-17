arr = [5,7,3,2,6,1,5,9]
left = 2
right = 5

def reverse(arr, left, right):
    if left >= right:
        return arr

    arr[left], arr[right] = arr[right], arr[left]

    return reverse(arr, left + 1, right - 1)

print(reverse(arr, left, right))