1from sortedcontainers import SortedList
2
3class Solution:
4    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
5        n = len(nums)
6        
7        if k == 1:
8            return nums[0]
9        
10        small = SortedList()  # k-1 smallest elements
11        large = SortedList()  # remaining elements
12        small_sum = 0  # Sum of elements in small
13        
14        # Initialize first window [1, 1+dist]
15        window_end = min(n - 1, 1 + dist)
16        
17        # Add all elements in initial window to small
18        for i in range(1, window_end + 1):
19            small.add(nums[i])
20            small_sum += nums[i]
21        
22        # Keep only k-1 smallest in small, move rest to large
23        while len(small) > k - 1:
24            val = small.pop()
25            small_sum -= val
26            large.add(val)
27        
28        # Calculate initial cost
29        min_cost = nums[0] + small_sum
30        
31        # Slide the window
32        for left in range(2, n):
33            right = left + dist
34            if right >= n:
35                break
36            
37            # Remove element at index left-1
38            remove_val = nums[left - 1]
39            if remove_val in small:
40                small.remove(remove_val)
41                small_sum -= remove_val
42                # Refill from large
43                if large:
44                    val = large.pop(0)
45                    small.add(val)
46                    small_sum += val
47            else:
48                large.remove(remove_val)
49            
50            # Add element at index right
51            add_val = nums[right]
52            if len(small) < k - 1:
53                small.add(add_val)
54                small_sum += add_val
55            elif add_val <= small[-1]:
56                small.add(add_val)
57                small_sum += add_val
58                val = small.pop()
59                small_sum -= val
60                large.add(val)
61            else:
62                large.add(add_val)
63            
64            # Update minimum cost
65            if len(small) == k - 1:
66                min_cost = min(min_cost, nums[0] + small_sum)
67        
68        return min_cost