1class Solution:
2    def detectCapitalUse(self, word: str) -> bool:
3        """
4        Capital usage is correct ONLY IF one of these holds:
5        All letters are uppercase → "USA"
6        All letters are lowercase → "leetcode"
7        Only first letter is uppercase AND the rest are lowercase → "Google"
8        """
9        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
10