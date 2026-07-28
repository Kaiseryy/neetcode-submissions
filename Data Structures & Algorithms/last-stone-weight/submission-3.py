class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)
        #最小堆它永远是最小的在上面，你取出来的也一直是最小的（堆顶）

        while len(stones) >1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones,first - second)
        
        stones.append(0)
        return abs(stones[0])
        