class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        # 꼬리(tail) 위치에 새로운 노드 삽입
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequeue(self):
        if self.head == None:
            return None

        # 머리(head) 위치에서 노드 꺼내기
        data = self.head.data
        self.head = self.head.next

        return data

    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next


queue = Queue()
data_list = [3, 5, 9, 8, 5, 6, 1, 7]

for data in data_list:
    queue.enqueue(data)

print("\n전체 노드 출력:", end=" ")
queue.show()

print("\n[원소 삭제]")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

print("[원소 삽입]")
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(3)

print("전체 노드 출력:", end=" ")
queue.show()
