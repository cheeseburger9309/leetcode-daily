class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hashmap_s, hashmap_t = {}, {}

        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
        
        for j in range(len(t)):
            hashmap_t[t[j]] = 1 + hashmap_t.get(t[j], 0)

        if hashmap_t == hashmap_s:
            return True
        else:
            return False
        
        