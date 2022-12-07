class Queue():
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.front_index == len(self.items):
            print('queue empty')
            return None
        else:
            returnvalue = self.items[self.front_index]
            self.front_index += 1
            return returnvalue
   
    def front(self):
        if self.front_index == len(self.items):
            print('queue is empty')
        else:
            returnvalue = self.items[self.front_index]
            return returnvalue
        
