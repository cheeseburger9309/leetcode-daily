class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)  # O(n) time and space
        smallest = 1

        while smallest in nums_set:
            smallest += 1

        return smallest
        # smallest = 1
        # i = 0

        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         if nums[i] == smallest:
        #             smallest = smallest + 1
                    
        #         elif nums[i] > smallest:
        #             continue
        # return smallest
            