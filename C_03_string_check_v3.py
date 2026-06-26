def string_check(question, valid_answers=('triangle', 'circle', 'rectangle', 'square')):
    """checks that users enter at least the start of a word from valid responses"""

    while True:

        response = input(question).lower().strip()

        for item in valid_answers:

            # check if the response matches the start of the valid item
            if item.startswith(response):
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

