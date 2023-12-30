class Triathlete:
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.race = {}

    def __str__(self):
        return (f'Name: {self.name}\nID: {self.tid}\nRace time: {sum(self.race.values())}')

    def add_time(self, sport, time):
        self.race[sport] = time

    def get_time(self, dis):
        return self.race[dis]
