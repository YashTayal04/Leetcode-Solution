class Solution:
    def secondHighest(self, s: str) -> int:
        l=-1
        sl=-1
        for i in s:
            if i>='0' and i<='9':
                i=int(i)
                if i>l:
                    sl=l
                    l=i 
                elif i<l and i>sl:
                    sl=i
        return sl