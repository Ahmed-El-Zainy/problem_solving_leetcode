1from collections import deque
2class Solution:
3    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
4        queue = deque(students)
5        count = 0
6        while queue and sandwiches:
7            if queue[0]==sandwiches[0]:
8                queue.popleft()
9                sandwiches.pop(0)
10                count = 0
11            else:
12                queue.append(queue.popleft())
13                count += 1
14                if count == len(queue):
15                    return len(queue)
16        return len(queue)