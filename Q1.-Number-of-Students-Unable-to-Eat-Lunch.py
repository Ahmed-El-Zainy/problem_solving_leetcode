1from collections import deque
2class Solution:
3    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
4        """
5        time complexity : O(n^2)
6        memory: 19.41MB , Beats: 6.23%
7        """
8        queue = deque(students)
9        sandwiches = deque(sandwiches)
10        count = 0
11        while queue and sandwiches:
12            if queue[0]==sandwiches[0]:
13                queue.popleft()
14                sandwiches.popleft()
15                count = 0
16            else:
17                queue.append(queue.popleft())
18                count += 1
19                if count == len(queue):
20                    return len(queue)
21        return len(queue)