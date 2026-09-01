class Solution:
    def isPalindrome(self, s: str) -> bool:
        # removing spaces from the string
        arr =[]
        s = s.lower()    #making the string in lower letters 
        for i in s:
            # removing non alphabetic char
            if ord(i)>= 97 and ord(i) <= 122:  #keeping only alphabets
                arr.append(i)
            if ord(i)>=48 and ord(i)<=57:   #keeping the numbers also
                arr.append(i)

        # if array is empty then also its palindrome
        if len(arr) == 0:
            return True

        # Applying two pointers to check the elements 
        p1 = 0
        p2 = len(arr) -1

        while(p1<p2):
            if arr[p1] != arr[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True
