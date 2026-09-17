# check palindrome - ITERATIVE APPROACH

def is_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False

        left += 1
        right -= 1

    return True


arr = "nitin"
print(is_palindrome(arr)) 




# RECURSIVE APPROACH

arr = "nitin"
left = 0
right = len(arr) - 1

def palindrome(arr, left, right):
    if left >= right:
        return True

    if arr[left] != arr[right]:
        return False

    return palindrome(arr, left + 1, right -1)


print(palindrome(arr, left, right))