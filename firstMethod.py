import random
#Doing our first method in Python. Working with the numInputRando.py program

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 1 and 10: "))
    if user_number in magic_numbers:
        print("You guessed the magic number! Congratulations!!!")
    if user_number not in magic_numbers:
        print("You didn't guess the magic number. That's a bummer. Try it again.")

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
# We want the parameter of the method to take this over. So no more (chances = 3) variable

def run_program_x_times(chances):
    #We want the user to determine how many chances they get. 
    for i in range(chances):
        print("This is attempt {}".format(i))
        ask_user_and_check_number()

user_chances = int(input("Enter a number for how many chances you'd like: "))
run_program_x_times(user_chances)
