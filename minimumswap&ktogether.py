class Solution:
    def minSwap(self, arr, k):
        c = 0
        for x in arr:
            if x <= k:
                c += 1
        
        b = 0
        for i in range(c):
            if arr[i] > k:
                b += 1
        
        ans = b
        
        for i in range(c, len(arr)):
            if arr[i] > k:
                b += 1
            if arr[i - c] > k:
                b -= 1
            ans = min(ans, b)
        
        return ans
