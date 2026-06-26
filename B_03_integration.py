import pandas
from tabulate import tabulate
from datetime import date
import math


def make_statement(statement, decoration):
    """Put headings of the project to let users know
     what project it is and emphasise it by adding
     decoration at the start and end

     Emphasises headings by adding decoration at te start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"


def yes_no_check(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).")


def instructions():
    """explain how the program will works"""

    print(make_statement(statement="Instructions", decoration="ℹ️"))
    print("""This is a Shape Calculator finding out the area and perimeter of shapes. 

Shapes only include: triangle, circle, rectangle, and square. 

The program automatically calculates the area and perimeter of
shapes that you entered with their dimensions. 

* Note: If all three sides of the triangle are unknown, 
the perimeter cannot be calculated and will be maked as
'N/A' (Not Applicable).

Please make sure to enter all measurements in centimeters (cm).

Once you have entered all of your shapes,
the program displays the data in a table format
and save it to a text file with today's date.

Enter 'xxx' when you want to finish it.

:)
    """)


def string_check(question, valid_answers=('triangle', 'circle', 'rectangle', 'square', 'xxx'),
                 num_letters=1):
    """Checks that users enter the valid answers including exit code
    reject wrong shapes such as sphere
    reject any other wrong answers"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word in valid answers
            if response == item:
                return item

            # skip first letter check of exit code so only accept 'xxx'
            elif item == 'xxx':
                continue

            # check if the response is first letter of valid answers
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def num_check(question, exit_code=None):
    """Checks users enter any number (integer/float) more than zero."""
    error = "Please enter a number more than zero.\n"
    while True:
        response = input(question).lower().strip()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            response = float(response)
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def round_component(x):
    """round number having more than 2 decimal places (#.##)"""

    # for triangle that cannot calculate perimeter
    if x is None:
        return "N/A"

    # remove decimals places for integer (doesn't need)
    if x == int(x):
        return str(int(x))

    # don't put * for number having dp less than 3
    if round(x, 2) == x:
        return str(x)

    # rounding to the 2 decimal place and *
    else:
        return "{:.2f}*".format(x)



# Main Routine goes here

# displays name of the program
print(make_statement("Shape Calculator", "="))

# checks if the users want to see the instruction or not
want_instructions = yes_no_check("Do you want to see the instructions? ")
print()

# display instruction if users choose 'yes'
if want_instructions == "yes":
    instructions()


# Get shape details

while True:
    shape = string_check(question="\nWhich of the following shapes is this: triangle, circle, rectangle, or square? ")

    if shape == "xxx":
        break

    elif shape == "triangle":
        triangle_all_sides = yes_no_check("\nDo you know all three sides of the triangle? ")

        if triangle_all_sides == "yes":
            side_1 = num_check("First side: ")
            side_2 = num_check("Second side: ")
            side_3 = num_check("Last side: ")

            # check whether the triangle is true (exist) or not
            if (side_1 + side_2 <= side_3) or (side_1 + side_3 <= side_2) or (side_2 + side_3 <= side_1):
                print("\nSorry, these sides cannot form a triangle.\n"
                      "Please enter valid value that the sum of two sides is bigger than the longest side.")
                continue

            perimeter = round_component(side_1 + side_2 + side_3)
            semi = (side_1 + side_2 + side_3) / 2
            area = round_component(math.sqrt((semi) * (semi - side_1) * (semi - side_2) * (semi - side_3)))

            print(f"{shape} has perimeter of {perimeter} cm and area of {area} cm\u00B2.")


        elif triangle_all_sides == "no":
            triangle_base_height = yes_no_check("Do you know base and height of the triangle? ")

            if triangle_base_height == "yes":
                base = num_check("Base: ")
                height = num_check("Height: ")

                perimeter = round_component(None)
                area = round_component((base * height)/2)

                print(f"{shape} has perimeter of {perimeter} and area of {area} cm\u00B2.")

            elif triangle_base_height == "no":
                print("Sorry. Since there is not enough information, I can't calculate.")


    elif shape == "circle":
        radius = num_check("Radius of circle: ")

        perimeter = round_component(radius * 2 * math.pi)
        area = round_component(radius * radius * math.pi)

        print(f"Circle has perimeter of {perimeter} cm and area of {area} cm\u00B2.")


    elif shape == "rectangle":
        base = num_check("Base: ")
        height = num_check("Height: ")

        perimeter = round_component(2 * (base + height))
        area = round_component(base * height)

        print(f"{shape} has perimeter of {perimeter} cm and area of {area} cm\u00B2.")


    elif shape == "square":
        side = num_check("Side: ")

        perimeter = round_component(4 * side)
        area = round_component(side * side)

        print(f"{shape} has perimeter of {perimeter} cm and area of {area} cm\u00B2.")


    else:
        print("please choose from triangle, circle, rectangle, or square. \n")
        continue


