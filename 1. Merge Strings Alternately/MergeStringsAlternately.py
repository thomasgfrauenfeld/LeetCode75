class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_list = list(word1)
        word2_list = list(word2)
        merged = ""
        i = 0

        while i < len(word1) + len(word2):
            if len(word1_list) > 0:
                merged += word1_list.pop(0)

            if len(word2_list) > 0:
                merged += word2_list.pop(0)
            
            i += 1
        
        return merged