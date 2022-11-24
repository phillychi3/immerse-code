class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == len(nums)-1:
                break
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j and j>i:
                    return [i,j]
                    
        return output