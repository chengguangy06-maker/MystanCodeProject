def main():
    a = int(input('a= '))
    b = int(input('b= '))
    print(power(a,b))
def power(a,b):
    ans = 1
    for i in range(b):
        ans = ans*a
    return  ans

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
