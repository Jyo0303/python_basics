class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        first = strs[0]

        for i in range(len(first)): 
            ch = first[i]
            for word in strs[1:]:
                
                if i >= len(word) or word[i] != ch:
                    return prefix
            prefix += ch  
        return prefix
