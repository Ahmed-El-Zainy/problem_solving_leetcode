1class Solution:
2    def minCostToMoveChips(self, position: List[int]) -> int:
3        even, odd = 0, 0
4        for num in position:
5            if num%2 ==0:
6                even +=1
7            else: 
8                odd += 1
9        return min(even, odd)