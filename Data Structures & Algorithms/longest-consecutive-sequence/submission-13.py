class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        sortednums=sorted(set(nums))
        if len(sortednums)==1:
            return 1
        currentn=sortednums[0]
        print(currentn)
        count=0
        print(sortednums)
        maxcount=1

        for x in range(0,len(sortednums)):
            if sortednums[x]==sortednums[x-1]+1:
                print(currentn,sortednums[x])
                currentn=sortednums[x]
                count+=1
                maxcount=max(count,maxcount)
            else:
                count=1
        return maxcount



        