class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = set()

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap.add(nums[i])
        return False