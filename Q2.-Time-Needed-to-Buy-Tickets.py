1class Solution:
2    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
3        time_step = 0
4        for i in range(len(tickets)):
5            if i <= k:
6                time_step += min(tickets[i], tickets[k])
7            else:
8                time_step += min(tickets[i], tickets[k] - 1)
9        return time_step