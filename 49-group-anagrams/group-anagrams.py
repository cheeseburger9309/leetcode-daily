class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for s in strs:
            charArray = [0] * 26
            for c in s:
                charArray[ord(c) - ord("a")] += 1
            hashmap[tuple(charArray)].append(s)
        return hashmap.values()
            
        
        
        