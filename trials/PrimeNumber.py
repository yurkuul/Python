import random

number = 0

def isPrime(num: int) -> bool:
    """
    Checks if the number inputted is prime.
    """
    count = 0 #counts how many times the num is divisible by
    for i in range(1, int(num/2)+1):
        if isDivisible(num, i):
            #1 is the default number of times a number should be divisible 
            #by a number
            count += 1
        if (count > 1):
            return True
    return False
        
def isDivisible(num: int, x: int) -> bool:
    """
    Checks to see if the num inputted is divisible by x.
    """
    return num % x == 0

number = random.randint(1, 100)
print("The number:", number)
print("The number is prime:", isPrime(number))
