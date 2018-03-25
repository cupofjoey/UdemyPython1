age = input("Enter your age: ")
#need to remember to put in a control on what the user can input. Like only accept ints rather than strings.
print("You have lived for " + str(int(age) * 365 * 24 * 60 * 60) + ' seconds. Congratulations.')