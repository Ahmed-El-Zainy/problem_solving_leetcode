1class Solution:
2    def licenseKeyFormatting(self, s: str, k: int) -> str:
3        s = s.replace("-", "").upper()[::-1]
4        result = []
5        for i in range(0, len(s), k):
6            result.append(s[i:i+k])            
7        return "-".join(result)[::-1]