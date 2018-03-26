# A brief look at for loops, if/else statements, and the 'in' keyword in Python
numbers = [0,1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number < 5:
        print("This number is less than 5")
    else:
        print("This number is greater than 5")

#Ok so let's look at the 'in' keyword

magic_numbers = [3, 9]
user_number = 4

for number in magic_numbers:
    if user_number == magic_numbers:
        print("This number is in this list")
    else:
        print("This number is not in this list")

#We can even simplify it even more:

user_number in magic_numbers

#this would return False, because, it's not in magic_numbers...duh