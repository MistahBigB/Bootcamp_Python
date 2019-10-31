#Practice: Fundamentals
#If you have anything that's repeated, try to write a function, or at least a loop
'''
Problem 1
Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
'''

#Remember that returning a value does not mean display it
#the function can be printed, or a print statement can be put in the function

def even_odd(a):
    if a%2 > 0:
        return "odd"
    else:
        return "even"

x = int(input("What's your number?\n>"))
print(even_odd(x))
'''
Problem 2
Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
'''
def truth(a, b):
    if a > 0 > b:
        return True
    else:
        return False

x = int(input("What's your first number?\n>"))
y = int(input("What's your second number?\n>"))
print(truth(x, y))
'''
Problem 3
Write a function that returns True if a number within 10 of 100.
'''
def near(a):
    if 110 >= x >=90:
        return True
    else:
        return False

x = int(input("What's your number?\n>"))
print(near(x))
'''
Problem 4
Write a function that returns the greatest of 3 parameters.
'''
nums = []

def greatest(*args):
    for i in range(0, 3):
        number = int(input("What's your number?\n>"))
        nums.append(number)

greatest(nums)

print(f"Biggest number entered is: {max(nums)}")
print(f"Smallest number entered is: {min(nums)}")

#without a function, variable number of parameters
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

'''
Problem 5
Print out the powers of 2 from 2^0 to 2^20

1, 2, 4, 8, 16, 32, ...
'''
for i in range(21):
    return(2**i)
#OR
def powers(a):
    for i in range(x):
        return(2**x)

x = int(input("How high would you like to raise 2?"))
print(powers(x))
