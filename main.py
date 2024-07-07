"""
    This script demonstrates the usage of the Shape class hierarchy. It creates instances
    of different shapes (Circle, Rectangle, Triangle), stores them in a list, and then
    calculates and displays the area and perimeter of each shape.

    Key Points:
    - Imports necessary classes from the `shapes` module.
    - Creates a list of shape objects with different colors and dimensions.
    - Iterates through the list of shapes.
    - Prints the color, type, area, and perimeter of each shape.

    How to Run:
    - Make sure you have Python installed.
    - From the terminal/command prompt, run `python3 main.py` in the same directory as this file
    and `shapes.py`. (Your python command may be python, or simply py, etc depending on your operating system and dev environment setup.)
"""

from shapes import Circle, Rectangle, Triangle

shapes = [
    Circle("red", 5),
    Rectangle("blue", 4, 6),
    Triangle("green", 3, 4, 5)
]

for shape in shapes:
    print(f"{shape.color} {type(shape).__name__}:") # Print shape details
    print(f"  Area: {shape.calculate_area():.2f}")
    print(f"  Perimeter: {shape.calculate_perimeter():.2f}")
    print("-" * 20) # Visual separator