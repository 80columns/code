"""
https://www.hackerrank.com/challenges/swap-nodes-algo/problem
"""

class Node:
    def __init__(self, val, level):
        self.left = None
        self.right = None
        self.val = val
        self.level = level
        self.visited = False

def swapNodes(indexes, queries):
    head = Node(1, 1)
    nodeList = [head]
    currentNodeIndex = 0
    outputTrees = []

    for index in indexes:
        if index[0] != -1:
            nodeList[currentNodeIndex].left = \
                Node(index[0], nodeList[currentNodeIndex].level + 1)
            nodeList.append(nodeList[currentNodeIndex].left)
        
        if index[1] != -1:
            nodeList[currentNodeIndex].right = \
                Node(index[1], nodeList[currentNodeIndex].level + 1)
            nodeList.append(nodeList[currentNodeIndex].right)

        currentNodeIndex += 1

    for swapLevel in queries:
        for x in range(0, len(nodeList)):
            # swap the children at all valid indexes divisible by swapLevel
            if nodeList[x].level % swapLevel == 0:
                tempNode = nodeList[x].left
                nodeList[x].left = nodeList[x].right
                nodeList[x].right = tempNode

        currentNode = nodeList[0]
        outputTree = []
        nodeStack = []

        while len(outputTree) < len(nodeList):
            if currentNode.left is not None \
               and currentNode.left.visited == False:
                nodeStack.append(currentNode)
                currentNode = currentNode.left
            else:
                outputTree.append(currentNode.val)
                currentNode.visited = True

                if currentNode.right is not None:
                    currentNode = currentNode.right
                elif len(nodeStack) > 0:
                    currentNode = nodeStack.pop()

        outputTrees.append(outputTree)

        # reset the visited state for each node
        for node in nodeList:
            node.visited = False
    
    return outputTrees

def main():
    print(swapNodes([[2, 3], [-1, -1], [-1, -1]], [1, 1]))
    print(swapNodes([[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]], [2]))
    print(swapNodes([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], \
                     [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]], [2, 4]))

if __name__ == "__main__":
    main()