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
        #you cant straight away map because random may point to a later node which not be created yet
        #store old and new copy as a hashmap
        oldToNew = {None : None} #hashmap
        curr = head
        while curr:
            copyNode = Node(curr.val)
            oldToNew[curr] = copyNode
            curr = curr.next
        #now all nodes are created so you can start mapping
        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]    
