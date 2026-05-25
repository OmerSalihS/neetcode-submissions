class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Final_list=set(nums)
        if len(Final_list)==len(nums):
            return False
        return True
        
        