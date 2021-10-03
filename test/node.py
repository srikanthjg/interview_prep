class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution():
    def swapPair(self,node):
        """
        input:1->2->3   ;  1->2->3->4
        output:(2->1)->(3)  ;  (2->1)->(4->3)
        """
        #no node
        if not node:
            return None

        #only one node
        if not node.next:
            return node

        one = node
        two = node.next
        three = node.next.next

        #swap
        two.next=one
        one.next=self.swapPair(three)

        return two

    def is_sizeLL_lessk(self,node,k):
        cur=node
        n=1
        while cur:
            if n>=k:
                return False
            cur=cur.next
            n+=1
        return True

    def reverseLLk(self,node,k):
        """
        return head of reversed LL, last node of reversedLL,first node of next LL after k
        """
        if not node:
            return
        cur = node
        prev = None
        n=k
        while n and cur:
            #store
            nxt=cur.next
            #operate
            cur.next = prev
            #prepare for next iteration
            prev = cur
            cur = nxt
            n-=1

        next_ll_head = cur
        return prev,node,next_ll_head


    def swapPairk(self,node,k):
        """
        input:1->2->3   ;  1->2->3->4
        output:(2->1)->(3)  ;  (2->1)->(4->3)
        """
        #no node
        if not node:
            return None

        #size of cur node length is less than k then return node
        if self.is_sizeLL_lessk(node,k):
            return node

        #size of node == k ; then reveseLL of size k
        cur=node
        first,last,next_ll_head = self.reverseLLk(cur,k)
        last.next=self.swapPairk(next_ll_head,k)
        return first


#build LL
root=Node(1)
cur=root
for i in range(2,5):
    cur.next=Node(i)
    cur=cur.next

def printLL(node):
    if not node:
        return
    print(node.val)
    printLL(node.next)

s=Solution()
printLL(root)
print("")


"""
#test revLLk
first,last,next_head=s.reverseLLk(root,2)
print(first.val,next_head.val)
printLL(first)
print("")
"""

#test swapk
head=s.swapPairk(root,3)
printLL(head)
