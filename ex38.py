ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # break up the string where there are spaces
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop() method removes and returns the last object from a list.
    print("Adding: ", next_one)
    stuff.append(next_one) # add the last item from more_stuff to stuff
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # print the second object in stuff
print(stuff[-1]) # print the last object in stuff
print(stuff.pop()) # remove and return the last object in stuff
print(' '.join(stuff)) # opposite of split, i.e. make the list stuff into a string with each object separated by a space.
"""
Recall that the syntax for split is
    string.split(' ')
while the syntax for join is
    ' '.join(list)
"""
print('#'.join(stuff[3:5])) # same as above but only objects 3 and 4 in the list 'stuff' and use # instead of a space.

"""
When to use lists:

You use a list whenever you have something that matches the list data structure's useful features:

1. You need to maintain order. Remember, this is a listed order, not a sorted order. Lists do not sort for you.
2. If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
3. If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.
"""

"""
Object-Oriented Programming, and Classes in Python:

A Class is like an Object-constructor, or a 'blueprint' for creating Objects. Classes provide a means of bundling data and functionality together. An Object is an instance of a Class.
When an Object of a Class is created, the Class is said to be instantiated. All the instances share the attributes and the behaviour of the Class. But the values of those attributes are unique for each Object. A single Class may have any number of instances.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person('Angus')
p.say_hi()
