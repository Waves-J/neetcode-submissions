# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        
        curr = head

        while curr != None:
            curr = curr.next
            length += 1
        
        half = (length + 1) // 2

        prev = None
        curr = head
        index = 0
        while curr != None and index < half:
            prev = curr
            curr = curr.next
            index += 1
        
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