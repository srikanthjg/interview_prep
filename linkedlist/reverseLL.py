class Node(object):
    def __init__(self,val):
        self.val =val
        self.next = None

class Solution(object):
    def __init__(self):
        self.head = None

    def printLL(self,node):
        cur = node
        while(cur):
            print "%d->"%(cur.val),
            cur = cur.next
        print ""

    def insert(self,val):
        if self.head == None:
            self.head = Node(val)
            return

        cur = self.head
        while(cur.next!=None):
            cur = cur.next
        cur.next = Node(val)

    def reverse_rec(self,node):

        if node.next == None:
            self.head = node
            return None


        self.reverse_rec(node.next)
        node.next.next = node # make the next node point to cur
        node.next = None 

        return



sol = Solution()
sol.insert(1)
sol.insert(2)
sol.insert(3)
sol.insert(4)
sol.printLL(sol.head)

sol.reverse_rec(sol.head)
sol.printLL(sol.head)
