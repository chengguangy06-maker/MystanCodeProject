"""
File: find_max.py
Name:
--------------------------
This program finds the maximum value
among all user inputs.

This file can be used as a reference
when working on Problem 4 in
Assignment 2.
"""

# This constant controls when to stop
EXIT = -1


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print('This program finds max')
    data =int(input('Data:'))
    if data == EXIT:
        print('No data')
    else:
        maximum = data
        minimum = data
        while True:
            data = int(input('Data: '))
            if data > maximum:
                maximum = data
            if data < minimum:
                minimum = data
            if data == EXIT:
                break
        print('Max '+str(maximum))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
