
class MyStack:

    def __init__(self):
        self.main_q = deque()

        
    def push(self, x: int) -> None:
        self.main_q.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None

        return self.main_q.pop()
        

    def top(self) -> int:
        if self.empty():
            return None

        top_ele = self.main_q[-1]
        return top_ele
        

    def empty(self) -> bool:
        return len(self.main_q) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
        

