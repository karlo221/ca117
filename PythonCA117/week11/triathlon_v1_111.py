class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return (f'Name: {self.name}\nID: {self.tid}')

class Triathlon(object):
    def __init__(self):
        self.fic = {}

    def add(self, t):
        self.fic[t.tid] = t

    def remove(self, t):
        if t in self.fic:
            del self.fic[t]

    def lookup(self, luk):
        try:
            return self.fic[luk]
        except KeyError:
            return None
