class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        str1 = {}

        for char in s:
            if char in str1:
                str1[char] += 1
            else:
                str1[char] = 1

        for char in t:
            if char in str1:
                str1[char] -= 1
            else:
                str1[char] = 1
        
        return not any(str1.values()) 
        

            