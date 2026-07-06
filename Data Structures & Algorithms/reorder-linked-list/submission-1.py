# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        prev = None

        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if fast != None:
            prev = slow
            slow = slow.next
            
        curr = slow
        prev.next = None
        prev = None

        while curr != None:
            curr.next, prev, curr = prev, curr, curr.next
        
        head2 = prev

        left = head
        right = head2

        while left != None and right != None:
            left_next = left.next
            right_next = right.next

            right.next = left.next
            left.next = right

            left = left_next
            right = right_next