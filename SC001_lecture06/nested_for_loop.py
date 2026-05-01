"""
File: nested_for_loop.py
Name:
------------------------
This program demonstrates the basic
concept of a nested (double) for loop
by printing a rectangle with 4 rows
and 3 columns.
"""

# These constants control the diameter of the rectangle
ROW = 4  # The number of rows
COL = 3  # The number of cols


def main():
	for i in range(ROW):
		for i in range(COL):
			print('#',end="")
		print("")


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
