class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        sign = 1
        if x < 0:
            x = abs(x)
            sign *= -1    
        while(x > 0):
            lastDigit = x % 10
            num =  num * 10
            num += lastDigit
            x = x // 10
        num *= sign
        if num < -(2**31) or num > 2**31 -1 : 
            return 0
        return num 
