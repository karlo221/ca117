class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, e):
        self.q.insert(len(self.q), e)

    def first(self):
        return self.q[0]

    def is_empty(self):
        return len(self.q) == 0

    def __len__(self):
        return len(self.q)

    def dequeue(self):
        return self.q.pop(0)
