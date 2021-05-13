class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while numBottles>=numExchange:
            x=numBottles//numExchange
            ans+=x
            numBottles-=(x*(numExchange-1))
        return ans
        