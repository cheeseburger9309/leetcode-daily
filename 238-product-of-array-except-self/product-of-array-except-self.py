class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1,n):
            prefix[i] = (nums[i-1]*prefix[i-1])

        for i in range(n-2, -1, -1):
            suffix[i] = (nums[i+1]*suffix[i+1])
        
        result = [0] * n

        for i in range(n):
            result[i] = prefix[i]*suffix[i]
        return result

