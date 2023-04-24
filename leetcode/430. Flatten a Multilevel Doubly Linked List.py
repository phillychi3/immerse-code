"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: 
            return None

        node = head
        while node:
            if node.child:
                flattened = self.flatten(node.child)
                node.child = None
                nextNode = self.appendtolist(node, flattened)
                node = nextNode
            else:
                node = node.next
        return head
    
    def appendtolist(self, node, flattened):
        next_node = node.next
        node.next = flattened
        flattened.prev = node
        while node.next:
            node = node.next
        node.next = next_node
        if next_node:
            next_node.prev = node
        return next_node