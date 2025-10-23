

### Factory DSP

from abc import ABC, abstractmethod
# Step 1: Define the Product Interface
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Step 2: Create Concrete Products
class WheatBurger(Burger):
    def prepare(self):
        print("Preparing a healthy Wheat Burger.")

class NormalBurger(Burger):
    def prepare(self):
        print("Preparing a classic Normal Burger.")

# Step 3: Create the Factory
class BurgerFactory:
    @staticmethod
    def create_burger(burger_type):
        if burger_type == "wheat":
            return WheatBurger()
        elif burger_type == "normal":
            return NormalBurger()
        else:
            return f"Unknown burger type: {burger_type}"

# # Step 4: Usage
burger1 = BurgerFactory.create_burger("wheat")
burger1.prepare()

burger2 = BurgerFactory.create_burger("normal")
burger2.prepare()


'''
🏭 Factory Pattern
Purpose:
Encapsulates object creation logic and returns instances based on input or configuration.

Use When:

You want to hide the instantiation logic from the client.
You need to create objects based on conditions (e.g., burger type).
You want to centralize and simplify object creation.
How to Think:

"I need an object, but I don't want the client to know or care about which class to instantiate."

Example:

Creating UI components (Button, Checkbox)
Creating different types of burgers or database connections
🧩 Abstract Factory Pattern
Purpose:
Creates families of related objects (e.g., burger + garlic bread) without specifying concrete classes.

Use When:

You need to create multiple related objects together.
You want to ensure consistency across product families.
'''