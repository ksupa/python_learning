# Variables are written by just writing the variable name and assigning it a value
age = 10
print(age)


# The variable can be changed and later in the code but will remain the orignal value until it is changed
age = 20
print(age)

# When writing a variable that will not change it's written in all caps
PI = 3.14
print(PI)

# When writing a variable name that is mulitple words long it's written in snake case
long_varaible_name = 0
print(long_varaible_name)

# Variable names can also have numbers but cannot start with a number
# Variable names can only consist of numbers, letters and underscores


# When using math functions, it still follows the same math rules like BEDMAS
# There are two types of numbers in python: Integers and Floats

# Integers are whole numbers like 1, 2, 3, 4, 5
# Floats are decimals values like 1.0, 2.0, 3.1, 4.23

# When doing division it will always give back a float
float_division = 12 / 3
print(float_division) # This will return 4.0

# You can also do integer division to return a whole number
# This is done by using two division symbols ( // )
integer_division = 12 // 3
print(integer_division) # This will return 4

# If it is a number that doesn't divide equally with each other it doesn't round the result
integer_division = 13 // 5
print(integer_division) # The float answer is 2.66 but the integer will return 2

# To find the remainder of an integer division statement you can use the modulus symbol ( % )
remainder = 13 % 5
print(remainder) # This will return 3 (5 goes into 13 only 2 times which leaves a remainder of 3)

# The modulus symbol can be used to determine whether a number is odd or even
# We can take a number and use the modulus by 2 and to determine whether there is a remainder of 0 or 1
# A remainder of 0 represents an even number and a remainder of 1 represents an odd number

# Ex. 10 / 2 = 5 (10 % 2 = 0 (It divides into 2 evenly with a remainder of 0 so 10 is an even number))
# Ex. 11 / 2 = 5 (11 % 2 = 0 (It doesn't divide into 2 evenly. There is a remainder of 1, so 11 is an odd number))
x = 37
remainder = x % 2
print(remainder) # This will return 1 because 2 goes into 37 13 times which equals 36. That leaves a remainder of 1. This means 37 is an odd number.
