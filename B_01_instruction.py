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


# Main Routine goes here

# displays name of the program
print(make_statement("Shape Calculator", "="))

# checks if the users want to see the instruction or not
want_instructions = yes_no_check("Do you want to see the instructions? ")
print()

# display instruction if users choose 'yes'
if want_instructions == "yes":
    instructions()
