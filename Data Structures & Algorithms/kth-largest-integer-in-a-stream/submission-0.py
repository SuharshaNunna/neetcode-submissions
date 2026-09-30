class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # sort the stream : brute force
        # better to store a min heap( storing the largest elements )
        # the heap should of size k 
        self.minheap= nums
        self.k= k 
        # to change the array into a heap 
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap)> self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
        
