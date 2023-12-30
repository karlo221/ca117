class Student:
    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.stack = []

    def __str__(self):
        return (f'Name: {self.name}\nCAO: {self.cao}\nPoints: {sum(self.stack)}')

    def push(self, e):
        self.stack.append(e)

    def add_grade(self, sub, grade):
        sub = sub
        self.grade = grade
        dict = {
            'H1': 100, 'H2': 88, 'H3': 77, '04': 28
        }
        if grade in dict.keys():
            self.push(dict[grade])
        if len(self.stack) > 3:
            self.stack.sort(reverse=True)
            self.stack[0] = dict[grade]
        else:
            pass
def main():
    
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)

    s1.add_grade('english', 'H2')
    s1.add_grade('irish', 'O4')
    s1.add_grade('french', 'H3')
    s1.add_grade('physics', 'H3')
    print(s1)

    print(s2)

if __name__ == '__main__':
    main()
