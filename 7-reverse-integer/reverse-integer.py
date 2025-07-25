class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        flag = 0
        if x<0:
            flag = 1
            x = -1*(x)
            print(x)
        while x > 0:
            digit = x%10
            sum = (sum*10) + digit
            x = int(x//10)
        if sum > (pow(2, 31) - 1):
            return 0
        elif (flag == 1):
            print(sum)
            sum = -1*(sum)
        return sum