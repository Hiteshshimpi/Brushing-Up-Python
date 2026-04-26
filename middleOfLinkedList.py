class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Build linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
cur = head
for val in [2, 3, 4, 5]:
    cur.next = Node(val)
    cur = cur.next

# Fast/slow pointer to find middle
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print(slow.val)  # Output: 3
