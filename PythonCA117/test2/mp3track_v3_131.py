class MP3Track:
    def __init__(self, title, duration, artists=None):
        self.title = title
        self.duration = duration
        if artists is None:
            artists = []
        self.artists = artists

    def __str__(self):
        return (f'Title: {self.title}\nBy: {", ".join(self.artists)}\nDuration: {self.duration}')

    def add_artist(self, add):
        self.artists.append(add)
