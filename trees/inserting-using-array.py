class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

def buildTree(arr):
    if not arr:
        return None

    nodes = [TreeNode(val) for val in arr]

    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(arr):
            nodes[i].left = nodes[left_index]

        if right_index < len(arr):
            nodes[i].right = nodes[right_index]

    return nodes[0]  # root

arr = ['3', '1', '2', '4', '5', '6', '7', '8']
root = buildTree(arr)
inOrderTraversal(root)