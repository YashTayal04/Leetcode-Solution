class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        c=1
        for i in target:
            while c!=i:
                ans.append("Push")
                ans.append("Pop")
                c+=1
            ans.append("Push")
            c+=1
        return ans