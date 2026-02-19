1class Solution:
2    def pivotInteger(self, n: int) -> int:
3        sum=(n*(n+1))//2
4        x=int(math.isqrt(sum))
5        return x if(x*x==sum) else -1