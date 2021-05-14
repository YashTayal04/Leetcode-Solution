class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s=[]
        for i in logs:
            if i=='./':
                continue
            elif i=='../':
                if len(s)>0:
                    s.pop()
            else:
                s.append(i)
        return len(s)