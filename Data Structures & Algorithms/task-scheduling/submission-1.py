class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
#逆向最小堆 
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q  = deque()

        while maxHeap or q:
            time+= 1 
            
            if not maxHeap:
                time = q[0][1]

            else:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    #q里存的是：cnt剩余的量，和下次执行的固定时间
                    q.append([cnt,time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
        
        