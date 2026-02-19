1from collections import deque
2class Solution:
3    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
4        """
5        time complexity : O(n^2)
6        memory: 19.41MB , Beats: 6.23%
7        for use sandwiches as it's 
8        but of make it as deque we will have optimal solution 
9        with 
10        time complexity: O(n)
11        """
12        queue = deque(students)
13        sandwiches = deque(sandwiches)
14        count = 0
15        while queue and sandwiches:
16            if queue[0]==sandwiches[0]:
17                queue.popleft()
18                sandwiches.popleft()
19                count = 0
20            else:
21                queue.append(queue.popleft())
22                count += 1
23                if count == len(queue):
24                    return len(queue)
25        return len(queue)