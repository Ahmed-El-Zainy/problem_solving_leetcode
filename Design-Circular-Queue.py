1class MyCircularQueue:
2
3    def __init__(self, k: int):
4        self.queue = [0] * k
5        self.k = k
6        self.front = 0
7        self.rear = 0
8        self.size = 0
9
10    def enQueue(self, value: int) -> bool:
11        if self.isFull():
12            return False
13        self.queue[self.rear] = value
14        self.rear = (self.rear + 1) % self.k
15        self.size += 1
16        return True
17
18    def deQueue(self) -> bool:
19        if self.isEmpty():
20            return False
21        self.front = (self.front + 1) % self.k
22        self.size -= 1
23        return True
24
25    def Front(self) -> int:
26        if self.isEmpty():
27            return -1
28        return self.queue[self.front]
29
30    def Rear(self) -> int:
31        if self.isEmpty():
32            return -1
33        return self.queue[(self.rear - 1 + self.k) % self.k]
34
35    def isEmpty(self) -> bool:
36        return self.size == 0
37
38    def isFull(self) -> bool:
39        return self.size == self.k
40
41# Your MyCircularQueue object will be instantiated and called as such:
42# obj = MyCircularQueue(k)
43# param_1 = obj.enQueue(value)
44# param_2 = obj.deQueue()
45# param_3 = obj.Front()
46# param_4 = obj.Rear()
47# param_5 = obj.isEmpty()
48# param_6 = obj.isFull()