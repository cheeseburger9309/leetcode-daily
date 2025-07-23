class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        array = []
        if x<0:
            return False
        while x > 0:
            units = x%10
            array.append(units)
            x = int(x//10)
        if (len(array)%2) == 0:
            n = int(len(array)/2)
            print(array[:n], array[-1:n-1:-1])
            return array[:n] == array[-1:n-1:-1]
        else:
            n = int((len(array) - 1)/2)
            print(array[:n], array[-1:n:-1])
            return array[:n] == array[-1:n:-1]
        # print(array[:n], array[n+1:])
        

        