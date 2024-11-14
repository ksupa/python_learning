"""
Dictionaries in Python store key-value pairs. 

Within a dictionary there is a key and the key holds a value. To access the value you need to use the key.

Dictionaries are made by using curly braces {}
To make a key-value pair you create the key and seperate it from the value by using a colon.

Ex. friend_ages = {"Kevin": 15, "John": 25, "Alex": 35} 

Accessing the value is the same as accessing a value from a list, but instead of putting the index number inside the square brackets you will use the key from the dictionary.

Ex. friend_ages["Kevin"]

This will return 15 because that is the value for the key "Kevin"
"""

smartphones = {
    "iPhone 5": 2013, 
    "Samsung Galaxy s6": 2015, 
    "Google Pixel": 2016
}

print(smartphones["Google Pixel"])

"""
To add a value into a dictionary you can use the following syntax

Ex. friend_ages["Taylor"] = 20
This will add a key-value pair to the end of the dictionary.

Addiotionally, you can edit the value of a key by using the same syntax

Ex. friend_ages["Kevin"] = 16
"""

smartphones["OnePlus 11"] = 2023
smartphones["iPhone 5"] = 2012

print(smartphones)



"""
A key difference between sets and dictionaries is that dictionaries keep their order and sets do not.

Also dicionaries do not allow for duplicate keys.

You can have dictionaries inside of a list/tuple

To access the values of the dictionary inside of the list/tuple you'll need to use square brakets to access the index of the list/tuple and then square brackets again to access the key of the dictionary.
"""

cars = (
    {"make": "Toyota", "model": "Camry", "year": 2020},
    {"make": "Honda", "model": "Civic", "year": 2019},
    {"make": "Ford", "model": "Mustang", "year": 2018}
)

print(cars[1]["year"])

"""
This is a tuple with a three dictionaries inside of it each with 3 key-value pairs.
"""



"""
To turn data into a dictionary you can use the dict() function.

Ex. friends = [("Kevin", 15), ("John", 25), ("Alex", 35)]

To make this list of tuples into a diciontary the dict() function can be used.

Ex. friends = dict(friends)

This will turn the list of tuples into a dictionary. The first value of the tuple being the key and second value of the tuple being the value in the key value pair.
"""