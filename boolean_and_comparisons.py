"""
There are different symobls that can be used to compare values:

== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to

A single "=" is used to assign a value to a variable. Not used for comparison

When comparing values, Python will return a bool value of either True or False
"""

my_number = 5
user_number = int(input("Enter a number: "))

print(my_number == user_number)

"""
You can have multiple compairsions using the "and" and "or" keywords

Using the "and" keyword will return True if both comparisons are true. If one is false, the whole expression will be false

Using the "or" keyword will return True if either comparison is true. If both are false, the whole expression will be false

When writing booleans you usually don't want to write them as negatives. 
    Ex. can_not_learn = age < 0 and age > 200

This can be confusing to read and hard to understand. It's better to write them as positives.
    Ex. can_learn = age > 0 and age < 200

The "not" keyword can be used to invert a boolean value
"""
age = int(input("Enter your age: "))
can_learn = age > 0 and age < 200

print(f"You can learn: {can_learn}")

number = int(input("Enter a number: "))
is_divisible = number % 3 == 0 or number % 5 == 0

print(f"The number is divisible by 3 or 5: {is_divisible}")


"""
You can convert values into boolean values using the bool() function
    Ex. bool("hello") will return True
        bool(11) will return True

Most values will return True when converted to a boolean value, but there are some values that return False
    Ex. bool(0) will return False
        bool("") will return False
        bool(None) will return False

True and False
    If you have a variable asigned to a True and False value, it will look at the first value and see if it's True or False. If it's True will return the second value, if it's False it will return the first value
        Ex. x = 35 and 0 (This will return False(0) because the first value is True(35))

True or False
    Using the keyword "or" in the same way as the above example with "and" will act in the opposite way. If the the first value is True, it will return the first value. If the first value is False, it will return the second value
        Ex. x = 35 or 0 (This will return True(35) because the first value is True(35))
"""
a = 35 and 0
print(a)
x = 35 or 0
print(x)

# Example
name = input("Enter your name: ")
surname = input("Enter your surname: ")
greeting = name or surname
print(f"Hello, Mr./Mrs./Ms. {greeting}")
"""
This example uses the "or" keyword which means that if the first value is True it will return the first value, otherwise it will return the second. If somone decided not to enter their name but enters their surname, it will return their surname.
"""