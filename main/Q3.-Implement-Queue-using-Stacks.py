1class MyQueue:
2
3    def __init__(self):
4        self.input_stack  = []
5        self.output_stack = []
6
7    def push(self, x: int) -> None:
8        self.input_stack.append(x)
9    def transfer_is_need(self):
10        if not self.output_stack:
11            while self.input_stack:
12                self.output_stack.append(self.input_stack.pop())
13
14    def pop(self) -> int:
15        self.transfer_is_need()
16        return self.output_stack.pop()
17
18    def peek(self) -> int:
19        self.transfer_is_need()
20        return self.output_stack[-1]
21
22    def empty(self) -> bool:
23        return len(self.input_stack) == 0 and len(self.output_stack) == 0
24
25
26# Your MyQueue object will be instantiated and called as such:
27# obj = MyQueue()
28# obj.push(x)
29# param_2 = obj.pop()
30# param_3 = obj.peek()
31# param_4 = obj.empty()