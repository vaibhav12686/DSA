# divide the array

class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_arr = arr[ : mid]
        right_arr = arr[mid : ]

        left = self.merge_sort(left_arr)
        right = self.merge_sort(right_arr)

        return self.merge_arr(left, right)

# merge 2 sorted arrays

    def merge_arr(self, left, right):
        result = []
        i, j = 0, 0
        n, m = len(left), len(right)

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j]) 
                j += 1

        if i < n:
            while i < n:
                result.append(left[i])
                i += 1
                        
        if j < m:
            while j < m:
                result.append(right[j])
                j += 1

        return result

arr = [9,4,2,6,8,4,1,6,9,4,2,6,8]

solution = Solution()
print(solution.merge_sort(arr))