# To get input from the user, the input() method can be used.
my_name = "Kevin"
your_name = input("Enter your name: ")

print(f"Hello, {your_name}. My name is {my_name}.")

"""
Input will always return a string. So if when asking for input and a number is
entered, it will function as a string instead of an integer.

age = input("Enter your age: ") # This will return a string. If the user enters
                                # 35 it will be read as "35"

To get around this we can use the int() function. Like how str() converts values
into strings, int() converts values into integers.
"""

# Nesting the input() function inside the int() allows for a cleaner code
age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} months.")


# Exercise: Calculate how many seconds someone has lived based on their age.
age = int(input("Enter your age: "))
days = age * 365.2525
hours = days * 24
minutes = hours * 60
seconds = round(minutes * 60 )
print(f"You have lived for {seconds} seconds.")