class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1 ,max(piles)
        res = r

        while l<=r:
            #k不断变化 一定要写在while里
            k = l + ((r-l)//2)
            totaltime = 0
            for p in piles:
                totaltime += math.ceil(p / k)

            if totaltime<= h:
                res = k
                r = k-1
            else:
                l = k+1
            
        return res


            
        
           

            
            

             