# ML Project
"""
 Written by Youmin Ko 
 
 Live life as if there were no second chance
"""

class Stack:
    def __init__(self):  # init은 생성함수
        self.items = []  # 데이터 저장을 위한 리스트 준비
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop() # pop을 할 아이템이 없으면
        except IndexError:
            print("Stack is empty") # IndexError 발생
            
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
            
    
    def __len__(self): # len()로 호출하면 stack의 item 수 반환
        return len(self.items)
    
    

S = Stack()
S.push(1)      # 1 
S.push(10)     # 1, 10
S.push(-3)     # 1, 10, -3
S.push(4)      # 1, 10, -3, 4
print(S.items) # [1,10,-3,4]
S.pop()        # 1, 10, -3
S.pop()        # 1, 10

