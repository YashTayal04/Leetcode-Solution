class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        c=1
        j=0
        i=0
        while i<len(sentence):            
            if sentence[i]==" ":
                i+=1
                c+=1
                j=0
            elif sentence[i]==searchWord[j]:
                i+=1
                j+=1
                if j==len(searchWord):
                    return c
            else:
                while i<len(sentence) and sentence[i]!=" ":
                    i+=1
                i+=1
                j=0
                c+=1
        return -1
                    