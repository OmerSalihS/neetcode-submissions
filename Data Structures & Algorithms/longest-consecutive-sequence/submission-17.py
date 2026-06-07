class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset=set(nums)
        maxcount=0
        for n in numset:
            if n - 1 not in numset:
                count=1
                while n+count in numset:
                    count+=1
                maxcount=max(count,maxcount)
        return maxcount

      


        