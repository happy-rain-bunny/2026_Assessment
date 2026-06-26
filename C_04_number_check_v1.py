# Functions go here
def num_check(question, exit_code=None):
    """Checks users enter an integer more than zero"""

    error = "Please enter an integer more than zero.\n"

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            response = int(response)
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes...
while True:
    print()

    number = num_check("Please enter a number more than 0: ")
    print(f"Thanks. You chose {number}")



