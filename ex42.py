## Animal is-a object
class Animal(object):

    def oink(self):
        print("Oink!")


## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a attribute name whose value is name.
        self.name = name

    def woof(self):
        print(f"{self.name} goes woof!")


## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a attribute name whose value is name.
        self.name = name

    def meow(self):
        print(f"{self.name} goes meow!")


## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a attribute name whose value is name.
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def hello(self):
        print(f"{self.name} says hello!")

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## This is how we run the __init__ of a parent class reliably.
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

    def please(self):
        print(f"{self.name} would like a raise.")


## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet. Her pet is-a Cat whose name is satan
mary.pet = satan

## frank is-a Employee and Frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet whose name is rover. Rover is-a Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()


satan.meow()
rover.woof()
rover.oink()

mary.hello()
frank.please()
frank.hello()


"""

In Python 2.2 there were two types of class:

1. those defined by C extensions and C coded built-ins
2. those defined by Python class statements

There were problems when you wanted to mix these types, with various ugly workarounds implemented.
So, new-style classes were created to unify the two types, including the ability to inherit from them.
For backward compatibility, the bare class syntax creates an old-style class, while the new behaviour is obtained by inheriting from object.

The most visible differences in behaviour are:

**  The Method Resolution Order (MRO). Take diamond-shaped inheritance hierarchies (e.g. A inherits from B and C, which both inherit from base class D). Previously, methods were looked up A B D C D, so if C overloads D then it won't be used by A. This is bad for mixin programming. New-style classes look up in the order A B C D. Look at the __mro__ attribute of a class to see the order it will search.

** The __new__ constructor is added, which allows the class to act as a factory method, rather than return a new instance of the class. This is useful for returning particular subclasses, or reusing immutable objects rather than creating new ones without having to change the creation interface.

** Descriptors. These are the feature behind such things as properties, classmethods, staticmethods, etc. Essentially, they provide a way to control what happens when you access or set a particular attribute on a (new-style) class.

"""
