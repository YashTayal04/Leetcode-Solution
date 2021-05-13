class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x:(x[1],x[0]))
        ans=0
        for i in boxTypes:
            if i[0]<=truckSize:
                ans+=i[0]*i[1]
                truckSize-=i[0]
            else:
                ans+=truckSize*(i[1])
                break
        return ans