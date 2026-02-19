# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#
#         # if the target in the list return it index
#         # else return -1 as default for the index of it is input target
#         # all values in index are unique
#         # with using binary search tree
#         l, r = 0, (len(nums) - 1)
#
#         while nums[l] <= nums[r]:
#             m = (r+l) //2
#             if target == nums[m]:
#                 return m
#             # left is sorted
#             if nums[l] <= nums[m]:
#                 if nums[l] <= target < nums[m]:
#                     r = m - 1
#                 else:
#                     l = m + 1
#
#             # right is sorted
#             if nums[m] <= nums[r]:
#                 if nums[m] < taget <= nums[r]:
#                     l = m + 1
#                 else:
#                     r = m - 1
#
#         return

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        result = ""
        while node:
            result += str(node.val) + " -> "
            node = node.next
        return result + "None"

import heapq
class Solution:
    def removeNodes(self, head:Optional[ListNode])->Optional[ListNode]:
        # You are given the head of a linked list.
        # Remove every node which has a node with a greater value anywhere to the right side of it.
        # Return the head of the modified linked list.
        # if head is None:
        #     return
        stack = []
        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        nex = None
        while stack:
            cur = stack.pop()
            cur.next = nex
            nex = cur
        return cur

    def findRelativeRanks(self, score: list[int]) -> list[str]:
        result = []
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        for rank, (s, i) in enumerate(sorted_scores):
            if rank == 0:
                result.append((i, "Gold Medal"))
            elif rank == 1:
                result.append((i, "Silver Medal"))
            elif rank == 2:
                result.append((i, "Bronze Medal"))
            else:
                result.append((i, str(rank + 1)))
        result.sort()
        return [r for i, r in result]

    import heapq
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        if k > len(happiness):
            return "Error: k cannot be greater than the length of the happiness list"

        # Invert the values in the happiness list to simulate a max heap
        heap = [-num for num in happiness]

        # Transform list x into a heap
        heapq.heapify(heap)

        max_values = 0
        turn = 0
        for _ in range(k):
            # Pop and return the smallest item from the heap, and also push the new item.
            # The heap size doesn’t change. So it can be more efficient than heappop() followed by heappush().
            max_values += max(-heapq.heappop(heap) - turn, 0)
            turn += 1

        return max_values
def convert_to_linked_list(nums):
    dummy = ListNode(0)
    ptr = dummy
    for num in nums:
        ptr.next = ListNode(num)
        ptr = ptr.next
    return dummy.next

if __name__ == "__main__":
    happiness = [7, 50, 3]
    # scores = set(scores)
    # print(scores)
    # linked_list = convert_to_linked_list(nums)
    res = Solution().maximumHappinessSum(happiness, k=3)
    # output --> 57
    print(res)

