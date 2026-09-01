class Solution:
    def isPalindrome(self, s: str) -> bool:
        # removing spaces and other signs from string using isalnum() function
        arr ="".join(char for char in s if char.isalnum())
        arr = arr.lower()
        # Applying two pointers to check the elements 
        p1 = 0
        p2 = len(arr) -1

        while(p1<p2):
            if arr[p1] != arr[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True

# the isalnum() method return True is the character is alphabet or numeric value
# ie. a alphanumeric value
