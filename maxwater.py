class Solution:
    def maxWater(self, arr):
        n = len(arr)
        water = 0
        
        for i in range(n):
            left_max = max(arr[:i+1])     
            right_max = max(arr[i:])      
            
            water += min(left_max, right_max) - arr[i]
        
        return water
