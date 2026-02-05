class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sum = 0

        for i in range(len(nums)):
            sum = sum + nums[i]
            result.append(sum)

        return result
            
        