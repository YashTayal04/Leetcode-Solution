class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        k=0
        ans=''
        l=len(word1)
        m=len(word2)
        while i<l and j<m:
            if k%2==0:
                ans+=word1[i]
                i+=1
            else:
                ans+=word2[j]
                j+=1
            k+=1
        while i<l:
            ans+=word1[i]
            i+=1
        while j<m:
            ans+=word2[j]
            j+=1
        return ans