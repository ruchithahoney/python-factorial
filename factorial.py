# Python program to find the factorial of a number provided by the user.

def find_factorial(num):

    factorial = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    return factorial



num = 7

factorial = find_factorial(num=num)

print("The factorial of",num,"is",factorial)