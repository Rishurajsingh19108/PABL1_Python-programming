class Solution:
    def prevSmaller(self, arr):
        stack = []
        ans = []
        
        for x in arr:
            while stack and stack[-1] >= x:
                stack.pop()
            
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
            
            stack.append(x)
        
        return ans
