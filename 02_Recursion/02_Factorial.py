class Solution:
    fact = 1
    def factorial(self, n: int) -> int:
        # code here
        if n ==1 or n == 0: 
            return self.fact
        return n* self.factorial(n-1)
