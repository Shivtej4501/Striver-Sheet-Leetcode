class Solution:
    def reverseArray(self, arr):
        # code here
        p2 = len(arr) -1
        p1 = 0
        while(p1<p2):
            arr[p1],arr[p2] = arr[p2], arr[p1]
            p1 +=1
            p2 -=1
        return arr
        
        
        
