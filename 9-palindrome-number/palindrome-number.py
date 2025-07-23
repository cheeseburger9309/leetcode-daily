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
        print(sum, x)
        return(sum == x)

        # array = []
        # if x<0:
        #     return False
        # while x > 0:
        #     units = x%10
        #     array.append(units)
        #     x = int(x//10)
        # if (len(array)%2) == 0:
        #     n = int(len(array)/2)
        #     print(array[:n], array[-1:n-1:-1])
        #     return array[:n] == array[-1:n-1:-1]
        # else:
        #     n = int((len(array) - 1)/2)
        #     print(array[:n], array[-1:n:-1])
        #     return array[:n] == array[-1:n:-1]
        # # print(array[:n], array[n+1:])
        

        