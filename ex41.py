"""
class           tell Python to make a new type of thing.
object          two meanings: the most basic type of thing, and any instance of some thing.
instance        what you get when you tell Python to create a class.
def             how you define a function inside a class.
self            the variable for the instance/object being accessed, inside the functions in a class.
inheritance     one class can inherit traits from another class.
composition     a class can be composed of other classes.
attribute       a property that classes have; from composition, and are usually variables.
is-a            a phrase to say that something inherits from another.
has-a           a phrase to say that something is composed of other things.
"""

class X(Y):
    'make a class named X that is-a Y'

class X(object): def __init__(self, J)
    'class X has-a __init__ that takes self and J parameters'

class X(object): def M(self, J)
    'class X has-a function named M that takes self and J parameters'

foo = X()
    'set foo to an instance of class X'

foo.M(J)
    'from foo, get the M function, and call it with parameters self and J'

foo.K = Q
    'from foo, get the K attribute and set it to Q'
