"""
File: count_ch.py
Name:
----------------------
The goal of this program is to count
the number of uppercase letters in
different words: 'ApPLE', 'Jerry', and 'PineApple'.

It defines a function called
num_upper() to perform the counting.
This function is then used to countp-[
the uppercase letters in several
example words and print the results.
"""


def main():
    s = 'ApPLE'
    s2 = 'Jerry'
    s3 = 'PineApple'
    print(num_upper(s)) #4
    print(num_upper(s2)) #1
    print(num_upper(s3))#2
def num_upper(s4):
    ans = 0
    for i in range(len(s4)):
        ch = s4[i]
        if ch.isupper():
            ans += 1
    return  ans


if __name__ == '__main__':
    main()