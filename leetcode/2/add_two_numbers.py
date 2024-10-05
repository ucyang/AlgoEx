# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lr = ret = ListNode()
        la = l1
        lb = l2
        s = 0

        while la or lb or s:
            if la:
                s += la.val
                la = la.next

            if lb:
                s += lb.val
                lb = lb.next

            lr.next = ListNode(s % 10)
            lr = lr.next

            s //= 10

        return ret.next
