#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def horizontal():
	print('+ - - - -', end = ' ')

def vertical():
	print('|        ', end = " ")

def horizontal_line():
	do_twice(horizontal)
	print('+')

def horizontal_line_4():
	do_four(horizontal)
	print('+')

def vertical_line():
	do_twice(vertical)
	print('|')

def vertical_line_4():
	do_four(vertical)
	print('|')

def print_horizontal():
	horizontal_line()
	do_four(vertical_line)

def print_row_4():
	horizontal_line_4()
	do_four(vertical_line_4)

def two_by_two():
	do_twice(print_horizontal)
	vertical_line()
	horizontal_line()

def four_by_four():
	do_four(print_row_4)
	horizontal_line_4()
	



# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    two_by_two()
    four_by_four()



if __name__ == "__main__":
    main()