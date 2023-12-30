class Point:
    def set_attributes(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_attributes(self):
        print(f'x: {self.x:.2f}')
        print(f'y: {self.y:.2f}')

    def reflect(self):
        self.x = -self.x
        self.y = -self.y
