import random

number = 0

def isPerfect(num: int) -> bool:
    """
    Checks if a number is perfect. A number is perfect if the sum of the
    factors of the number is the number itself.
    
    i.e.
    6 is the smallest perfect number. It is divisible by 1, 2, 3, and 6.
    1+2+3 -= 6
    """
    total = 0
    for i in range(1, int(num/2)+1):
        if (isDivisible(num, i)):
            total += i
    return total == num
        
def isDivisible(num: int, x: int) -> bool:
    """
    Checks to see if the num inputted is divisible by x.
    """
    return num % x == 0

number = random.randint(1, 100)
print("The number:", number)
print("The number is perfect:", isPerfect(number))
