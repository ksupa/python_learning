"""
Lists allow you to store multiple values in a single variable. Instead of having 
multiple variables, you can easily put all of them in one variable

Lists are made by using square brackets []

Ex. my_list = [1, 2, 3]
"""
# fruit1 = "apple"
# fruit2 = "banana"
# fruit3 = "blueberry"

fruits = ["apple", "banana", "blueberry"]

"""
To access values inside a list you type the list name followed by the index of 
the value you want to access inside of square brackets

Lists in Python start at index 0. This means the first value in a list will be 
accessed by [0]

There can be an unlimited number of values and multiple data types in a list, 
and when making a list the values should usually be related to the list name. 
A list of fruits should contain names of fruits.

This keeps the data organized and easy to understand.

To find the length of a list you can use the len() function.
"""

print(fruits[0])
print(len(fruits))

"""
You can nest lists inside of other lists. This is called a list of lists.

When there are many lists inside the list it's good to have them on separate 
lines so that it's easier to read.

To access a value inside a nested list you use two sets of square brackets. 

Ex. fruits_inside_house[0][0]

The first square brackets access the first list in the entire list, the second 
square brackets accesses the first value in the first list. 
"""
fruits_inside_house = [
    ["apple", 2], 
    ["banana", 6], 
    ["blueberry", 20], 
    ["cherry", 10], 
    ["orange", 8], 
    ["pineapple", 4],
]

print(fruits_inside_house[0][0]) #This returns apple
print(fruits_inside_house[4][1]) # This returns 8. 
# 4 is the index for the fifth list and 1 is the index for the second value in 
# the fifth list. The fifth list is for orange.

"""
To add a value to a list you can use the append() function. 
This will add a value to the end of the list.

To remove a value from a list you can use the remove() function. 
This will remove the first instance of the value you want to remove.

To remove a list that is nested inside a list you can use remove() but you will 
have to remove the entire list explicitly.

Ex. remove(fruits_inside_house["apple", 2])
"""


"""
There is a .join() function that will take values of a list/tuple and create a
string that joins the values and separates them with a your choice of separator.
"""

print(f"I like {fruits}")
comma_separated = ", ".join(fruits)

print(f"I like {comma_separated}.")
# Instead of returning the list with the square brackets around it, join() 
# creates a new string