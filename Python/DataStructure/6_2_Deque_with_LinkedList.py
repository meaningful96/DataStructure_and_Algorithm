class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def appendleft(self, data):
        node = Node(data)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1

    def append(self, data):
        node = Node(data)
        if self.rear == None:
            self.front = node
            self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self.size += 1

    def popleft(self):
        if self.size == 0:
            return None
        # 앞에서 노드 꺼내기
        data = self.front.data
        self.front = self.front.next
        # 삭제로 인해 노드가 하나도 없는 경우
        if self.front == None:
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
        return data

    def pop(self):
        if self.size == 0:
            return None
        # 뒤에서 노드 꺼내기
        data = self.rear.data
        self.rear = self.rear.prev
        # 삭제로 인해 노드가 하나도 없는 경우
        if self.rear == None:
            self.front = None
        else:
            self.rear.next = None
        self.size -= 1
        return data

    def front(self):
        if self.size == 0:
            return None
        return self.front.data

    def rear(self):
        if self.size == 0:
            return None
        return self.rear.data

    # 앞에서부터 원소 출력
    def show(self):
        cur = self.front
        while cur:
            print(cur.data, end=" ")
            cur = cur.next


d = Deque()
arr = [5, 6, 7, 8]
for x in arr:
    d.append(x)
arr = [4, 3, 2, 1]
for x in arr:
    d.appendleft(x)
d.show()

print()
while d.size != 0:
    print(d.popleft())

arr = [1, 2, 3, 4, 5, 6, 7, 8]
for x in arr:
    d.appendleft(x)
d.show()

print()
while True:
    print(d.pop())
    if d.size == 0:
        break
    print(d.popleft())
    if d.size == 0:
        break
