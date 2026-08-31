class Solution:
    def armstrongNumber (self, n):
        # code here 
        k = len(str(n))   # getting length of the number
        num = n
        summ = 0
        while(n > 0):
            summ += (n%10)**k
            n = n//10
        return num == summ
