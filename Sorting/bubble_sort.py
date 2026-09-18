class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n - 2, -1, -1):
            swapped = False

            for j in range(0, i + 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr


arr = [64, 25, 12, 22, 11]

solution = Solution()
print(solution.bubbleSort(arr))