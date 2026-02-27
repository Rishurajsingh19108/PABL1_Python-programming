class Solution:
    def has132Pattern(self, arr):
        n = len(arr)
        stack = []
        third = float('-inf')

        for i in range(n - 1, -1, -1):
            if arr[i] < third:
                return True

            while stack and arr[i] > stack[-1]:
                third = stack.pop()

            stack.append(arr[i])

        return False
