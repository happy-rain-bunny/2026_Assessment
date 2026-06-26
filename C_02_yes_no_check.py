# functions go here...
def yes_no_check(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower().strip

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).")

# Main routine goes here

# Loop for testing purposes
while True:
    want_instructions = yes_no_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")


