from movie import Movie
from user import User

user = User("Joe")

my_movie = Movie("The Matrix", "Sci-Fi", "Wachowski")

user.movies.append(my_movie)

print(user)
print(user.movies)