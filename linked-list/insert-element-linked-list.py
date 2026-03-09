class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"

def insertElement(head, newElement, position):
    if position == 1:
        newElement.next = head
        return newElement
    
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    
    newElement.next = currentNode.next
    currentNode.next = newElement
    return head


node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertElement(node1, newNode, 3)
