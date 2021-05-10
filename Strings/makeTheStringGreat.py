class Solution:
    def makeGood(self, s: str) -> str:
        ans=''
        for i in s:
            if len(ans)==0:
                ans+=i
            else:
                if ans[-1].lower()==i.lower():
                    if ans[-1]==i:
                        ans+=i
                    else:
                        ans=ans[:-1]
                else:
                    ans+=i
        return ans