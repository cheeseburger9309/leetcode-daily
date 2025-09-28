class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmaps = {}
        hashmapt = {}

        for char in s:
            hashmaps[char] = 1 + hashmaps.get(char, 0)
        for char in t:
            hashmapt[char] = 1 + hashmapt.get(char, 0)
        return hashmaps == hashmapt
    
        