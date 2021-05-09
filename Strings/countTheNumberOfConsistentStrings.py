class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        c=0
        for i in words:
            c+=1
            for j in i:
                if j not in s:
                    c-=1
                    break
        return c