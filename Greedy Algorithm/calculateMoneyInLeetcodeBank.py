class Solution:
    def totalMoney(self, n: int) -> int:
        x=n//7
        ans=7*x*(x+7)//2
        r=n%7
        s=x+1
        for i in range(r):
            ans+=s
            s+=1
        return ans
            