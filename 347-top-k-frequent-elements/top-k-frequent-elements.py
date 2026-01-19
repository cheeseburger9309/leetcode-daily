class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        result = sorted(hashmap.items(), key = lambda x: x[1], reverse = True)

        return [item[0] for item in result[:k]]
        
            
        