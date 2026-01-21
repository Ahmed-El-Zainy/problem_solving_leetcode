1class Solution:
2    def licenseKeyFormatting(self, s: str, k: int) -> str:
3        s= s.replace("-", "").upper()[::-1]
4        groups = [s[i:i+k] for i in range(0,len(s), k)]
5        return "-".join(groups)[::-1]