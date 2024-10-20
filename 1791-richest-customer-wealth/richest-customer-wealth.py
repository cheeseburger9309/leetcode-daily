class Solution(object):
    def maximumWealth(self, accounts):

        row_sums = [sum(row) for row in accounts]  

        return max(row_sums)

        
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        