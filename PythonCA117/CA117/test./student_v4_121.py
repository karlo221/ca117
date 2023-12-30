class Student(object):
    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid
        self.d = {}

    def __str__(self):
        try:
            return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}\nAverage mark: {sum(self.d.values())/len(self.d):.2f}'
        except ZeroDivisionError:
            return f'Name: {self.name}\nAddress: {self.address}\nID: {self.sid}\nAverage mark: 0.00'

    def add_mark(self, module, mark):
        self.d[module] = mark

    def get_mark(self, module):
        if module in self.d.keys():
            return self.d[module]
        else:
            return "Not registered for module"

    def __eq__(self, num):
        return (f'{sum(self.d.values())/len(self.d):.2f}') == (f'{sum(num.d.values())/len(num.d):.2f}')

    def __gt__(self, num):
        return (f'{sum(self.d.values())/len(self.d):.2f}') > (f'{sum(num.d.values())/len(num.d):.2f}')

    def __lt__(self, num):
        return (f'{sum(self.d.values())/len(self.d):.2f}') < (f'{sum(num.d.values())/len(num.d):.2f}')
