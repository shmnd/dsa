from collections import deque

class MyQueue:

    def __init__(self):
        self.main_q = deque()
        

    def push(self, x: int) -> None:
        return self.main_q.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        return self.main_q.popleft()
        

    def peek(self) -> int:
        if self.empty():
            return None
        else:
            return self.main_q[0]
        

    def empty(self) -> bool:
        return len(self.main_q) == 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(7)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()