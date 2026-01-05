class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}

        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        
        for char in t:
            if char in dict:
                dict[char] -= 1
            else:
                return False
        return all(value == 0 for value in dict.values())
            