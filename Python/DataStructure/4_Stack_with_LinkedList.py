class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # 원소 삽입
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # 원소 추출하기
    def pop(self):
        if self.is_empty():
            return None

        # 머리(head) 위치에서 노드 꺼내기
        data = self.head.data
        self.head = self.head.next

        return data

    # 최상위 원소(top)
    def top(self):
        if self.is_empty():
            return None
        return self.head.data

    # 먼저 추출할 원소부터 출력
    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

    # 스택이 비어있는지 확인
    def is_empty(self):
        return self.head is None

## 클래스를 실행해보기, for문을 이용한 generator를 이용해 실행
stack = Stack()
arr = [9, 7, 2, 5, 6, 4, 2]
for x in arr:
    stack.push(x)
stack.show()
print()

while not stack.is_empty():
    print(stack.pop())
