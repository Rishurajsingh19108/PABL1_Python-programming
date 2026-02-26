class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        ans = 0
        
        for i in range(n):
            j = i
            while j < n and arr[j] >= arr[i]:
                ans += 1
                j += 1
                
        return ans
        
