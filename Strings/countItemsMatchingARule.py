class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        x=0 
        if ruleKey=='color' :
            x=1
        elif ruleKey=='name' :
            x=2
        c=0
        for i in items:
            if i[x]==ruleValue:
                c+=1
        return c