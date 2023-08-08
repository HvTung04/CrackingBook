class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(arr):
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()

def addNode(head, val):
    add = Node(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = add
    return head

def deleteNode(head, val):
    if val == head.data:
        return head.next
    prev, curr = head, head.next
    while curr.data != val:
        prev = curr
        curr = curr.next
    prev.next = curr.next
    curr.next = None
    return head
    


def main():
    arr = [1, 2, 3, 4, 5]
    head = createLinkedList(arr)
    printLinkedList(head)
    head = addNode(head, 99)
    printLinkedList(head)
    head = deleteNode(head, 1)
    printLinkedList(head)
    head = deleteNode(head, 5)
    printLinkedList(head)

if __name__ == '__main__':
    main()