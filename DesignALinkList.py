class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(self.size, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        self.size += 1
        for i in range(index):
            curr = curr.next

        newNode = ListNode(val)
        newNode.next = curr.next
        curr.next = newNode

    def deletAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for i in range(index):
            curr = curr.next
        size = -1
        curr.next = curr.next.next


myList = LinkList()
myList.addAtHead(1)
