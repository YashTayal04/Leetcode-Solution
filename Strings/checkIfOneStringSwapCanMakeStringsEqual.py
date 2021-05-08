class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        f=0
        p=-1
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if f>=2:
                    return False
                elif f==0:
                    f=1 
                    p=i
                else:
                    f=2 
                    if s1[i]==s2[p] and s1[p]==s2[i]:
                        pass
                    else:
                        return False
        if f==1:
            return False
        else:
            return True
                