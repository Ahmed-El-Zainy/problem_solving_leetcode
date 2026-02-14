1class Solution:
2    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
3        tower = [[0] * (i + 1) for i in range(100)]
4        tower[0][0] = poured
5        
6        for i in range(99):
7            for j in range(i + 1):
8                excess = max(0, tower[i][j] - 1)
9                tower[i][j] = min(1, tower[i][j])
10                tower[i + 1][j] += excess / 2
11                tower[i + 1][j + 1] += excess / 2
12        
13        return min(1, tower[query_row][query_glass])
14    