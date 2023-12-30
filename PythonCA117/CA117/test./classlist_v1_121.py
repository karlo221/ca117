class Student():
    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        return (f'Name: {self.name}\nCAO: {self.cao}')

class Classlist(object):
    def __init__(self):
        self.d = {}

    def add(self, s):
        self.d[s.cao] = s

    def remove(self, cao):
        del(self.d[cao])

    def lookup(self, cao):
        if cao in self.d:
            return self.d[cao]
        else:
            return None

def main():
    
    cl = Classlist()
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)

    cl.add(s1)
    cl.add(s2)

    s = cl.lookup(21345654)
    assert(isinstance(s, Student))
    assert(s.name == 'Boris Spassky')
    assert(s.cao == 21345654)

    cl.remove(21907321)
    s = cl.lookup(21345654)
    assert(s is None)

if __name__ == '__main__':
    main()
