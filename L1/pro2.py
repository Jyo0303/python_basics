class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        pal=0
        temp=0
        x1=x
        while x!=0:
            temp=x%10
            pal=pal*10+temp
            x=x//10
        return pal==x1
            
