class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            l=[0]*26
            c=""
            for j in range(i,len(s)):
                c+=s[j]
                if s[j]>='a':
                    l[ord(s[j])-ord('a')]=l[ord(s[j])-ord('a')]|1
                else:
                    l[ord(s[j])-ord('A')]=l[ord(s[j])-ord('A')]|2
                f=0
                for k in l:
                    if k==1 or k==2:
                        f=1
                        break
                if f==0:
                    if len(c)>len(ans):
                        ans=c
        return ans