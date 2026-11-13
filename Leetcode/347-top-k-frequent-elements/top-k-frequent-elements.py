class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen={}
        result=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1
        sorted_items = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        for key, value in sorted_items[:k]:
            result.append(key)
        return result
            


            



        