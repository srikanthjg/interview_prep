class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def hasCycle(self, head):
    slow = head
    fast = head

    while(fast and fast.next):
        if(slow==fast):
            return 1
        slow = slow.next
        fast = fast.next.next

    return 0

  def printLL(self,head):
      while(head):
          print "%d->"%head.val
          head = head.next


head = [4,3,2,1,0]
pos = 1
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
testTail.next = node1

sol = Solution()
#sol.printLL(testHead)
print sol.hasCycle(testHead)



print(Solution().hasCycle(testHead))
