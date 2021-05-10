class Solution:
    def modifyString(self, s: str) -> str:
        ans=""
        n=len(s)
        for i in range(n):
            if s[i]!='?':
                ans+=s[i]
            else:
                l=[]
                if i>0:
                    l.append(ans[-1])
                if i+1<n:
                    l.append(s[i+1])
                if 'a' not in l:
                    ans+='a'
                elif 'b' not in l:
                    ans+='b'
                else:
                    ans+='c'
        return ans