# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        if not cur:
            return None
        if cur.next is None:
            return cur
        sentinel = ListNode(0, head)
        cur = sentinel.next
        prev = sentinel
        while cur :
            #print(cur.val)
            if cur.next and cur.val==cur.next.val:
                #move cur till same
                while cur.next and cur.val==cur.next.val:
                    cur=cur.next
                prev.next=cur.next
                cur=cur.next
            else:
                prev=prev.next
                cur=cur.next
        return sentinel.next
