class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        n = len(arr)
        
        x = arr[-1] - arr[0]
        
        for i in range(1, n):
            mn = min(arr[0] + k, arr[i] - k)
            mx = max(arr[-1] - k, arr[i-1] + k)
            
            if mn >= 0:
                x = min(x, mx - mn)
        return x
