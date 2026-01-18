class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        final = set()
        for num in nums:
            if num in final:
                return True
            final.add(num)
        return False


        
