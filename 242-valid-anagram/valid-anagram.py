class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hashmap = {}

        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        for char in t:
            if char not in hashmap or hashmap[char] == 0:
                return False
            hashmap[char] -= 1 
        return True

        
    
        