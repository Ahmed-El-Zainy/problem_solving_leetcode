1class Solution:
2    def detectCapitalUse(self, word: str) -> bool:
3        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())