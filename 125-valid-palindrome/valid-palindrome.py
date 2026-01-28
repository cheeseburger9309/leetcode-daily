class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char for char in s if char.isalnum()])
        s = s.lower()

        # return s == s[::-1]

        j = len(s) - 1
        i = 0

        while i < j:
            if s[i] == s[j]:
                j = j - 1
                i = i + 1
                continue
            else:
                return False
        return True
        