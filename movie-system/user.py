from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User: {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)
        
    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        movies_watched = list(filter(lambda movie: movie.watched, self.movies)) # x = movie
        return movies_watched

# to open files and close them when you're done use the following method:
# with open('my_file.txt', 'w') as f:
#   f.write("Hello World")
#       or
#   print(f.readline())