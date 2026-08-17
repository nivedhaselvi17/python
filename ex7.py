class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)


# Main program
bst = BinarySearchTree()
root = None

n = int(input("Enter number of books: "))

for i in range(n):
    title = input("Enter book title: ")
    root = bst.insert(root, title)

print("\nBooks in Inorder Traversal:")
bst.inorder(root)

