class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans=""
        n=str(n)
        for i in range(len(n)):
            if i%3==0 and i!=0:
                ans+='.'
            ans+=n[len(n)-1-i]
        return ans[::-1]
                