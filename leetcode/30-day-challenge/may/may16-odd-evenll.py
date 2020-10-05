class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def __init__(self):
        self.root=None

    def printLL(self):
        cur=self.root
        while(cur):
            print "%d->"%(cur.val),
            cur = cur.next

    def printLL2(self,root):
        cur=root
        while(cur):
            print "%d->"%(cur.val),
            cur = cur.next

    def insert(self,val):
            cur = self.root
            while(cur.next):
                cur = cur.next
            cur.next = Node(val)
            return

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        odd_head=head
        even_head=head.next

        cur=odd_head
        while(cur):
            tmp=cur.next
            if cur.next:
                cur.next=cur.next.next
            if tmp and tmp.next:
                tmp.next=tmp.next.next
            cur=cur.next

        cur=odd_head
        while(cur.next):
            cur=cur.next
        cur.next=even_head

        return odd_head

sol = Solution()

sol.root=Node(1)
sol.insert(2)
sol.insert(3)
sol.insert(4)
sol.insert(5)
sol.printLL()
print ""
sol.oddEvenList(sol.root)
