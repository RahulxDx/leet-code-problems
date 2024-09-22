class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        is_negative = x < 0
        x = abs(x)
        count = 0

        while x > 0:
            last = x % 10
            rev = (rev * 10) + last
            x //= 10
    
        if is_negative:
            rev = -rev
        
        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        return rev
