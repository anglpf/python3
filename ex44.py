"""

Most of the uses of inheritance can be simpified or replaced with composition, and multiple inheritance should be avoided at all costs.

There are 3 ways that parent and child classes can interact:

1. Actions on the child imply an action on the parent.
2. Actions on the child override the action on the parent.
3. Actions on the child alter the action on the parent.

"""

# IMPLICIT INHERITANCE
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


# EXPLICIT OVERRIDE
class Grandmother(object):

    def override(self):
        print("GRANDMOTHER override()")

class Mother(Grandmother):

    def override(self):
        print("MOTHER override()")

gma = Grandmother()
mum = Mother()

gma.override()
mum.override()


# ALTER BEFORE OR AFTER
class Grandfather(object):

    def altered(self):
        print("GRANDFATHER altered()")

class Father(Grandfather):

    def altered(self):
        print("FATHER, BEFORE GRANDFATHER altered()")
        super(Father, self).altered() # basically asks the parent class for the function altered(), and so prints 'GRANDFATHER altered()'
        print("FATHER, AFTER GRANDFATHER altered()")

gpa = Grandfather()
dad = Father()

gpa.altered()
dad.altered()


# COMPOSITION
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()
son.implicit()
son.override()
son.altered()

"""
Zed's advice:

Use composition to package code into modules that are used in many different unrelated places and situations.

Use inheritance only when there are clearly-related, reusable pieces of code that fit under a single common concept.

"""
