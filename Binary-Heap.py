from heapq import heappop, heappush, heapify

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1)//2
    
    def insert(self, key):
        heappush(self.heap, key)

    def decreaseKey(self, i, val):
        self.heap[i]  = val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
    
    def delete(self, key):
        self.decreaseKey(key,float("-inf"))
        return heappop(self.heap)
    
    def GetMin(self):
        return self.heap[0]
    
heapObj = MinHeap()
heapObj.insert(3)
heapObj.insert(2)
heapObj.delete(1)
heapObj.insert(15)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(45)
print(heapObj.GetMin())
heapObj.decreaseKey(2, 1)
print(heapObj.GetMin())