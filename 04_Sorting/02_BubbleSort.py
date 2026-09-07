class Solution:
    def bubbleSort(self,arr):
        # code here
        for i in range(len(arr)-1,-1,-1):
            swapped = 0
            for j in range (0,i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped +=1
            if swapped == 0:
                break
            
