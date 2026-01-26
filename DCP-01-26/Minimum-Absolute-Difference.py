1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        arr.sort()
4        min_diff = float('inf')
5        for i in range(len(arr)-1):
6            current_diff = arr[i+1] - arr[i]
7            if current_diff < min_diff:
8                min_diff = current_diff
9
10        answer = []
11        
12        for i in range(len(arr)-1):
13            if (abs(arr[i] - arr[i+1])) <= min_diff:
14                answer.append([arr[i], arr[i+1]])
15        
16        return answer 
17