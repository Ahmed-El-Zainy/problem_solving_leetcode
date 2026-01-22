1class Solution:
2    def maskPII(self, s: str) -> str:
3        if "@" in s:
4            name, domain = s.lower().split("@")
5            return name[0] + "*****" + name[-1] + "@" + domain
6        else:
7            digits = [digit for digit in s if digit.isdigit()]
8            total_length = len(digits)
9            local = "".join(digits[-4:])
10            country_len = total_length - 10
11            if country_len==0:
12                return "***-***-" + local
13            else: 
14                return "+" + "*" * country_len + "-***-***-" + local
15