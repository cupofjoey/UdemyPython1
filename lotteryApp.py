import random

def menu():
    #Ask player for numbers
    user_numbers = get_player_numbers
    # Calculate lottery Numbers
    lottery_numbers = create_lottery_numbers
    #Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You won ${}!".format(100 ** len(matched_numbers)))

# User can pick 6 numbers
def get_player_numbers():
    number_csv = input("Enter your 6 numbers, spearated by commas: ")
    # Create a set of integers from this number_csv
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

# Lottery calculates 6 random numbers (b/t 1 & 20)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values
# Then we match the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matched

print(create_lottery_numbers())
