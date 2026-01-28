class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ''.join([char for char in s if char.isalnum()])
        lower = cleaned.lower()

        j = len(lower) - 1

        for i in range(j+1):
            if lower[i] == lower[j]:
                j = j - 1
                continue
            else:
                return False
        return True
        