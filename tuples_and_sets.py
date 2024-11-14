"""
Tuples are like a list in the way that it is able to store multiple values in a single variable.

To define a tuple you can just define it with multiple values seperated by commas.

Ex. my_tuple = 1, 2, 3

Though this is a tuple, it can be made clearer to see if they are within parentheses()


Ex. my_tuple = (1, 2, 3)

If you want to have a tuple inside of a list, there will need to be the use of parentheses to show that it is a tuple inside of a list

Ex. list_with_tuple = [(1, 2, 3), 4, 5]
"""

cars = ("Toyota", "Honda", "Ford")
cars += ("Tesla",)
# cars = cars + ("Tesla",)

print(cars)

"""
A big difference between tuples and lists is that you cannot add or remove values from a tuple.

If you want to "add" a value to a tuple you can use the += operator. In a technical sense this doesn't add a value to the tuple, but rather it creates a new tuple with the values of the original tuple and the new value.

Tuples are useful when you want to keep them unchanged.

Use lists when you want to allow modifications
"""



"""
Sets are like lists and tuples except they are unordered and cannot have duplicate values.

To define a set you can use curly braces {}.

Ex. my_set = {1, 2, 3}

To add a value to a set you can use the add() function.
To remove a value from a set you can use the remove() function.
"""

classes = {"Math", "Physics", "Chemistry"}
print(classes)

classes.add("English")
print(classes)

classes.remove("Chemistry")
print(classes)

# Because it's unordered the values will not stay in the same order as they were added or written.