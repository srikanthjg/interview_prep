# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum=0
        carry=0
        l3=None
        out=[]
        while(True):
            if(l1==None and l2==None):
                break
            if(l1==None and l2):
                s1=0
                s2=l2.val
            if(l1 and l2==None):
                s1=l1.val
                s2=0
            if(l1 and l2):
                s1=l1.val
                s2=l2.val

            addition = carry + (s1 + s2)
            sum = addition%10
            carry = addition//10

            #print sum,
            if(l3==None):
                l3 = ListNode(sum)
                cur=l3
            else:
                cur.next = ListNode(sum)
                cur=cur.next

            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
            #print l1.val

            if(carry!=0 and (l1==None and l2==None)):
                cur.next = ListNode(carry)
                cur=cur.next
            #print out,sum,carry


        return l3
