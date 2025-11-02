class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)

        for i in range(n-m+1):
            s=""
            j=0
            while j<m and haystack[i+j]==needle[j]:
                s+=haystack[i+j]
                j+=1
            if s==needle:
                return i
        return -1
