class KthLargest:
    heap: list[int]
    k: int

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        # O(log N)
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            # O(log N)
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        # O(log k)
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            # O(log k)
            heapq.heappop(self.heap)
        # O(1)
        return self.heap[0]

        
