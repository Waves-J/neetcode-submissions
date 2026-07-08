# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            curr = dummy
            carry = 0
            
            while l1 or l2 or carry:
                val1 = l1.val if l1 else 0
                val2 = l2.val if l2 else 0
                
                total = val1 + val2 + carry
                carry = total // 10
                
                if l1:
                    # If l1 still has nodes, overwrite its value and link to it
                    l1.val = total % 10
                    curr.next = l1
                elif l2:
                    # If l1 is empty but l2 has nodes, overwrite l2 and link to it
                    l2.val = total % 10
                    curr.next = l2
                else:
                    # We only create a new node if both lists are dead but we have a leftover carry 
                    curr.next = ListNode(total % 10)
                    
                # Shift everything forward safely
                curr = curr.next
                if l1: l1 = l1.next
                if l2: l2 = l2.next
                
            return dummy.next

        