# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = set()
        curr = head

        while curr != None:
            if curr.next in hashmap:
                return True
            hashmap.add(curr)
            curr = curr.next

        return False