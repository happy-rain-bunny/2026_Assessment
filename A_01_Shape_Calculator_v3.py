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


# gather the information that users enter for table and file
triangle_dimensions = []
triangle_perimeters = []
triangle_areas = []

circle_dimensions = []
circle_perimeters = []
circle_areas = []

rectangle_dimensions = []
rectangle_perimeters = []
rectangle_areas = []

square_dimensions = []
square_perimeters = []
square_areas = []


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


        # save dimensions (sides OR base & height)
        if triangle_all_sides == "yes":
            triangle_dimensions.append(f"s={side_1}, {side_2}, {side_3}")
        else:
            triangle_dimensions.append(f"b={base} h={height}")

        # save calculated value (perimeter & area)
        triangle_perimeters.append(perimeter)
        triangle_areas.append(area)


    elif shape == "circle":
        radius = num_check("Radius of circle: ")

        perimeter = round_component(radius * 2 * math.pi)
        area = round_component(radius * radius * math.pi)

        print(f"Circle has perimeter of {perimeter} cm and area of {area} cm\u00B2.")

        # save dimensions (radius), calculated value (perimeter & area)
        circle_dimensions.append(f"r={radius}")
        circle_perimeters.append(perimeter)
        circle_areas.append(area)

    elif shape == "rectangle":
        base = num_check("Base: ")
        height = num_check("Height: ")

        perimeter = round_component(2 * (base + height))
        area = round_component(base * height)

        print(f"{shape} has perimeter of {perimeter} cm and area of {area} cm\u00B2.")

        # save dimensions (base & height), calculated value (perimeter & area)
        rectangle_dimensions.append(f"b={base} h={height}")
        rectangle_perimeters.append(perimeter)
        rectangle_areas.append(area)


    elif shape == "square":
        side = num_check("Side: ")

        perimeter = round_component(4 * side)
        area = round_component(side * side)

        print(f"{shape} has perimeter of {perimeter} cm and area of {area} cm\u00B2.")

        # save dimensions (side), calculated value (perimeter & area)
        square_dimensions.append(f"s={side}")
        square_perimeters.append(perimeter)
        square_areas.append(area)

    else:
        print("please choose from triangle, circle, rectangle, or square. \n")
        continue


# strings / output area

# **** Get current date for heading and filename ****

today = date.today()

# Get dya, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Headings / Strings...
main_heading_string = make_statement(statement= f"Shape Calculator "
                                    f"({day}/{month}/{year})", decoration="=")

# calculate how many shapes the user type
total_shapes = len(triangle_dimensions) + len(circle_dimensions) + len(rectangle_dimensions) + len(square_dimensions)
quantity_string = f"You entered {total_shapes} shapes in total."

# List of strings to be outputted / written to file
to_write = [main_heading_string, quantity_string]

# Tables...

# triangle
if len(triangle_dimensions) > 0: # If the user has not entered any shapes, it does not display!
    to_write.append("\n--- Triangle ---")
    shape_dict = {
        "No.": list(range(1, len(triangle_dimensions) + 1)), # it starts from 0 so +1
        "Dimensions": triangle_dimensions,
        "Perimeter": triangle_perimeters,
        "Area": triangle_areas
    }
    shape_frame = pandas.DataFrame(shape_dict)

    # bring tabulate
    shape_string = tabulate(shape_frame, 'keys', 'psql',
                            showindex=False,numalign="left", stralign="left")
    to_write.append(shape_string)

# circle
if len(circle_dimensions) > 0:
    to_write.append("\n--- Circle ---")
    shape_dict = {
        "No.": list(range(1, len(circle_dimensions) + 1)),
        "Dimensions": circle_dimensions,
        "Perimeter": circle_perimeters,
        "Area": circle_areas
    }
    shape_frame = pandas.DataFrame(shape_dict)

    # bring tabulate
    shape_string = tabulate(shape_frame, 'keys', 'psql',
                            showindex=False,numalign="left", stralign="left")
    to_write.append(shape_string)

# rectangle
if len(rectangle_dimensions) > 0:
    to_write.append("\n--- Rectangle ---")
    shape_dict = {
        "No.": list(range(1, len(rectangle_dimensions) + 1)),
        "Dimensions": rectangle_dimensions,
        "Perimeter": rectangle_perimeters,
        "Area": rectangle_areas
    }
    shape_frame = pandas.DataFrame(shape_dict)

    # bring tabulate
    shape_string = tabulate(shape_frame, 'keys', 'psql',
                            showindex=False,numalign="left", stralign="left")
    to_write.append(shape_string)

#square
if len(square_dimensions) > 0:
    to_write.append("\n--- Square ---")
    shape_dict = {
        "No.": list(range(1, len(square_dimensions) + 1)),
        "Dimensions": square_dimensions,
        "Perimeter": square_perimeters,
        "Area": square_areas
    }
    shape_frame = pandas.DataFrame(shape_dict)

    # bring tabulate
    shape_string = tabulate(shape_frame, 'keys', 'psql',
                            showindex=False, numalign="left", stralign="left")
    to_write.append(shape_string)


# follow the panda/file output plan
to_write.append("\n* means it is rounded to two decimal places.")


# Print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = f"Shape_Calculator_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")