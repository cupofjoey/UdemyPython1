from user import User

user = User.load_from_file('Joe.txt')

print(user.name)
print(user.movies)