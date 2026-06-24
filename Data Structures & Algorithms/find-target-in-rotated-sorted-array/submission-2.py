class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        #先找到最小的那个数值和坐标
        while l<r:
            m = (r+l)//2

            if nums[m]>nums[r]:
                l=m+1
            else:
                r = m

        mini = l
         #然后确定target是在最小值的左边还是右边
        l,r=0,len(nums)-1

        if target>= nums[mini] and target<=nums[r]:
            l = mini
        else:
            r = mini-1
        
        #确定好是在最小值左侧或者右侧后 ，反正都是升序序列，继续二分法找就行了
        while l<=r:
            m = (l+r) //2
            if nums[m] == target:
                return m
            elif nums[m]<target:
                l = m+1
            else:
                r = m-1
        return -1


            
        