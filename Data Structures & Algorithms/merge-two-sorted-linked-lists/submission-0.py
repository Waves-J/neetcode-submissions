# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        if curr1 == None:
            return curr2
        elif curr2 == None:
            return curr1

        if curr1.val <= curr2.val:
            head = curr1
            curr = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr = curr2
            curr2 = curr2.next

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr2
                curr2 = curr2.next
        
        if curr1 != None:
            curr.next = curr1
        elif curr2 != None:
            curr.next = curr2
        
        return head