my_string = "Hello, World!"
print(my_string)

# When writing string the quotation marks have to match
# Also when writing strings with quotes inside they need to be different quotation marks
string_with_quotes = "Hello, it's me."
print(string_with_quotes)

# Another Example
another_string_with_quotes = "He said 'You are amazing!'"
print(another_string_with_quotes)

# Muliline strings can be written like this:
multiline = """Hello, World.

My name is Kevin. Welcome to my program.
"""
print(multiline)


"""
Multiline strings are useful when writing longer strings,

But can also be useful for leaving comments. This multiline string will
not be shown in the program. 
When writing longer comments you can use a multiline string instead of 
using multiple pound symbols( # ) when leaving a comment
"""

# Strings can be added together just by using the plus symbol ( + )
first_name = "Kevin"
greeting = "Hello, " + first_name
print(greeting)


"""
Integers cannot be added to strings. To add integers to strings they need to be 
converted to a string.

Using the str() method and integer can be converted to a string
Alternatively the number can be saved as a string by writing it as a string.
Ex. "29"
"""
age = 29
age_as_string = str(age)
print("You are " + age_as_string)


"""
Another way to do this without converting is using string interpolation. 
In python this is refered to as an f string.
"""
print(f"You are {age}")


"""
A limitation of f strings is that if a variable value used in an f string
changes the value in the f string varialbe wont change
"""
# Ex.
name = "Kevin"
greeting = f"How are you, {name}?"
print(greeting)

name = "John"
print(greeting)
"""
greeting still prints Kevin even though the name variable has changed. This
is because when the greeting variable was made, the name variable was Kevin
"""

"""
Another way to write this to get around the f string limitation is using the 
format() method.

Using this method there needs to be an empty curly brace in the string that you 
want to format. The format() method will look for the curly brace and insert the
variable/string inside it.

You are able to write something in the curly brace as well, but when using the
format() method it will need to specify what it is looking for and what the
value will be. 

This may be useful if there are multiple changing variables within a string.
"""
# final_greeting = "How are you, {}?"
final_greeting = "How are you, {name}?"

# EMPTY CURLY BRACE
# john_greeting = final_greeting.format(name)
# print(john_greeting)

# NAMED CURLY BRACE
friend_name = "Jeff"
jeff_greeting = final_greeting.format(name = friend_name)
print(jeff_greeting)




