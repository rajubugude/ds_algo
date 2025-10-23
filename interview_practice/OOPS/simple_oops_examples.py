
class Bikes:
    __wheels = 2
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self): # if we print obj, then the below string will return.
        return f"Bike has {Bikes.__wheels} wheels, it is {self.make} and model is {self.model}"


### obj or class both can change/modify the class attributes
obj = Bikes('Royal Enfield', 'himalayan450')
print(obj)


### ENCAPSULATION

# Encapsulation Example
class Bike:
    def __init__(self, make, model):
        self._make = make  # Encapsulated attribute
        self._model = model  # Encapsulated attribute

    def get_make(self):  # Getter method
        return self._make

    def get_model(self):  # Getter method
        return self._model

    def set_make(self, make):  # Setter method
        self._make = make

    def set_model(self, model):  # Setter method
        self._model = model


my_bike = Bike("Honda", "Shine")
print(my_bike.get_make())  # Output: Honda
my_bike.set_make("Hero")
print(my_bike.get_make())  # Output: Hero


### Abstraction

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """Abstract base class for all payment methods."""

    @abstractmethod
    def pay(self, amount):
        """Process the payment of a given amount."""
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing credit card payment of ₹{amount}")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing PayPal payment of ₹{amount}")

# Usage
def process_payment(payment_method: PaymentMethod, amount: float):
    payment_method.pay(amount)

# Example calls
process_payment(CreditCardPayment(), 1500)
process_payment(PayPalPayment(), 2000)


### Inheritance

class Animal:
    def __init__(self, species):
        self.species = species
    
    def eat(self):
        return "animal is eating"

    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, species):
        self.name = name
        super().__init__(species)
        
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("lab", "Canine")
print(dog.sound())  # Output: Woof!
print(dog.eat())  # Output: animal is eating
cat = Cat("Feline")
print(cat.sound())  # Output: Meow!


### Polymorphism

# Polymorphism Example
class Animal:
    def sound(self):
        return "Animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

animal = Animal()
print(make_sound(animal))  # Output: Animal sound
dog = Dog()
print(make_sound(dog))  # Output: Woof!
cat = Cat()
print(make_sound(cat))  # Output: Meow!