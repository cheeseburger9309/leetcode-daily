class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        # new.sort()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

            # for j in range(i+1, len(nums)):
            #     if nums[j] == target - nums[i]:
            #         return[i, j]
                

        # for i in range(len(nums)):
        #     t = target - nums[i]
        #     new[nums[i]] = t
        
        # j = -1
        # for key, value in new.items():
        #     j = j + 1
        #     a = value
        #     new.popitem()
        #     for k, key in enumerate(new):
        #         if key == a:
        #             return(j, k)
        #             break
                
