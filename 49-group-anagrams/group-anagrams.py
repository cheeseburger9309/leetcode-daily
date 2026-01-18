class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hashmap = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            hashmap[key].append(s)
            # else:
            #     hashmap[key] = [s]
        
        return hashmap.values()
        
