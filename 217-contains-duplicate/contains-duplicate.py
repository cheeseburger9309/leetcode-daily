class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupset = set()

        for n in nums:
            if n in dupset:
                return True
            dupset.add(n)
        return False

        
        