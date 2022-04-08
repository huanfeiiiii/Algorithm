# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c1, c2 = headA, headB
        k1, k2 = 0, 0
        while c1:
            c1 = c1.next
            k1 += 1
        while c2:
            c2 = c2.next
            k2 += 1
        c1, c2 = headA, headB
        if k1 > k2:
            for i in range(k1 - k2):
                c1 = c1.next
        if k2 > k1:
            for i in range(k2 - k1):
                c2 = c2.next
        while c1 != c2:
            c1 = c1.next
            c2 = c2.next
        return c1
