# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len_1 = 0
        len_2 = 0
        curr1 = l1
        curr2 = l2

        while curr1 != None:
            len_1 += 1
            curr1 = curr1.next
        
        while curr2 != None:
            len_2 += 1
            curr2 = curr2.next

        if len_2 > len_1:
            l1, l2 = l2, l1

        head = l1
        prev = None
        curr1 = l1
        curr2 = l2

        carry = 0

        while curr1 != None and curr2 != None:
            quotient = (curr1.val + curr2.val + carry) % 10
            carry = (curr1.val + curr2.val + carry) // 10
            curr1.val = quotient
            prev = curr1
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1 != None:
            quotient = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            curr1.val = quotient
            prev = curr1
            curr1 = curr1.next
        
        if carry == 1:
            prev.next = ListNode(1)
        
        return head


        