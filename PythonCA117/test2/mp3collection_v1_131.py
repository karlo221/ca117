class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        rl = []
        rl.append('Title: {}'.format(self.title))
        rl.append('Duration: {}'.format(self.duration))
        return '\n'.join(rl)

class MP3Collection(object):

    def __init__(self):
        self.d = {}

    def add(self, mp3):
        self.d[mp3.title] = mp3

    def remove(self, title):
        if title in self.d:
            del self.d[title]

    def lookup(self, title):
        try:
            return self.d[title]
        except KeyError:
            return None
