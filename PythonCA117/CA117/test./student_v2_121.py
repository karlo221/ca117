class Student:
    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.iteam = {}

    def add_grade(self, grade, mark):
        self.iteam[grade] = mark

    def get_grade(self, find):
        if find in self.iteam.values():
            return self.iteam[find]
        else:
            return ('N/A')
