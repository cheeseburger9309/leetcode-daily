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
            else:
                final.add(num)
        return False


        
