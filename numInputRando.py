import random
#Doing random numbers in Python now. This will have you guess a secret number that's randomly
#generated. Good times.

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
chances = 3
for i in range(chances):
    print("This is attempt {}".format(i))
    user_number = int(input("Enter a number between 1 and 10: "))
    if user_number in magic_numbers:
        print("You guessed the magic number! Congratulations!!!")
    if user_number not in magic_numbers:
        print("You didn't guess the magic number. That's a bummer. Try it again.")