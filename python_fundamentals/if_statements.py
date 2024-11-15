"""
If statements runs a block of code based on whether boolean condition is met.

To create an if statement you just use the keyword "if" and then write out the condition that needs to be met.

To write the body of the if statement, it needs to be indented so that Python knows that that's the code it will run if the condition is met.

If there is no indentation then that code is not part of the body of the if statement.

Example:

if *condition*:
    *block of code*
    *block of code*

If it is written like this:

if *condition*:
*block of code*

The block of code is not part of the if statement and will cause an error

As long as it is indented it is part of the if statement. Once the indentation is removed the if statement will be finished.
"""

friend_name = "John"
user_name = input("Enter your name: ")

if user_name == friend_name:
    print("Hello, friend")
    print("This will run too")

print("This will always run")

"""
This if statement is checking to see whether the name that is inputed as in the user_name matches the friend_name.

If the user_name matches the friend name it will go into the body of the if statement and print "Hello, friend"

If it doesn't match, it will not run the next line.
"""

number = 1
user_number = int(input("Enter a number: "))

if user_number == number:
    print("You got it right")

# if user_number != number:
#     print("You got it wrong")
else:
    print("You got it wrong")

"""
Writing mulitple if statements for multiple scenarios can get lengthy espcially if they are related to each other.

Python has the "else" keyword that comes after "if" to say that if this condition isn't met, do this instead.

Example:
if *condition*:
    *block of code*
    *block of code*
else:
    *block of code*
    *block of code*

If there is anything else that comes between the if and else statements it will cause an error because now the if and else statements aren't connected.

Example:
if *condition*:
    *block of code*
    *block of code*
*code*
else:
    *block of code*
    *block of code*
"""


"""
Because there are values that evaluate to True and False, those values can be used as the "if" condition.
The "if" condition doesn't always have to be a comparison. It just needs to evaluate to True or False.
"""
name = input("Enter your name: ")

print(bool(name))

if name:
    print("I know your name.")

# An empty string will evaluate to False and the if statement body will not run
# As long as something is inputed it will evaluate to True

"""
You can use if statements to check if a value is in a list by using the "in" keyword.

Example:
if *input* in *list*:
    *block of code*
    *block of code*
*code*
else:
    *block of code*
    *block of code*

Additionally to run a chain of related if statements you can use the keyword "elif" (else if).
This is used to say that if one condition isn't met check this condition or this condition.

You can finish this with the "else" keyword to say that if none of the conditions are met, run this.
"""

fruit_i_like = ["apple", "banana", "grape"]
fruit_i_dont_like = ["pineapple", "blueberry"]

fruit = input("Enter a fruit: ")

if fruit in fruit_i_like:
    print("I like this")
elif fruit in fruit_i_dont_like:
    print("I don't like this")
else:
    print("This is a fruit")
