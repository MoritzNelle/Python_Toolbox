'''
READ ME:
- The module contains one class: Triangle
- The Triangle class has two methods: calculate_circumference and calculate_area
- The module imports the 'math' module for mathematical operations

DESCRIPTION:
- The Triangle class represents a triangle defined by two points (point_b and point_c) in a 2D space.
- The calculate_circumference method calculates the circumference of the triangle.
- The calculate_area method calculates the area of the triangle.

PARAMETERS:
- The Triangle class constructor takes two parameters:
    - point_b (tuple): a tuple of two numbers representing the coordinates of point B.
    - point_c (tuple): a tuple of two numbers representing the coordinates of point C.
- The calculate_circumference and calculate_area methods do not take any parameters.

LIMITATIONS:
- The Triangle class assumes that the points are represented as tuples of two numbers. If the points are not in this format, an error will be raised.
- The Triangle class does not check if the points form a valid triangle (i.e., the points are not collinear). If the points are collinear, the calculated circumference and area will not be correct.

STRUCTURES:
- The Triangle class uses a constructor (__init__) to initialize the points.
- The calculate_circumference method uses the Pythagorean theorem to calculate the lengths of the sides and then adds them up to get the circumference.
- The calculate_area method uses the formula for the area of a triangle given the coordinates of its vertices.

OUTPUTS:
- The calculate_circumference method returns the circumference of the triangle.
- The calculate_area method returns the area of the triangle.
- The module contains test code that prints the circumference and area of a sample triangle to the console.
'''

import math

class Triangle:

# CLASS CONSTRUCTOR (initilizer):
# A class constructor is a special method in Python classes that is automatically called #when a new instance of the class is created.
# The constructor method is named __init__ and is used to initialize the attributes #(variables) of the class.
# In this case, the Triangle class constructor takes two parameters: point_b and point_c, #and assigns them to the corresponding attributes of the class.

# SELF:
# The self parameter is a reference to the current instance of the class.
# E.g., self.point_b refers to the point_b attribute of the current instance of the #Triangle class.
# Syntax: def __init__(self, param1, param2, ...): 
    # self is a reference to the current #instance of the class
    # instance variable are declared by self.var_name = var_name

    def __init__(self, point_b, point_c):   # constructor
        self.point_b = point_b              # declare instance variable
        self.point_c = point_c              # -"-

# METHODS:
# Methods are functions defined inside a class that operate on the attributes(variables) of the class.
# They are called using the dot notation (self.atribute) on an instance of the class, e.g., triangle1.calculate_circumference().

    def calculate_circumference(self):      # method
        dx = self.point_c[0] - self.point_b[0]
        dy = self.point_c[1] - self.point_b[1]
        side_length = math.sqrt(dx**2 + dy**2)
        circumference = side_length * 2 + math.sqrt(self.point_b[0]**2 + self.point_b[1]**2) + math.sqrt(self.point_c[0]**2 + self.point_c[1]**2) # formula for circumference
        return circumference

    def calculate_area(self):                   # well ... another method
        area = abs(self.point_b[0] * self.point_c[1] - self.point_c[0] * self.point_b[1]) / 2   # formula for area
        return area


# Test code
if __name__ == "__main__":
    triangle1 = Triangle((0,2), (1,1))                                  # create an object of the class Triangle
    print(f"Circumference: \t{triangle1.calculate_circumference()}")    # call the method calculate_circumference from the class Triangle for the object triangle1
    print(f"Area: \t\t{triangle1.calculate_area()}")                    # call the method calculate_area ...