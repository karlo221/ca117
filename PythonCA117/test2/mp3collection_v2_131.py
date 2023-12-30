class MP3Track(object):

    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists

    def __str__(self):
        rl = []
        rl.append('Title: {}'.format(self.title))
        rl.append('By: {}'.format(', '.join(self.artists)))
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

    def get_mp3s_by_artist(self, artist):
        return [mp3 for mp3 in self.d.values() if artist in mp3.artists]
