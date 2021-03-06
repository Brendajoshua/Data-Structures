import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        new_node = BinarySearchTree(value)
        while True:
            # compare value to root node
            # if value is lesser, move left
            if value < node.value:
                # if there's no child in that direction, insert the value
                if node.left is None:
                    node.left = new_node
                    break
                node = node.left
            # if value is greater or equal, move right
            else:
                if node.right is None:
                    node.right = new_node
                    break
                node = node.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # recursive solution
        def search_tree(node, target):
            if node is None:
                return False
            elif target == node.value:
                return True
            elif target < node.value:
                return search_tree(node.left, target)
            else:
                return search_tree(node.right, target)

        return search_tree(self, target)

        # iterative solution
        # node = self
        # while True:
        #     # if values match, return true
        #     if target == node.value:
        #         return True
        #     # if target is less, move left
        #     elif target < node.value:
        #         # if no left child, tree does not contain target
        #         if node.left is None:
        #             return False
        #         node = node.left
        #     # if target is greater or equal, move right
        #     else:
        #         # if no right child, tree does not contain target
        #         if node.right is None:
        #             return False
        #         node = node.right


    # Return the maximum value found in the tree
    def get_max(self):
        node = self
        # move right until reach the rightmost (max) node
        while node.right is not None:
            node = node.right
        return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def traverse_tree(node, cb):
            if node is None:
                return
            else:
                cb(node.value)
                traverse_tree(node.left, cb)
                traverse_tree(node.right, cb)
        traverse_tree(self, cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go as far left as possible
        # print left node
        # print root node
        # if right node has children
            # go as far left as possible
            # print left node
            # print root node
            # etc....
        # if right node doesn't have children 
            # move back to the parent of the root node
        # same idea as for_each recursive solution
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)
    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make a queue and temp var
        q = Queue()
        tmp = node
        q.enqueue(tmp)
        # while the queue is not empty
        while q.len() > 0:
            # save root in temp var, dequeue
            tmp = q.dequeue()
            # print value
            print(tmp.value)
            # check left and right
            # if item exists, add to queue
            if tmp.left:
                q.enqueue(tmp.left)
            if tmp.right:
                q.enqueue(tmp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make a stack and a temp var
        stk = Stack()
        tmp = node
        stk.push(tmp)
        # while the stack is not empty
        while stk.len() > 0:
            # save root in temp var, then pop off stack
            tmp = stk.pop()
            # print value
            print(tmp.value)
            # check left and right
            # if item exists, add to stack
            if tmp.left:
                stk.push(tmp.left)
            if tmp.right:
                stk.push(tmp.right)
                

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        if self.right:
            self.right.post_order_dft(self.right)
        print(self.value)
