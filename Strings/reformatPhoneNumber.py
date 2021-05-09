class Solution:
    def reformatNumber(self, number: str) -> str:
        ans=''
        c=0
        for i in number:
            if i>='0' and i<='9':
                if c==3:
                    ans+='-'
                    c=0
                ans+=i
                c+=1 
        if c==1:
            return ans[:-3]+'-'+ans[-3]+ans[-1]
        else:
            return ans