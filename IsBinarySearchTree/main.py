"""
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
"""

def checkNode(node, items, minVal, maxVal):
    if node.data in items \
       or (minVal is not None and node.data < minVal) \
       or (maxVal is not None and node.data > maxVal):
        return False
    
    items.add(node.data)
    
    leftResult = True if node.left is None else checkNode(node.left, items, minVal=minVal, maxVal=node.data)
    rightResult = True if node.right is None else checkNode(node.right, items, minVal=node.data, maxVal=maxVal)
    
    return (leftResult and rightResult)

def checkBST(root):
    items = set()
    
    return checkNode(root, items, None, None)