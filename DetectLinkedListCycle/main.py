"""
https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
"""

def child_has_cycle(node, items):
    if node.data in items:
        return True
    
    items.add(node.data)
    
    if node.next is None:
        return False
    else:
        return child_has_cycle(node.next, items)

def has_cycle(head):
    if head is None or head.next is None:
        return False
    
    return child_has_cycle(head, set())