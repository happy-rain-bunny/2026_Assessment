def string_check(question, valid_answers=('triangle', 'circle', 'rectangle', 'square', 'xxx')):
    """Checks that users enter the valid answers including exit code
    reject wrong shapes such as sphere
    reject any other wrong answers"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is in valid answers
            if response == item:
                return item

        print(f"Please choose an option from {valid_answers}")

# Main routine goes here

# Loop for testing purposes
while True:
    shape = string_check(question="\nWhich of the following shapes is this: triangle, circle, rectangle, or square? ")
    if True:
        print(f"You chose {shape}.")
    if False:
        print("Please enter valid answers.")

