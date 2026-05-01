"""
File: stack_frame_error.py
Name:
------------------------
This program demonstrates the concept
of parameter passing through stack
frames.

By examining how values are passed
between functions, students can better
understand how function calls work.
"""


def main():
    """
    This program prints the value of a
    on Console. Is it 0 or 1?
    """
    print('-------------')
    a = 0
    plus_one(a)
    print(a)
    print('-------------')


def plus_one(a):
    """
    :param a: the number to be incremented
    """
    a += 1


if __name__ == '__main__':
    main()
