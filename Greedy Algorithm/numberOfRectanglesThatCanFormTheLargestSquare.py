class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        s=min(rectangles[0][0],rectangles[0][1])
        for i in rectangles:
            s=max(s,min(i[0],i[1]))
        ans=0
        for i in rectangles:
            if s==min(i[0],i[1]):
                ans+=1
        return ans