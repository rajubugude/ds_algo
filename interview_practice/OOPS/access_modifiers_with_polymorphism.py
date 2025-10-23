class Shape:
    def __init__(self, name):
        self.name = name          # Public: Accessible everywhere
        self._color = "Blue"      # Protected: Conventionally for subclasses
        self.__id = "SH001"       # Private: Name-mangled, restricted

    # Public method
    def get_info(self):
        return f"Shape: {self.name}, Color: {self._color}, ID: {self.__id}"

    # Protected method
    def _set_color(self, color):
        self._color = color
        return f"Color set to {self._color}"

    # Private method
    def __generate_id(self):
        return f"ID-{self.__id}"

    # Method for polymorphism
    def draw(self):
        return f"Drawing a generic shape: {self.name}"

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)  # Initialize base class
        self.radius = radius    # Public attribute

    # Override draw method (polymorphism)
    def draw(self):
        return f"Drawing a circle: {self.name} with radius {self.radius}"

    # Access protected method
    def update_color(self, color):
        return self._set_color(color)  # Can access protected method

    # Attempt to access private method
    def try_private(self):
        try:
            return self.__generate_id()  # Will raise AttributeError
        except AttributeError:
            return "Cannot access private __generate_id"

# Test the example
def main():
    shape = Shape("Generic")

    # Access modifiers
    print("Accessing attributes:")
    print(shape.name)          # Public: Generic
    print(shape._color)        # Protected: Blue (accessible but not recommended)
    try:
        print(shape.__id)      # Private: Raises AttributeError
    except AttributeError:
        print("Cannot access private __id")

    print("\nAccessing methods:")
    print(shape.get_info())    # Public: Shape: Generic, Color: Blue, ID: SH001
    print(shape._set_color("Red"))  # Protected: Color set to Red
    try:
        print(shape.__generate_id())  # Private: Raises AttributeError
    except Exception as e:
        print(f"Cannot access private __generate_id: {e}")

    # Circle access
    circle = Circle("Round", 5)
    print("\nCircle access:")
    print(circle.name)         # Public: Round
    print(circle._color)       # Protected: Blue
    print(circle.radius)       # Public: 5
    print(circle.update_color("Green"))  # Protected: Color set to Green
    print(circle.try_private())  # Cannot access private __generate_id

    # Polymorphism
    print("\nPolymorphism:")
    print(shape.draw())   # Shape: Drawing a generic shape: Generic
    print(circle.draw())  # Circle: Drawing a circle: Round with radius 5

if __name__ == "__main__":
    main()