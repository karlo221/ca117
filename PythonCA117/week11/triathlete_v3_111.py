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

    def __eq__(self, num):
        return(sum(self.race.values())) == (sum(num.race.values()))

    def __gt__(self, num):
        return(sum(self.race.values())) > (sum(num.race.values()))

    def __lt__(self, num):
        return(sum(self.race.values())) < (sum(num.race.values()))
