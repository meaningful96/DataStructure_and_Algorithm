class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 가장 뒤에 노드 삽입
    def append(self, data):
        # 헤드(head)가 비어있는 경우
        if self.head == None:
            self.head = Node(data)
            return
        # 마지막 위치에 새로운 노드 추가
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드를 하나씩 출력
    def show(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next

    # 특정 인덱스(index)의 노드 찾기
    def search(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    # 특정 인덱스(index)에 노드 삽입
    def insert(self, index, data):
        new = Node(data)
        # 첫 위치에 추가하는 경우
        if index == 0:
            new.next = self.head
            self.head = new
            return
        # 삽입할 위치의 앞 노드
        node = self.search(index - 1)
        next = node.next
        node.next = new
        new.next = next

    # 특정 인덱스(index)의 노드 삭제
    def remove(self, index):
        # 첫 위치를 삭제하는 경우
        if index == 0:
            self.head = self.head.next
            return
        # 삭제할 위치의 앞 노드
        front = self.search(index - 1)
        front.next = front.next.next


linked_list = LinkedList()
data_list = [3, 5, 9, 8, 5, 6, 1, 7]

for data in data_list:
    linked_list.append(data)

print("전체 노드 출력:", end=" ")
linked_list.show()

linked_list.insert(4, 4)
print("\n전체 노드 출력:", end=" ")
linked_list.show()

linked_list.remove(7)
print("\n전체 노드 출력:", end=" ")
linked_list.show()

linked_list.insert(7, 2)
print("\n전체 노드 출력:", end=" ")
linked_list.show()

