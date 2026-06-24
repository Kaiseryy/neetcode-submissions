class Solution:
    def hasDuplicate(self,nums):
        T=0
        for i in nums:
            n = nums.count(i)
            if n >=2 :
                T = 1
        if T ==1:
            return True
        else:
            return False
        

                
            
              
        