# W8D3 - Object-Oriented Programming - Part 2: Shape Class Hierarchy Project

This project showcases a simple class hierarchy to model and calculate properties of various geometric shapes using object-oriented programming (OOP) principles emphasizing inheritance, polymorphism, and abstraction.

## Project Goals

- Illustrate the core concepts of OOP in a clear and concise manner.
- Provide a reusable and extensible framework for representing different shapes.
- Calculate and display the area and perimeter of various shapes using specialized methods.

## Key OOP Concepts

### Inheritance:

- The foundation of this hierarchy is the Shape class, which acts as a blueprint for all shapes. It defines common attributes like color and outlines the methods each shape should have: calculate_area and calculate_perimeter.

- Concrete shape classes like Circle, Rectangle, and Triangle inherit from Shape. They inherit the color attribute and are responsible for providing the area and perimeter calculations.

### Polymorphism:

- Polymorphism is evident in the calculate_area and calculate_perimeter methods. These methods exist in both the parent Shape class and the child shape classes. However, each child class tailors these methods to calculate the values according to its unique geometric properties.

- This means you can have a list of different shapes and call the same method on each, getting the correct result based on the actual shape type, without needing to write conditional logic.

### Abstraction:

- The Shape class uses abstraction. It provides a high-level representation of what a shape is, focusing on its essential characteristics and behaviors.

- It doesn't get bogged down in the specifics of how each shape calculates its properties. That responsibility is delegated to the derived classes, which are the experts on their particular geometries.

## Project Structure

### The project is organized into two files:

#### shapes.py:  

- This file contains the definitions of all the classes used in the project. You'll find the Shape base class along with the derived classes: Circle, Rectangle, and Triangle. Each class defines its attributes (e.g., radius for a circle) and the methods to calculate its area and perimeter.

#### main.py: 

- This file serves as the entry point of the program. It demonstrates how to use the classes defined in shapes.py. It creates instances of different shapes, stores them in a list, and then iterates over the list to calculate and print the area and perimeter of each shape.

### How to Run

- Make sure you have Python installed. Then, from your terminal or command prompt, navigate to the directory containing this README and the code files, and run this command in your terminal (Your python command may be python, or simply py, etc depending on your operating system and dev environment setup.):

```python3 main.py```

### This will produce output similar to:

```
red Circle:
  Area: 78.54
  Perimeter: 31.42
--------------------
blue Rectangle:
  Area: 24.00
  Perimeter: 20.00
--------------------
green Triangle:
  Area: 6.00
  Perimeter: 12.00
--------------------
```
**Accreditation Notes:**

- I used Google Gemini Advanced to help me debug some of the traceback calls that I could not solve using online resources in addition to the course materials such as Stack Overflow, and to help me with the details for this readme file and the documentation. It also helped me with the math formulas.

- I use Stack Overflow & W3 Schools as a resource in most of my coding, mostly to help understand what is happening in the terminal errors when I cannot find the information in the course materials.