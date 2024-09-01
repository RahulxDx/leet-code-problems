class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        l = []
        for i in digits:
            s = s + str(i)
        f = int(s)
        f = f + 1
        for j in str(f):
            l.append(int(j))
        return l
        
