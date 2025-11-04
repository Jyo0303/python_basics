class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in range(len(digits)):
            s=s+str(digits[i])
        n=int(s)+1
        m= str(n)
        l=[]
        for i in range(len(m)):
            l.append(int(m[i]))
        return l
