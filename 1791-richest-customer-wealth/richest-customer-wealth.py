class Solution(object):
    def maximumWealth(self, accounts):

         

        return max(sum(row) for row in accounts)

        
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        