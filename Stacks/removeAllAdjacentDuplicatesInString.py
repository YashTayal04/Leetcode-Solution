class Solution:
    def removeDuplicates(self, s: str) -> str:
        l=[]
        for i in s:
            if len(l)==0:
                l.append(i)
            elif i==l[-1]:
                l.pop()
            else:
                l.append(i)
        return "".join(l)