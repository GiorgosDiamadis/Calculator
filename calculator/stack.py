class Stack():

    def __init__(self):
        self.array = []
        self.top = -1

    def push(self, data):

        self.array.insert(0, data)

        if self.top == -1:
            self.top = 0

    def pop(self):

        if self.top != -1:

            value = self.array[self.top]
            self.array.pop(0)

            if len(self.array) == 0:
                self.top = -1

            return value

        return None

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.top]

    def is_empty(self):
        return self.top == -1
