class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        i=0
        j=1
        while j<len(s):
            if s[j]==s[i]:
                j+=1
            else:
                ans=max(ans,j-i)
                i=j
                j+=1 
        ans=max(ans,j-i)
        return ans