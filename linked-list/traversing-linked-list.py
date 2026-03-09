class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def traverseLinkedList(head):
    currentElement = head
    while currentElement != None:
        print("Current element: ", currentElement.data)
        currentElement = currentElement.next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

traverseLinkedList(node1)