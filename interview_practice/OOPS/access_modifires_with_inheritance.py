class Animal:
    def __init__(self, species):
        self.species = species        # Public: Accessible everywhere
        self._age = 5                # Protected: For subclasses
        self.__id = "ID001"          # Private: Restricted to Animal

    def get_details(self):  # Public method
        return f"Species: {self.species}, Age: {self._age}"

    def _make_sound(self):  # Protected method
        return f"{self.species} makes a sound"

    def __get_id(self):  # Private method
        return f"ID: {self.__id}"

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)  # Inherit from Animal
        self.breed = breed         # Public attribute

    def access_animal_data(self):
        # Access public and protected attributes/methods
        result = f"Dog Breed: {self.breed}, Species: {self.species}, Age: {self._age}"
        result += f", Sound: {self._make_sound()}"
        try:
            result += f", ID: {self.__get_id()}"  # Try accessing private method
        except AttributeError:
            result += ", Cannot access private __get_id"
        return result

# Test access modifiers with inheritance
def main():
    dog = Dog("Canine", "Labrador")

    # Accessing attributes
    print("Accessing attributes:")
    print(dog.species)      # Public: Canine
    print(dog.breed)        # Public: Labrador
    print(dog._age)         # Protected: 5 (accessible but not recommended)
    try:
        print(dog.__id)     # Private: Raises AttributeError
    except AttributeError:
        print("Cannot access private __id")

    # Accessing methods
    print("\nAccessing methods:")
    print(dog.get_details())       # Public: Species: Canine, Age: 5
    print(dog._make_sound())       # Protected: Canine makes a sound
    print(dog.access_animal_data()) # Accesses public/protected, fails on private

if __name__ == "__main__":
    main()