mystuff_dictionary = {'apple': "I AM DICTIONARY APPLES!"}
print(mystuff_dictionary['apple']) # get apple string from a dictionary

import mystuff # mystuff.py is a file in the same directory that defines a single function that prints "I AM APPLES!"

mystuff.apple() # get apple string from a module (i.e. another python file)

print(mystuff.tangerine) # get a variable that is declared in another module

"""
We have a common pattern in Python: take a key=value style container and get something out of it by the key's name.
1. Container is a dictionary, key is a string, and the syntax is [key]
2. Container is a module, key is an identifier, and the syntax is .key() or .key
You can think about a module as a specialised dictionary that can store Python code so you can access it with the . operator.
A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . operator.
"""

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between" # this sets the tangerine instance variable

    def apple(self):
        print("I AM CLASSY APPLES!")

"""
When you instantiate a class, you get an object.
An object is an instance of a class.
"""

thing = MyStuff()
thing.apple() # because 'thing' is an instance of the class MyStuff, so we can call the MyStuff functions and variables on thing using the . (dot) operator.
print(thing.tangerine)

"""
What's happening here:
1. Python sees that MyStuff is a class that we've defined above.
2. Python creates an empty object with all the functions I specified in the class (using def).
3. Python looks to see whether we wrote an __init__ function, and because we did it calls that __init__ function to initialise our newly-created empty object.
4. In the MyStuff function __init__ we then get this extra variable called 'self', which is the empty object that Python made in step 2. We can set variables on this just like we would with a module, dictionary, or other object.
5. In our case, we set self.tangerine to a song lyric, then initialise this object.
6. Now Python takes the newly-created object and assigns it to the 'thing' variable for us to work with.
"""

# dict style
mystuff_dictionary['apple']

# module style
mystuff.apple()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)
