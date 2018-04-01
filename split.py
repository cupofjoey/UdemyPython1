#Working on the String split() method
numbers = input("Enter your numbers, separated by commas: ")
numbers.split(",")
numbers_as_int = []
for number in numbers:
    numbers_as_int.append(int(number))

#Another way to do this

[int(number) for number in numbers] #this will convert each variable in that list into an int