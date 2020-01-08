import heapq;
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        n = len(A);
        heap = [];
        for i in range(B):
            heapq.heappush(heap,-A[i]);
        
        
        for i in range(B,n):
            if(-heap[0] > A[i]):
                heapq.heappop(heap);
                heapq.heappush(heap,-A[i]);
                
        return -heapq.heappop(heap);
