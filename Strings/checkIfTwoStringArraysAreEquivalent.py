class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i=0
        j=0
        m=len(word1)
        n=len(word2)
        l1=0
        l2=0
        while i<m and j<n:
            if word1[i][l1]!=word2[j][l2]:
                return False
            else:
                l1+=1 
                l2+=1
                if l1==len(word1[i]):
                    i+=1 
                    l1=0
                if l2==len(word2[j]):
                    j+=1
                    l2=0
        if i<m or j<n:
            return False
        else:
            return True