class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s=sum(nums)//2
        c=0
        l=[]
        nums.sort(reverse=True)
        for i in nums:
            c+=i
            l.append(i)
            if c>s:
                return l