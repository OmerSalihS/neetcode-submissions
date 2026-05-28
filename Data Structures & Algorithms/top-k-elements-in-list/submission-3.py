class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countlist={}
        last=[]
        for x in nums:
            if x not in countlist.keys():
                countlist[x]=1
            else:
                countlist[x]+=1
        lastdict=sorted(countlist.items(),key=lambda x: x[1], reverse=True)
        for y in range(0,k):
            last.append(lastdict[y][0])
        return last

        
        