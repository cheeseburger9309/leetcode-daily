class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char for char in s if char.isalnum()])
        s = s.lower()

        j = len(s) - 1

        for i in range(j+1):
            if s[i] == s[j]:
                j = j - 1
                continue
            else:
                return False
        return True
        