class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def create_cycle(self, pos):
        """Create a cycle by connecting tail to node at position pos"""
        if pos < 0 or pos >= self.size:
            return

        tail = self.head
        cycle_node = self.head

        # Find tail node
        while tail.next:
            tail = tail.next

        # Find node at position pos
        for i in range(pos):
            cycle_node = cycle_node.next

        # Create cycle
        tail.next = cycle_node

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val


def linked_list_with_cycle(ll):
    slow = ll.head
    fast = ll.head
    disct_list = {}
    while fast and fast.next:
        if slow in disct_list:
            print(f"Cycle detected at node with value: {slow.val}")
            return True
        else:
            disct_list[slow.val] = slow
            slow = slow.next
            fast = fast.next.next

    print("No cycle detected")


# Create linked list: 3 -> 2 -> 0 -> -4 -> (back to node at index 1)
ll = LinkedList()
ll.append(3)
ll.append(2)
ll.append(0)
ll.append(-4)
ll.create_cycle(1)  # pos = 1, cycle back to node with value 2
print(linked_list_with_cycle(ll))  # Output: Cycle detected at node with value: 2
