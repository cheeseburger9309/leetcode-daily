class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sum = 0
        temp = x
        while temp > 0:
            units = temp%10
            sum = (sum*10) + units
            temp = int(temp//10)
        # print(sum, x)
        return(sum == x)

        
        

        