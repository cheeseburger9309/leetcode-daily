class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high)//2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                high = middle -1
            if nums[middle] < target:
                low = middle + 1
        else:
            return -1

        