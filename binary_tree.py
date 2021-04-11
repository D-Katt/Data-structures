"""Example of binary tree class and various methods of tree traversal."""

from collections import deque


class Tree:
    """Binary tree where left_subtree value ≤ node value < right_subtree value."""

    def __init__(self, value=None, left=None, right=None):
        """Tree could be initialized as empty or with some initial values.
        """
        self.value = value
        self.left = left
        self.right = right

    def insert(self, data):
        """Inserts a new value into the tree.
        """
        # Compare the new value with the parent node
        if self.value:
            if data <= self.value:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:  # If tree is empty
            self.value = data

    def find(self, value):
        """Checks if value is in a tree. Returns True or False.
        """
        # If the tree is empty
        if self.value is None:
            return False
        # If the tree has values in nodes
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            return self.left.find(value)
        else:
            if self.right is None:
                return False
            return self.right.find(value)

    def print_tree(self):
        """Prints all node values recursively (in ascending order).
        """
        if self.left:
            self.left.print_tree()
        print(self.value),
        if self.right:
            self.right.print_tree()

    def inorder(self, root):
        """Inorder traversal of binary tree: visit left subtree,
        then root node, then right subtree.
        """
        result = []
        if root:
            result = self.inorder(root.left)
            result.append(root.value)
            result = result + self.inorder(root.right)
        return result

    def preorder(self, root):
        """Preorder traversal of binary tree: visit root node,
        then left subtree, then right subtree.
        """
        result = []
        if root:
            result.append(root.value)
            result = result + self.preorder(root.left)
            result = result + self.preorder(root.right)
        return result

    def postorder(self, root):
        """Postorder traversal of binary tree: visit left subtree,
        then right subtree, then root node.
        """
        result = []
        if root:
            result = self.postorder(root.left)
            result = result + self.postorder(root.right)
            result.append(root.value)
        return result

    def levelorder(self):
        """Level order traversal of binary tree, i.e. going from left to right
        level by level from top (root) to bottom.
        """
        # If we don't have a root node
        if not self.value:
            return []

        # If we have a root
        result = [[self.value]]  # 1st level (root node)
        queue = deque()
        if self.left is not None:  # 2nd level
            queue.append(self.left)
        if self.right is not None:
            queue.append(self.right)

        while queue:
            # On each iteration initialize a new list for the next level
            arr = []
            # Get all nodes of the previous level one by one from left to right
            for i in range(len(queue)):
                node = queue.popleft()
                arr.append(node.value)
                # Get child nodes of the current node
                left = node.left
                right = node.right
                # If they are not None, add them to queue
                if left is not None:
                    queue.append(left)
                if right is not None:
                    queue.append(right)
            # Add all nodes from the current level to result
            result.append(arr)
        return result

    def zigzag(self):
        """Zigzag level order traversal of binary tree values
        (i.e., from left to right, then right to left and so on).
        """
        # Get regular level order traversal
        level_order = self.levelorder()
        zigzag_order = []
        # Reverse the numbers in every sublist with odd index
        for i in range(len(level_order)):
            if i % 2 == 0:
                zigzag_order.append(level_order[i])
            else:
                zigzag_order.append(level_order[i][::-1])
        return zigzag_order

    def invert(self, root):
        """Inverts a binary tree, i.e. replaces left and right subtrees
        for every node in a tree.
        """
        # If the tree is empty
        if root is None:
            return []
        # It the tree contains values
        root.left, root.right = root.right, root.left
        if root.left is not None:
            root.left = self.invert(root.left)
        if root.right is not None:
            root.right = self.invert(root.right)
        return root


# Create a binary tree
tree = Tree()

# Insert all values from the list into the tree
values = [3, 9, 20, 15, 7, 50, 4, 25, 6, 60, 1, 12, 35, 0]
for element in values:
    tree.insert(element)

# Print all values recursively in an ascending order
tree.print_tree()

# Check if a value is in the tree
print(tree.find(11))

# Traverse the tree visiting nodes in different order
print(tree.inorder(tree))
print(tree.preorder(tree))
print(tree.postorder(tree))

# Two ways of level order traversal
print(tree.levelorder())
print(tree.zigzag())

# Invert the tree and show level order traversal
inv_tree = tree.invert(tree)
print(inv_tree.levelorder())
