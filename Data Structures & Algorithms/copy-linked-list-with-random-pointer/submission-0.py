"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        randmap = {}

        curr = head
        
        while curr != None:
            if curr not in randmap:
                randmap[curr] = Node(curr.val)
            copy = randmap[curr]
            if curr.next != None and curr.next not in randmap:
                next_copy = Node(curr.next.val)
                randmap[curr.next] = next_copy
            if curr.random != None and curr.random not in randmap:
                rand_copy = Node(curr.random.val)
                randmap[curr.random] = rand_copy
            if curr.next in randmap:
                copy.next = randmap[curr.next]
            if curr.random in randmap:
                copy.random = randmap[curr.random]
            curr = curr.next
        
        return randmap[head]
        


            
