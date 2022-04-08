# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        p = result
        while l1 and l2:
            num = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            p.next = ListNode(num)
            l1 = l1.next
            l2 = l2.next
            p = p.next

        l3 = l1 if l1 else l2
        while l3:
            num = (l3.val + carry) % 10
            carry = (l3.val + carry) // 10
            p.next = ListNode(num)
            p = p.next
            l3 = l3.next
        if carry == 1:
            p.next = ListNode(1)
        return result.next
