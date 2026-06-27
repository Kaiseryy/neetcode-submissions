class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
            #自己数学推导一遍
        slow2= 0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        