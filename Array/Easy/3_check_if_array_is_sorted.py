# Given an integer array arr, decide if it is sorted in non-decreasing order (each element is no larger than the next).

# Return True if the whole array obeys this rule
# otherwise return False.

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        n = len(arr)
        # Scan pairs (i, i+1)
        for i in range(n - 1):           # last index is n-2
            if arr[i] > arr[i + 1]:      # found a drop
                return False
        return True                      # never dropped → sorted


s = Solution()

print(s.arraySortedOrNot([1, 2, 3, 4]))      # True  (sorted)
print(s.arraySortedOrNot([1, 3, 2, 4]))      # False (3 > 2)
print(s.arraySortedOrNot([5]))              # True  (single element)
print(s.arraySortedOrNot([]))               # True  (empty array)
print(s.arraySortedOrNot([2, 2, 3, 3]))      # True  (non-decreasing, equal allowed)