class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        if len(num1) >= 1 and len(num2) <= 10**4:
            f = int(num1) + int(num2)
        return str(f)
