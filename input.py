age = input("Enter your age: ")
#need to remember to put in a control on what the user can input. Like only accept ints rather than strings.
#that's where the input method comes in
#print("You have lived for " + str(int(age) * 365 * 24 * 60 * 60) + " seconds. Congratulations.")
print('You have lived for {} seconds. Congratulations. This corresponds to {} years.'.format(int(age) * 365 * 24 * 60 * 60, age))