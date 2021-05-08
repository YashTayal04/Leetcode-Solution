class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l=[0]*26
        for i in sentence:
            l[ord(i)-ord('a')]+=1 
        for i in l:
            if i==0:
                return False
        return True