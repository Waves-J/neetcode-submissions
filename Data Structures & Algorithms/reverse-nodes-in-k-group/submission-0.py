# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        curr = head
        prev = None

        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = getKth(group_prev, k)
            
            if not kth:
                break

            group_next = kth.next

            prev, curr = kth.next, group_prev.next
            
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next