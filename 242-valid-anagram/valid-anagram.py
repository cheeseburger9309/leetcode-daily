class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        str1 = sorted(s)
        str2 = sorted(t)

        return str1 == str2

            