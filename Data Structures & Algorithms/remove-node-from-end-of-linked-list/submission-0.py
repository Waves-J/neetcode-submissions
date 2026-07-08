# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
        
        prev = None
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next

        if prev == None:
            return head.next
        else:
            prev.next = slow.next
            return head
        