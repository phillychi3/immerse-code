class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        isee = {}
        for i in nums:
            if i in isee:
                return True
            isee[i]=i
        return False
        