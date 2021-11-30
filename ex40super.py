class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle): # this says that Square is a subclass of the previously-defined Rectangle class.
    def __init__(self, length):
        super().__init__(length, length) # I guess this expresses how the sub-class Square relates to the super-class Rectangle.

square = Square(4)
print(square.area()) # prints 16

class Cube(Square):
    def surface_area(self):
        face_area = super().area() # instead of rewriting the area() formula, we reference the Rectangle class via the Square class in order to pull it in here. Avoids hard-coding in multiple places; very handy. But beware: if Square also had a function called area(), we'd need to make sure we call the right one... by using super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super().area() # is there a way to write it so that we don't have to duplicate this line?
        return face_area * self.length

cube = Cube(3)
print(cube.surface_area())
print(cube.volume())

"""
Python supports multiple inheritance, in which a sub-class can inherit from multiple super-classes that don't inherit from each other (otherwise known as sibling classes).
https://realpython.com/python-super/#an-overview-of-pythons-super-function
"""

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area() # Both super-classes, Square and Triangle, have a function called area(). We get an error if we leave the script like this. The traceback references the Triangle formula for area(), so we know that it's calling that.
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

pyramid = RightPyramid(2,4)
print(pyramid.area())
