#lets do a small program to see if a person can guess the magic number. They have 3 chances. 
magic_numbers = [3, 9]
chances = 3
for i in range(chances):
    print("This is attempt {}".format(i))
    user_number = int(input("Enter a number between 1 and 10: "))
    if user_number in magic_numbers:
        print("You guessed the magic number! Congratulations!!!")
        #I was trying to just use a simple 'else' statement here, and it worked at first, but after 
        #mark 4 it kept giving me an error, so I went with the ugly 'not in' statement
        #I'm sure it works, I just don't like the way it looks. Giving me a minor 'No!' in the back of my head.
    if user_number not in magic_numbers:
        print("You didn't guess the magic number. That's a bummer. Try it again.")