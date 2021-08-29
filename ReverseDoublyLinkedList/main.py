"""
https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
"""

def reverse(llist):
    if llist is None or (llist.next is None and llist.prev is None):
        return llist
    
    tempNode = llist
    prevNode = None
    
    while tempNode.next is not None:
        tempNode.prev = tempNode.next
        tempNode.next = prevNode
        
        prevNode = tempNode
        tempNode = tempNode.prev
        
    tempNode.prev = None
    tempNode.next = prevNode
    
    return tempNode