class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str1 = {}
        str2 = {}

        for char in s:
            if char in str1:
                str1[char] += 1
            else:
                str1[char] = 1

        for char in t:
            if char in str2:
                str2[char] += 1
            else:
                str2[char] = 1
        
        return str1 == str2
        

            