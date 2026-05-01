"""
File: guess_my_number.py
Name:
-----------------------------
This program runs a console game
called "Guess My Number".

The program repeatedly asks the user
to guess a number until the correct
answer is given.
"""

# This number controls when to stop the game
SECRET = 32


def main():
    print('Guess an int from 0 to 99')
    while True:
        guess = int(input('Guess: '))
        if guess == SECRET:
            break
        elif guess > SECRET:
            print('too high')
        else:
            print('too low')
    print('Congrats! the answer: '+str(SECRET))




    # guess = int(input('Guess: '))
    # while guess != SECRET:
    #     if guess > SECRET:
    #         print('too high')
    #     else:
    #         print('too low')
    #     guess = int(input('Guess: '))
    # print('Congrats! the answer: '+str(SECRET))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
