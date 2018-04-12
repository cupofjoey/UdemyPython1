class Movie:
    def __init__(self, name, genre, director):
        self.name = name
        self.genre = genre
        self.director = director

    def __repr__(self):
        return "<Movie Name: {}>".format(self.name)