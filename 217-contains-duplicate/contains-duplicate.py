class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(1, n):
                if nums[i]==nums[i-1]:
                    return True
        return False    