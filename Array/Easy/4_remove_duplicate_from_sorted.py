# brute force

# using Dictionary

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in nums:
            my_dict[i] = 0

        j = 0
        for n in my_dict:
            nums[j] = n
            j += 1
        return j

sol = Solution()

nums = [1, 1, 2, 2, 3]
k = sol.removeDuplicates(nums)
print(k)  
print(nums[:k])  # [1, 2, 3]  (first 3 elements are the unique sorted array)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = sol.removeDuplicates(nums)
print(k)
print(nums[:k])  # [0, 1, 2, 3, 4]    



# OPTIMAL SOLUTION

# using two pointers

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return i + 1

sol = Solution()

nums = [1, 1, 2, 2, 3]
k = sol.removeDuplicates(nums)
print(k)       # 3
print(nums[:k])  # [1, 2, 3]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = sol.removeDuplicates(nums)
print(k)       # 5
print(nums[:k])  # [0, 1, 2, 3, 4]

nums = [1]
k = sol.removeDuplicates(nums)
print(k)       # 1
print(nums[:k])  # [1]