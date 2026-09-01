"""
Exercise 06: Class usage
TODO: Define Rectangle with __init__(self, width, height) and area(self).
      area() must return width * height.
"""


class Rectangle:
    def __init__(self, width, height):
        # TODO: set self.width and self.height
        pass

    def area(self):
        # TODO: return width * height
        pass


def main() -> None:
    rectangle = Rectangle(3, 4)
    print(rectangle.area())


if __name__ == "__main__":
    main()
