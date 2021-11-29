"""
Keyword Review:

and         logical operator
as          part of the with-as statement, e.g. 'with X as Y: pass'
assert      ensure that something is true
break       stop this loop right now
class       define a class
continue    don't process more of the loop, do it again
def         define a function
del         delete from dictionary
elif        else if condition
else        else condition
except      if an exception happens, do this, e.g. 'except ValueError as e: print(e)'
exec        run a string as Python, e.g. exec 'print("hello")'
finally     exceptions or not, finally do this no matter what
for         loop over a collection of things
from        import specific parts of a module
global      declare that you want a global variable, e.g. 'global X'
if          if condition
import      import a module into this one, to use here
in          part of for-loops. Also a test of X in Y
is          like == to test equality
lambda      create a short anonymous function, e.g. s = lambda y: y ** y; s(3)
not         logical operator
or          logical operator
pass        this block is empty, e.g. def fname(arg): pass
print       print a string
raise       raise an exception, e.g. raise ValueError("No")
return      exit the function with a return value
try         try this block, and if exception then go to except
while       while-loop
with        with an expression as a variable, do something
yield       pause here and return to caller
"""

"""
Data Type Review:

True        boolean value
False       boolean value
None        no value e.g. X = None
byte        stores bytes, maybe of text, PNG, file, etc., e.g. x = b"Hello"
string      textual information
number      integers
float       decimals
list        an ordered list of things
dict        a key=value mapping of things e.g. e = {'x': 1, 'y': 2}
"""

"""
String Escape Sequences"

\\          backslash
\'          single quote
\"          double quote
\a          bell        # makes a sound. print("\a")
\b          backspace   # this moves the cursor one space to the left. The shell can be set up to interpret it to mean delete one character.
\f          formfeed    # equivalent to a page break.
\n          newline
\r          carriage    # historically used to move the cursor to the left side of the line. Useful for writing out command line progress or loading strings, for example.
\t          tab
\v          vertical tab
"""

"""
Review of Operators:

**          raise to power of
/           divide
//          floor divide, e.g. 9 // 2 returns 4
%           modulus, e.g. 9 % 2 returns 1
<=          less than or equal
>=          greater than or equal
@           at (decorators), e.g. @classmethod
    # A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function that you want to decorate.
"""
### Example of a decorator ###

# Assign a function to a variable:
def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5)) # = 6

# You can define a function inside a function:
def plus_two(number):
    def add_two(number):
        return number + 2

    result = add_two(number)
    return result
print(plus_two(4)) # = 6

# You can also pass a function as a parameter to another function:
def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one)) # = 6

# A function can also return another function:
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

hello = hello_function()
print(hello()) # prints "Hi"

# Nested functions can access the outer scope of the enclosing function:
def print_message(message):
    "Enclosing function"
    def message_sender():
        "Nested function"
        print(message) # it knows this variable from the parent function.

    message_sender()

print_message("Some random sender.")

# Creating a decorator to turn a sentence into upper case:
def uppercase_decorator(function): # we give the decorator a function
    def wrapper(): #
        func = function() # assign the input-function to a variable called func
        make_uppercase = func.upper() # upper() makes a string uppercase. Not really sure why we need to use the decorator at all...
        return make_uppercase

    return wrapper

@uppercase_decorator # this is the easiest way to apply the decorator.
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate()) # this prints 'HELLO THERE' even if we don't have the @uppercase_decorator above the say_hi() function.

print(say_hi()) # this prints 'HELLO THERE' as long as we have the @uppercase_decorator above the say_hi() function.
