class Solution:
    def countFreq(self, arr):
        #code here
        dic = {}
        # filling the dictionary with the key as element and frequency as value
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        return [[k,v] for k,v in dic.items()]
