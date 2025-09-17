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

        nums.sort()
        if len(nums) > 1:
            for i in range(len(nums) - 1):
                print(nums[i])
                print(nums[i+1])
                if nums[i] == nums[i+1]:
                    return True
            return False
        else:
            return False




        

