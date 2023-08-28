class deque():
    def __init__(self):
        self.items = []
        self.front_value = 0



    def push(self, value):
        self.items.append(value)

    def pushleft(self, value):
        self.items.insert(self.front_value,value)

    def pop():
        if len(self.items) == self.front_value:
            print('queue is empty')
            return None
        else:
            return self.items.pop()

    def popleft():
        if len(self.items) == self.front_value:
            print('queue is empty')
            return None
        else:
            x = self.items[self.front_value]
            self.front_value += 1
            return x
