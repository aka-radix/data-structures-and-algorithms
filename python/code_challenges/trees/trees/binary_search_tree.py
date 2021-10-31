from trees.node import Node
from trees.queue import Queue
from trees.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    A class representing a binary search tree. Extends BinaryTree.

    Args:
        BinaryTree (class): The base binary tree class.
    """

    def __init__(self, *args):
        """
        The constructor method of a binary search tree, initialize the nodes list, and the root node, as well as add any node to the tree if passed as an argument.
        """
        super().__init__()
        for itm in args:
            self.add(itm)

    def add(self, value):
        """
        Add a node to a binary tree. Follows breadth first traversal.

        Args:
            value (any): The value to be stored in a node that will get connected to the tree.
        """
        if not self.root:
            self.root = Node(value)
            return
        breadth = Queue()
        breadth.enqueue(self.root)
        while breadth.peek():
            if breadth.front.left and breadth.front.right:
                breadth.enqueue(breadth.front.left)
                breadth.enqueue(breadth.front.right)
                breadth.dequeue()
            elif not breadth.front.left:
                breadth.front.left = Node(value)
                return
            elif not breadth.front.right:
                breadth.front.right = Node(value)
                return

    def contains(self, value):
        """
        Check if there exists a node in the tree that has a value equals to the passed value.

        Args:
            value (any): The value to be checked for.

        Returns:
            bool: True if the tree has a node that has a value equals the passed value, False otherwise.
        """
        try:
            for item in self.post_order(self.root):
                if item == value:
                    return True
            return False
        except AttributeError:
            return False

    def __str__(self):
        """
        Construct and return a string representation of a tree.

        Returns:
            str: A string representation of a tree.
        """
        if not self.root:
            return 'Empty tree.'
        q = Queue()
        q.enqueue(self.root)
        representation = ""
        while not q.is_empty():
            front = q.dequeue()
            representation += f"[Value > {front.value} | Left > {front.left if front.left else '....None'} | Right > {front.right if front.right else '....None'}]\n"
            if front.left:
                q.enqueue(front.left)
            if front.right:
                q.enqueue(front.right)
        return representation
