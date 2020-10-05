class LRUCache(object):
##EVICTION POP FROM TAIL
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache={}
        self.lruList=[] #list of keys
        self.capacity=capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.cache:
            #print -1
            return -1
        else:
            #update value the list
            v=self.cache[key]
            #
            index = self.lruList.index(key)
            if index==-1:
                return -1

            self.lruList.pop(index)
            #move to last
            self.lruList.append(key)

            #print self.lruList,v
            return v

    def put(self, k, v):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #EVICT
        if len(self.cache)==self.capacity and k not in self.cache:
            #evict last used; evict from head
            poped_key = self.lruList.pop(0)
            #print "evicted = %d"%poped_key
            self.cache.pop(poped_key)

        #ADD
        #recently updated
        if k in self.cache:
            #update list and add
            #print k,self.lruList,self.cache
            index = self.lruList.index(k)
            #print "found at index=%d"%index
            if index==-1:
                return -1
            self.lruList.pop(index)
            self.lruList.append(k)
            self.cache[k]=v
            #
        else:
            #add
            self.lruList.append(k)
            self.cache[k]=v


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#["LRUCache","get","put","get","put","put","get","get"]
#[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

Lcache =LRUCache(2) #/* capacity */ );
Lcache.get(2)
Lcache.put(2, 6)
#print Lcache.lruList,Lcache.cache
Lcache.get(1)
Lcache.put(1, 5)
Lcache.put(1, 2)


#Lcache.get(1)
#Lcache.get(2)
