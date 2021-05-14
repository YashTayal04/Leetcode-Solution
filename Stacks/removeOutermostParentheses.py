class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        c=0
        ans=""
        for i in S:
            if i=='(':
                if c>0:
                    ans+=i
                c+=1
            else:
                c-=1
                if c>0:
                    ans+=i
        return ans