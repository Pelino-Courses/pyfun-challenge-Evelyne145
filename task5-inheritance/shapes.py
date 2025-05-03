import math

class Shape:
    """
    The base class for all shapes.

    This is like a template — it defines what all shapes should be able to do,
    like calculating area and perimeter. Specific shapes will fill in the details.
    """

    def area(self):
        """Calculate the area. (Every shape will do this differently.)"""
        raise NotImplementedError("Oops! This shape hasn't told us how to calculate area yet.")

    def perimeter(self):
        """Calculate the perimeter. (Every shape will do this differently.)"""
        raise NotImplementedError("Oops! This shape hasn't told us how to calculate perimeter yet.")

    def __str__(self):
        return "A generic shape."


class Circle(Shape):
    """A lovely circle, defined by its radius."""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero. No negative circles allowed!")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"A circle with radius {self.radius}"


class Rectangle(Shape):
    """A trusty rectangle, defined by width and height."""

    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Both width and height must be positive. You can’t have a flat rectangle!")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"A rectangle ({self.width} x {self.height})"


class Square(Rectangle):
    """A perfect square — just a rectangle with all sides equal."""

    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side length must be positive. A square needs real sides!")
        super().__init__(side, side)

    def __str__(self):
        return f"A square with side {self.width}"


class Triangle(Shape):
    """
    A triangle, defined by three sides.

    We use Heron's formula to calculate the area.
    """

    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive. No stick-figure triangles allowed.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("These sides can't make a triangle. The sum of any two sides must be greater than the third.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2  # semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"A triangle with sides {self.a}, {self.b}, {self.c}"


# Try it out — runs only if you run this file directly
if __name__ == "__main__":
    print("🔷 Let's explore some shapes!")

    shapes = [
        Circle(5),
        Rectangle(3, 4),
        Square(6),
        Triangle(3, 4, 5)
    ]

    for shape in shapes:
        print(f"\n👉 {shape}")
        print(f"   Area: {shape.area():.2f}")
        print(f"   Perimeter: {shape.perimeter():.2f}")