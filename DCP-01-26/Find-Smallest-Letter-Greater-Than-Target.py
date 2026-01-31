1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        left, right = 0, len(letters) - 1
4        while left <= right:
5            mid = (left + right) // 2
6            if letters[mid] <= target:
7                left = mid + 1
8            else:
9                right = mid - 1
10        return letters[left] if left < len(letters) else letters[0]