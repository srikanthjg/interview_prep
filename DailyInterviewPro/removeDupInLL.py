class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Solution(object):
  def printLL(self, head):
      tmp=head
      while(tmp):
          print "%r->"%tmp.val,
          tmp=tmp.next
      print "None"
  def deleteDuplicates(self, node):
    head=node
    if head == None:
        return None

    cur=head
    dupHead=None

    while cur.next:
        if cur.val == cur.next.val:
            dupHead=cur.next
            while cur.val == dupHead.val:
                dupHead=dupHead.next
            cur.next=dupHead
            cur=dupHead
            continue
        cur=cur.next
    return head


n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
#print(n)
sol = Solution()
sol.printLL(n)
# 1 2 3 3 4

sol.deleteDuplicates(n)
#print(n)
print"After"
sol.printLL(n)
