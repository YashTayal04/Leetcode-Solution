class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s=set()
        p=''
        f=0
        for i in word:
            if i=='0':
                f=1
                if len(p)!=0:
                    p+=i
            elif i>='0' and i<='9':
                f=0
                p+=i
            else:
                if len(p)>0:
                    s.add(p)
                elif f==1:
                    s.add('0')
                f=0
                p=''
        if len(p)>0:
            s.add(p)
        elif f==1:
            s.add('0')
        return len(s)