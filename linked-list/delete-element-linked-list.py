class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"


def deleteElement(head, deleteNode):
    if head == deleteNode:
        return head.next
    
    currentNode = head
    print("Current Node:", currentNode)
    print(deleteNode)

    while currentNode.next and currentNode.next != deleteNode:
        currentNode = currentNode.next
    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next

    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

node4.next = node5

# Delete node4
node1 = deleteElement(node1, node4)



    
