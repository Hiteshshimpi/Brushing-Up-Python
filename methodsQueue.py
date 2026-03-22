from collections import deque
from queue import Queue

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q[0])  # Output: 1
print(len(q))
q.popleft()
print(len(q))

queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())  # Output: 1
