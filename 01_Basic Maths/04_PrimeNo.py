class Solution:
    def isPrime(self, n):
        # code here
        if n ==1:
            return False
        for i in range (n-1,1,-1):
            if (n %  i == 0):
                return False
        return True
