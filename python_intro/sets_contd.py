cars_set_1 = {"Ford", "Chevrolet", "Lexus"}
cars_set_2 = {"Toyota", "Lexus", "Acura"}

"""
You can use the difference() function to find the values that are in one set but not the other.

Ex. set_1_but_not_2 = cars_set_1.difference(cars_set_2)

The first set is the set you are comparing and the second set inside the difference() function is the set that you want to compare to the first set.

The example will return the values that are in the first set but not the second.

difference() returns elements that are in one but not the other.
"""

set_1_but_not_2 = cars_set_1.difference(cars_set_2)
print(set_1_but_not_2)
# This will not return "Lexus" because that value is in the second set
# It will return the values that are unique to the first set
  
set_2_but_not_1 = cars_set_2.difference(cars_set_1)
print(set_2_but_not_1)
# This will not return "Lexus" because that value is in the first set
# it will return the values that are unique to the second set



"""
There is a function called symmetric_difference() which will return the values that are unique to both sets. 

symmetric_difference() returns elements that are not in either.
"""
not_in_both = cars_set_1.symmetric_difference(cars_set_2)
print(not_in_both)
# This will return the values that are unique to both sets
# Because "Lexus" is in both sets, this function will return the values other than "Lexus" because it is shared by both sets.



"""
To find the values that are in both sets you can use the intersection() function.

Ex. in_both = cars_set_1.intersection(cars_set_2)

This will check if the first set has any common values with the second set. If there are any common values, those values will be returned.
"""
in_both = cars_set_1.intersection(cars_set_2)
print(in_both)
# This will return "Lexus" because it is in both sets



"""
To make set with the values from both sets you can use the union() function.

Ex. all_values = cars_set_1.union(cars_set_2)

This will return all the values from both sets.
"""
all_cars = cars_set_1.union(cars_set_2)
print(all_cars)