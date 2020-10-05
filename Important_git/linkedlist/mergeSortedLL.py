class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def __init__(self):
        self.head=None

    def mergeLL(self,l1,l2):
        if l1==None:
            self.head=l2
            return
        if l2==None:
            self.head=l1
            return

        cur1=l1
        cur2=l2
        if cur1.val<=cur2.val:
            self.head = cur1
        else:
            self.head = cur2

        cur = self.head
        while cur1 and cur2:
            if cur1.val<=cur2.val:
                cur.next = cur1
                cur1=cur1.next
            else:
                cur.next = cur2
                cur2=cur2.next

        if cur1:
            cur.next = cur1.val
        if cur2:
            cur.next = cur2.val

        return self.head

def printLL(head):
        cur=head
        while(cur):
            print "%d->"%(cur.val),
            cur = cur.next


#l1=[2,3,5,6]
sol = Solution()
l1 = Node(2)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next.next = Node(6)
print "\nl1"
printLL(l1)

#l2=[1,2,3,4,5]
l2 = Node(1)
l2.next = Node(2)
l2.next.next = Node(3)
l2.next.next.next = Node(4)
l2.next.next.next.next = Node(5)
print "\nl2"
printLL(l2)
print ""

h = sol.mergeLL(l1,l2)
printLL(h)
