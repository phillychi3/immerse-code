class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxnum = 0
        mm = -9999999999999
        for i in nums:
            if maxnum > 0:
                maxnum+=i
            else:
                maxnum = i
            
            mm = max(mm,maxnum)
        return mm