class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        f = ''
        for i in l:
            rev_i = i[::-1]
            f += rev_i + ' ' 
        return f.strip()
