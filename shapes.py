"""
    This module defines a class hierarchy for representing various geometric shapes.

    Classes:
    - Shape: Base class for all shapes. Provides the common interface (abstract methods) for
            calculating area and perimeter.
    - Circle: Represents a circle with a given radius.
    - Rectangle: Represents a rectangle with a given length and width.
    - Triangle: Represents a triangle with given side lengths.

    Key Points:
    - Each class inherits from the `Shape` base class.
    - Each class overrides the `calculate_area` and `calculate_perimeter` methods to provide
    shape-specific implementations.
    - The `Shape` class has abstract methods, which means they must be implemented in derived
    classes.

    How to Use:
    - Import the necessary classes from this module into your code.
    - Create instances of the desired shape classes with appropriate arguments.
    - Use the methods of the shape objects to calculate and access their properties.
"""

import math

class Shape:
    """Base class constructor for all shapes."""
    def __init__(self, color):
        """Initializes the shape with a given color."""
        self.color = color

    def calculate_area(self):
        """Calculates and returns the area of the shape.

        This is an abstract method that must be implemented in derived classes.
        """
        raise NotImplementedError

    def calculate_perimeter(self):
        """Calculates and returns the perimeter of the shape.

        This is an abstract method that must be implemented in derived classes.
        """
        raise NotImplementedError

class Circle(Shape):
    # Class constructor
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        # Area of a circle: pi * r^2
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        # Circumference of a circle: 2 * pi * r
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    # Class constructor
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        # Area of a rectangle: length * width
        return self.length * self.width

    def calculate_perimeter(self):
        # Perimeter of a rectangle: 2 * (length + width)
        return 2 * (self.length + self.width)

class Triangle(Shape):
    # Class constructor
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # Area of a triangle (Heron's formula)
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        # Perimeter of a triangle: side1 + side2 + side3
        return self.side1 + self.side2 + self.side3