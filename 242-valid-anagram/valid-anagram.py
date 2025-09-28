class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hashmaps, hashmapt = {}, {}

        for i in range(len(s)):
            hashmaps[s[i]] = 1 + hashmaps.get(s[i], 0)
            hashmapt[t[i]] = 1 + hashmapt.get(t[i], 0)
        return hashmaps == hashmapt
    
        