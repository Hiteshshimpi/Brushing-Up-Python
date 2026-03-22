class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.ptr = 0
        self.my_list = []
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.my_list.append(value)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.ptr >= self.size:
            return False
        self.ptr += 1
        self.size = self.size - 1
        return True

    def Front(self) -> int:
        if self.k < 0:
            return -1
        else:
            return self.ptr

    def Rear(self) -> int:
        if self.k < 0:
            return -1
        else:
            len_list = len(self.my_list)
            return self.my_list[len_list - 1]

    def isEmpty(self) -> bool:
        if self.size < self.k:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
