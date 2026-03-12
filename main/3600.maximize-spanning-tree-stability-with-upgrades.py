#
# @lc app=leetcode id=3600 lang=python3
#
# [3600] Maximize Spanning Tree Stability with Upgrades
#
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/description/
#
# algorithms
# Hard (39.58%)
# Likes:    72
# Dislikes: 3
# Total Accepted:    7.6K
# Total Submissions: 18.7K
# Testcase Example:  '3\n[[0,1,2,1],[1,2,3,0]]\n1'
#
# You are given an integer n, representing n nodes numbered from 0 to n - 1 and
# a list of edges, where edges[i] = [ui, vi, si, musti]:
# 
# 
# ui and vi indicates an undirected edge between nodes ui and vi.
# si is the strength of the edge.
# musti is an integer (0 or 1). If musti == 1, the edge must be included in the
# spanning tree. These edges cannot be upgraded.
# 
# 
# You are also given an integer k, the maximum number of upgrades you can
# perform. Each upgrade doubles the strength of an edge, and each eligible edge
# (with musti == 0) can be upgraded at most once.
# 
# The stability of a spanning tree is defined as the minimum strength score
# among all edges included in it.
# 
# Return the maximum possible stability of any valid spanning tree. If it is
# impossible to connect all nodes, return -1.
# 
# Note: A spanning tree of a graph with n nodes is a subset of the edges that
# connects all nodes together (i.e. the graph is connected) without forming any
# cycles, and uses exactly n - 1 edges.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1
# 
# Output: 2
# 
# Explanation:
# 
# 
# Edge [0,1] with strength = 2 must be included in the spanning tree.
# Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
# The resulting spanning tree includes these two edges with strengths 2 and
# 6.
# The minimum strength in the spanning tree is 2, which is the maximum possible
# stability.
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2
# 
# Output: 6
# 
# Explanation:
# 
# 
# Since all edges are optional and up to k = 2 upgrades are allowed.
# Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
# The resulting spanning tree includes these two edges with strengths 8 and
# 6.
# The minimum strength in the tree is 6, which is the maximum possible
# stability.
# 
# 
# 
# Example 3:
# 
# 
# Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0
# 
# Output: -1
# 
# Explanation:
# 
# 
# All edges are mandatory and form a cycle, which violates the spanning tree
# property of acyclicity. Thus, the answer is -1.
# 
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^5
# 1 <= edges.length <= 10^5
# edges[i] = [ui, vi, si, musti]
# 0 <= ui, vi < n
# ui != vi
# 1 <= si <= 10^5
# musti is either 0 or 1.
# 0 <= k <= n
# There are no duplicate edges.
# 
# 
#

# @lc code=start
# @lc app=leetcode id=3600 lang=python3
#
# [3600] Maximize Spanning Tree Stability with Upgrades
#
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/description/  
#

from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        mandatory_edges = []
        optional_edges = []
        
        for ui, vi, si, musti in edges:
            if musti == 1:
                mandatory_edges.append((ui, vi, si))
            else:
                optional_edges.append((ui, vi, si))
        
        # Union-Find helpers
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, x, y):
            px, py = find(parent, x), find(parent, y)
            if px != py:
                parent[px] = py
                return True
            return False
        
        def can_form_base_spanning_tree():
            """Check if mandatory edges form a valid forest (no cycles)"""
            if len(mandatory_edges) > n - 1:
                return False
            parent = list(range(n))
            for ui, vi, si in mandatory_edges:
                if not union(parent, ui, vi):
                    return False
            return True
        
        def can_achieve(stability_target):
            """Check if stability >= stability_target is achievable with at most k upgrades"""
            if not can_form_base_spanning_tree():
                return False
            
            parent = list(range(n))
            edges_count = 0
            upgrades_used = 0
            
            # Add mandatory edges (cannot be upgraded)
            for ui, vi, si in mandatory_edges:
                if si < stability_target:
                    return False
                if union(parent, ui, vi):
                    edges_count += 1
            
            # Separate optional edges
            free_edges = []      # Already meet target, no upgrade needed
            need_upgrade = []     # Need upgrade but reachable with upgrade
            
            for ui, vi, si in optional_edges:
                if si >= stability_target:
                    free_edges.append((ui, vi))
                elif 2 * si >= stability_target:
                    need_upgrade.append((ui, vi, si))
            
            # Priority: use free edges first, then upgradable edges (prefer stronger originals)
            need_upgrade.sort(key=lambda x: x[2], reverse=True)
            
            # Use free edges
            for ui, vi in free_edges:
                if union(parent, ui, vi):
                    edges_count += 1
                    if edges_count == n - 1:
                        return upgrades_used <= k
            
            # Use upgradable edges
            for ui, vi, si in need_upgrade:
                if union(parent, ui, vi):
                    edges_count += 1
                    upgrades_used += 1
                    if edges_count == n - 1:
                        return upgrades_used <= k
            
            # Final check: did we connect all nodes?
            return edges_count == n - 1 and upgrades_used <= k
        
        # Quick sanity check
        if not can_form_base_spanning_tree():
            return -1
        
        # Binary search on possible stability values
        min_strength = min(si for _, _, si, _ in edges)
        max_strength = max(2 * si for _, _, si, _ in edges)
        
        left, right = min_strength, max_strength
        best = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_achieve(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best

# @lc code=end

