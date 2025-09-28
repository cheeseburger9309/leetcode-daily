class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap = {}

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hashmap:
        #         return [hashmap[diff], i]
        #     hashmap[n] = i
        
        hashmap = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return hashmap[target-nums[i]], i
            else:
                hashmap[nums[i]] = i