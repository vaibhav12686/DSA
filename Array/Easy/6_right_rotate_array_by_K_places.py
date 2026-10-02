# brute force

# pop and insert

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Reduce unnecessary rotations
        rotations = k % len(nums)

        # Rotate one position at a time
        for i in range(rotations):
            last = nums.pop()
            nums.insert(0, last)

nums = [10, 20, 30, 40, 50, 60]
k = 8

Solution().rotate(nums, k)

print(nums)            