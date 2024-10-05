# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head.prev = None
        tail = head
        while tail.next:
            tail.next.prev = tail
            tail = tail.next

        front, back = head, tail
        while front != back and back.next != front:
            if front.val != back.val:
                return False
            front = front.next
            back = back.prev
        return True
