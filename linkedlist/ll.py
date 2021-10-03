class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def __init__(self):
        self.head = None

    def printLL(self):
        cur=self.head
        while(cur):
            print "%d->"%(cur.val),
            cur = cur.next

    def insert(self,val):
        if self.head == None:
            self.head = Node(val)
        else:
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = Node(val)
        return

    def find_mid(self):
        i=0
        slow = self.head
        fast = self.head

        while(fast and fast.next):
            i+=1
            slow = slow.next
            fast = fast.next.next
        #slow will be the mid node
        return i

    def reverse(self):
        prev = None
        cur = self.head

        while(cur):
            if cur.next == None:
                self.head = cur
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return

sol = Solution()
##how to pass head from outside instead of self.head
sol.insert(1)
sol.insert(2)
sol.insert(3)
sol.insert(4)
sol.insert(5)
sol.insert(6)
sol.insert(7)
sol.insert(8)
sol.printLL()
print ""
print sol.find_mid()
sol.reverse()
sol.printLL()
