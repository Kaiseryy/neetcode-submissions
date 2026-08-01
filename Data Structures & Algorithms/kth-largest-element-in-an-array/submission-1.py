class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #记住这个函数heapq.nlargest
        return heapq.nlargest(k,nums)[-1]
        