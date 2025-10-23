### Abstract Factory.

from abc import ABC, abstractmethod

# Abstract Product: Burger
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass
# Abstract Product: Garlic Bread
class GarlicBread(ABC):
    @abstractmethod
    def bake(self):
        pass

# Concrete Burgers
class WheatBurger(Burger):
    def prepare(self):
        print("Preparing a healthy Wheat Burger.")

class NormalBurger(Burger):
    def prepare(self):
        print("Preparing a classic Normal Burger.")

# Concrete Garlic Breads
class WheatGarlicBread(GarlicBread):
    def bake(self):
        print("Baking Wheat Garlic Bread.")

class NormalGarlicBread(GarlicBread):
    def bake(self):
        print("Baking Normal Garlic Bread.")


# Abstract Factory
class MealFactory(ABC):
    @abstractmethod
    def create_burger(self) -> Burger:
        pass

    @abstractmethod
    def create_garlic_bread(self) -> GarlicBread:
        pass

# Concrete Factory: Wheat Meal
class WheatMealFactory(MealFactory):
    def create_burger(self) -> Burger:
        return WheatBurger()

    def create_garlic_bread(self) -> GarlicBread:
        return WheatGarlicBread()

# Concrete Factory: Normal Meal
class NormalMealFactory(MealFactory):
    def create_burger(self) -> Burger:
        return NormalBurger()

    def create_garlic_bread(self) -> GarlicBread:
        return NormalGarlicBread()

# Client Code
def prepare_meal(factory: MealFactory):
    burger = factory.create_burger()
    garlic_bread = factory.create_garlic_bread()

    burger.prepare()
    garlic_bread.bake()

# Usage
print("Wheat Meal:")
prepare_meal(WheatMealFactory())

print("\nNormal Meal:")
prepare_meal(NormalMealFactory())



