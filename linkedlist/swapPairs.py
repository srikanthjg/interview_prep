#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def __init__(self):
        self.head = None
        self.count=0
    def printLL(self):
        cur = self.head
        while(cur):
            print cur.val
            cur = cur.next
            self.count = self.count +1

    def insert(self,val):
        cur = self.head
        if(cur==None):
            cur = ListNode(val)
            self.head = cur
        else:
            while(cur.next!=None):
                cur = cur.next
            cur.next = ListNode(val)

    def swapHelper(self,head,cur):
        #1
        if(cur and cur.next == None):
            if(self.count==1):
                self.head = cur
            return
        #2
        elif(cur.next and cur.next.next == None):
            if self.count == 2:
                cur.next.next = cur
                self.head = cur.next
                cur.next = None
            else:
                cur.next.next = cur
                #self.head = cur.next
                cur.next = None
        #3
        elif(cur.next.next and cur.next.next.next == None):
            if self.count == 3:
                tmp = cur.next.next
                cur.next.next = cur
                self.head = cur.next
                cur.next = tmp
            else:
                tmp = cur.next.next
                cur.next.next = cur
                #self.head = cur.next
                cur.next = tmp


        return


    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head

        first=head
        second=head.next

        first.next=self.swapPairs(second.next)
        second.next=first
        return second


head=None
sol = Solution()
for i in range(1,4):
    sol.insert(i)

sol.printLL()
print "count=%d"%sol.count
sol.head=sol.swapPairs(sol.head)
print ""
sol.printLL()
