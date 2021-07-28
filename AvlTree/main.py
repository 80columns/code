class AvlTreeNode:
    val = None
    left = None
    right = None

    def __init__(self):
        pass

    def __init__(self, val):
        self.val = val

    def insert(self, val):
        # insert a new value into this tree
        left_height = -1
        right_height = -1

        if val < self.val:
            # left insert
            if self.left:
                left_height = self.left.insert(val)
            else:
                self.left = AvlTreeNode(val)
                left_height = 1
                
            right_height = 0 if self.right is None \
                             else self.right.__get_height()
        else:
            # right insert
            if self.right:
                right_height = self.right.insert(val)
            else:
                self.right = AvlTreeNode(val)
                right_height = 1

            left_height = 0 if self.left is None else self.left.__get_height()

        self.__balance(left_height - right_height)

        return self.__get_height()

    def insert_list(self, val_list):
        # insert a list of values into this tree
        for val in val_list:
            self.insert(val)
    
    def delete(self, val):
        # delete a node from this tree
        if self.val == val:
            if self.left is None and self.right is None:
                # handle the case where this is the root node or a leaf node
                self.val = None

            elif self.left and self.right is None:
                # replace the current node with its left child
                self.val = self.left.val
                self.right = self.left.right
                self.left = self.left.left

                # calculate the balance factor and balance the tree at this node
                self.__balance(self.left.__get_height())

            elif self.left is None and self.right:
                # replace the current node with its right child
                self.val = self.right.val
                self.left = self.right.left
                self.right = self.right.right

                # calculate the balance factor and balance the tree at this node
                self.__balance(-1 * self.right.__get_height())

            elif self.left and self.right:
                # traverse to the left-most node of the right subtree and
                # replace the current node's value with that value
                temp_node_stack = []
                temp_node = self.right
                leftmost_node_val = -1

                while temp_node.left:
                    temp_node_stack.append(temp_node)

                    if temp_node.left.left is None:
                        # found the left-most node of the right subtree
                        leftmost_node_val = temp_node.left.val

                        if temp_node.left.right:
                            # move the right node of the left-most node of the
                            # right subtree up one level
                            temp_node.left = temp_node.left.right
                        else:
                            temp_node.left = None

                        break

                    temp_node = temp_node.left

                if len(temp_node_stack) == 0:
                    # if there were no left nodes to traverse to, the first
                    # right node is selected as the replacement
                    leftmost_node_val = temp_node.val
                    self.right = self.right.right

                self.val = leftmost_node_val

                # balance the tree recursively upwards to the current node
                for x in range(0, len(temp_node_stack)):
                    temp_node_stack.pop().__balance()

                self.__balance()

            return True

        if val < self.val and self.left:
            deletion_result = self.left.delete(val)

            if deletion_result:
                if self.left.val == None:
                    # if the left child node of this node was deleted, and
                    # it was a leaf node, then remove the node itself here
                    self.left = None

                # if a node in this node's subtree was deleted,
                # the tree needs to be balanced recursively upwards
                # to the root node
                self.__balance()

            return deletion_result
        elif val > self.val and self.right:
            deletion_result = self.right.delete(val)

            if deletion_result:
                if self.right.val == None:
                    # if the right child node of this node was deleted, and
                    # it was a leaf node, then remove the node itself here
                    self.right = None

                # if a node in this node's subtree was deleted,
                # the tree needs to be balanced recursively upwards
                # to the root node
                self.__balance()

            return deletion_result
        else:
            return False

    def search(self, val):
        # find whether the value exists in this tree,
        # using a depth-first search
        if self.val == val:
            return True
        elif val < self.val and self.left:
            return self.left.search(val)
        elif val > self.val and self.right:
            return self.right.search(val)
        else:
            return False
    
    def print(self, end='\n', level=None, padding=None):
        # print the tree to the console using breadth-first search
        if level is None:
            # if this is the root node, calculate the padding
            # from the subtree height
            height = self.__get_height()
            padding = ((2**height) // 2) * 8

            print(str(self.val).center(padding), end=end)

            for current_level in range(0, height - 1):
                padding //= 2

                if self.left:
                    self.left.print('', current_level, padding)
                else:
                    print(''.center(padding), end='')

                if self.right:
                    self.right.print(end, current_level, padding)
                else:
                    print(''.center(padding), end=end)

        elif level == 0:
            # if we're at the bottom node of the current breadth-first search,
            # print it
            print(str(self.val).center(padding), end=end)

        else:
            # if we're not yet at the bottom node of the current breadth-first
            # search, print the child nodes if they exist
            if self.left and self.right:
                self.left.print('', level - 1, padding)
                self.right.print(end, level - 1, padding)
            elif self.left and self.right is None:
                self.left.print('', level - 1, padding)
                print(''.center(padding), end=end)
            elif self.left is None and self.right:
                print(''.center(padding), end='')
                self.right.print(end, level - 1, padding)
            else:
                print(''.center(padding), end='')
                print(''.center(padding), end=end)

    def __get_balance_factor(self):
        # get the balance factor of the current node by subtracting the height
        # of its right subtree from the height of its left subtree
        left_height = 0 if self.left is None else self.left.__get_height()
        right_height = 0 if self.right is None else self.right.__get_height()

        return (left_height - right_height)

    def __balance(self, balance_factor=None):
        # balance the binary tree by looking at
        # the balance_factor of the updated node
        if balance_factor is None:
            balance_factor = self.__get_balance_factor()

        if balance_factor > 1:
            # tree is left-heavy
            left_node_balance_factor = self.left.__get_balance_factor()

            if left_node_balance_factor > 0:
                # subtree is also left-heavy, perform a right rotation
                self.__right_rotation()
            elif left_node_balance_factor < 0:
                # subtree is right-heavy, perform a left-right rotation
                self.left.__left_rotation()
                self.__right_rotation()

        elif balance_factor < -1:
            # tree is right-heavy
            right_node_balance_factor = self.right.__get_balance_factor()

            if right_node_balance_factor < 0:
                # subtree is also right-heavy, perform a left rotation
                self.__left_rotation()
            elif right_node_balance_factor > 0:
                # subtree is left-heavy, perform a right-left rotation
                self.right.__right_rotation()
                self.__left_rotation()

    def __right_rotation(self):
        # perform a right rotation

        # store the current node's value & move up the left side
        temp_self_val = self.val
        temp_right_node = self.left.right
        self.val = self.left.val
        self.left = self.left.left
        
        # create a new right node with the stored node's value,
        # and set its right to the original node's right
        new_right_node = AvlTreeNode(temp_self_val)
        new_right_node.right = self.right
        self.right = new_right_node
        self.right.left = temp_right_node

    def __left_rotation(self):
        # perform a left rotation

        # store the current node's value & move up the right side
        temp_self_val = self.val
        temp_left_node = self.right.left
        self.val = self.right.val
        self.right = self.right.right

        # create a new left node with the stored node's value,
        # and set its left to the original node's left
        new_left_node = AvlTreeNode(temp_self_val)
        new_left_node.left = self.left
        self.left = new_left_node
        self.left.right = temp_left_node

    def __get_height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left and self.right is None:
            return 1 + self.left.__get_height()
        elif self.left is None and self.right:
            return 1 + self.right.__get_height()
        else:
            left_height = self.left.__get_height()
            right_height = self.right.__get_height()

            return (1 + left_height) if left_height > right_height \
                   else (1 + right_height)

def main():
    # Test example here, https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
    int_avl_tree = AvlTreeNode(109)
    int_avl_tree.insert_list([110, 111, 108, 107, 113, 112, 104, 105, 97])

    print("int tree:\n")

    int_avl_tree.print()

    print(f"\nint tree contains 111: {int_avl_tree.search(111)}")
    print(f"int tree contains 42: {int_avl_tree.search(42)}\n")

    int_avl_tree.delete(112)
    int_avl_tree.insert(96)
    int_avl_tree.insert(106)
    int_avl_tree.delete(109)

    print(f"int tree after deleting 112, inserting 96 & 106, and deleting 109:\n")

    int_avl_tree.print()

    # Wikipedia example, https://en.wikipedia.org/wiki/AVL_tree#/media/File:AVL_Tree_Example.gif
    letter_avl_tree = AvlTreeNode('M')
    letter_avl_tree.insert_list(['N', 'O', 'L', 'K', 'Q', 'P', 'H', 'I', 'A'])

    print("\nletter tree:\n")

    letter_avl_tree.print()

    print(f"\nletter tree contains 'M': {letter_avl_tree.search('M')}")
    print(f"letter tree contains 'X': {letter_avl_tree.search('X')}")

if __name__ == "__main__":
    main()