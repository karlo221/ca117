class Stack:
    def __init__(self):
        self.s = []

    def push(self, e):
        self.s.append(e)

    def top(self):
        return self.s[-1]

    def pop(self):
        return self.s.pop()

    def is_empty(self):
        return len(self.s) == 0

    def __len__(self):
        return len(self.s)
