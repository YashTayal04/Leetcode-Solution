class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d={}
        ans=-1
        for i in range(len(s)):
            if s[i] in d:
                ans=max(i-d[s[i]]-1,ans)
            else:
                d[s[i]]=i
        return ans