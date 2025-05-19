class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        """
        :type nums: List[int]
        :rtype: bool
        """
        for num in nums:
            if num in seen:
                    return True
            seen.add(num)
        return False    