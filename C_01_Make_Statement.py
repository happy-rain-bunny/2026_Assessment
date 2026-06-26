# function goes here...

def make_statement(statement, decoration):
    """Put headings of the project to let users know
     what project it is and emphasise it by adding
     decoration at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"

# Main routine goes here

print(make_statement("Shape Calculator", "="))