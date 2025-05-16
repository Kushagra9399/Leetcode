# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a = l1
        b = l2
        c = 0
        prev = a
        while a or b:
            if a is not None and b is not None:
                k = a.val + b.val + c
                c = k//10
                a.val = k%10
                prev = a
                a = a.next
                b = b.next
            elif a is not None:
                k = a.val + c
                c = k//10
                a.val = k%10
                prev = a
                a = a.next
            elif b is not None:
                k = b.val + c
                c = k//10
                prev.next = ListNode(k%10)
                prev = prev.next
                b = b.next
        if c!=0:
            prev.next = ListNode(c)
        return l1
