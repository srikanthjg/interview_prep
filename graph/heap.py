"""
Insert/Del from bottom
max_heapify from top
"""
"""
import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val

heapq.heappop(minheap)      # pop from minheap
heapq._heappop_max(maxheap) # pop from maxheap

"""
class Heap():
    def build_max_heap(self,arr):
        half=len(arr)//2-1
        for i in range(half,-1,-1):
            self.max_heapify(arr, i)
        return

    def max_heapify(self,arr,index):
        l=(2*index)+1
        r=(2*index)+2
        n=len(arr)

        if l<n and arr[l]>arr[index]:
            largest=l
        else:
            largest=index

        if r<n and arr[r]>arr[largest]:
            largest=r

        if largest!=index:
                arr[largest],arr[index]=arr[index],arr[largest]
                self.max_heapify(arr, largest)
        return
    def extract_max_heap(self,arr):
        max_ele=arr[0]
        arr[-1],arr[0]=arr[0],arr[-1]
        arr.pop()
        self.max_heapify(arr, 0)
        return max_ele

    def parent(self,arr,i):
        if i>len(arr)-1:
            return -1
        return arr[(i-1)//2]

    def heap_insert(self,arr,val):
        arr.append(val)
        i=len(arr)-1
        parent=(i-1)//2
        #print arr[i],arr[parent],i
        while arr[i]>arr[parent]:
            arr[parent],arr[i]=arr[i],arr[parent]
            i=parent
            #print i
        return


arr=[2,5]
heap=Heap()
heap.build_max_heap(arr)
heap.insert(arr,7)
print arr
