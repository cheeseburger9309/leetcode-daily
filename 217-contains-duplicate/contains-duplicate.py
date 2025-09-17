class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Brute-force: 
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Sorting approach (Efficient approach):
        nums.sort()
        # if len(nums) > 1:
        for i in range(1, len(nums)):
            # print(nums[i])
            # print(nums[i+1])
            if nums[i] == nums[i-1]:
                return True
        return False
        # else:
            # return False

        # # Set Approach
        # nums_set = set()
        # # length = 1

        # for i in range(len(nums)):
        #     if nums[i] in nums_set:
        #         return True 
        #     else:
        #         nums_set.add(nums[i])
        # return False

            # if length == len(nums_set):
            #     length += 1
            # else:
            #     return False
        
        
            








        

