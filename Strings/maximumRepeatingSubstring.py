class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans=0
        l=len(word)
        for i in range(len(sequence)):
            c=0
            j=0
            for k in sequence[i:]:
                if word[j]==k:
                    j+=1 
                    if j==l:
                        c+=1 
                        j=0
                else:
                    break
            ans=max(ans,c)
        return ans