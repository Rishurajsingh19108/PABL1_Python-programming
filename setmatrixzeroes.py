class Solution:
    def setZeroes(self, matrix):
        r, c = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j] = 0
