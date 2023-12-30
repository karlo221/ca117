class MP3Track:
    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists

    def __str__(self):
        return (f'Title: {self.title}\nBy: {", ".join(self.artists)}\nDuration: {self.duration}')
