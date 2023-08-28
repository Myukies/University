class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree():
    data = int(input("Enter data (or -1 for no node): "))
    if data == -1:
        return None
    node = TreeNode(data)
    print("Enter left subtree of", data)
    node.left = build_tree()
    print("Enter right subtree of", data)
    node.right = build_tree()
    return node

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

if __name__ == "__main__":
    print("Build your binary tree:")
    root = build_tree()

    print("Inorder Traversal:")
    inorder(root)
    print()

    print("Preorder Traversal:")
    preorder(root)
    print()

    print("Postorder Traversal:")
    postorder(root)
    print()
