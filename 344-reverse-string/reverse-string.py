class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        k = (len(s) - 1)
        j = (len(s) - 1)
        

        while i < j:
            temp = s[i]        
            s[i] = s[j]        
            s[j] = temp
            i = i+1
            j = j-1
            
        
