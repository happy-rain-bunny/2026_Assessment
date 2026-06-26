# Functions go here
def round_component(x):
    """round number having more than 2 decimal places (#.##)"""

    # for triangle that cannot calculate perimeter
    if x is None:
        return "N/A"

    # remove decimals places for integer (doesn't need)
    if x == int(x):
        return str(int(x))

    # rounding to the 2 decimal place and *
    if round(x, 2) == x:
        return str(x)

    else:
        return "{:.2f}*".format(x)



# Main Routine goes here

# loop for testing purposes...
while True:
    user_input = input("What is your number? ")

    if user_input == "":
        user_input = None

    else:
        user_input = float(user_input)

    number = round_component(user_input)
    print(f"It can be rounded as {number}.\n")
