from abc import ABC, abstractmethod

# ------------------ Strategy Pattern ------------------

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI.")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card.")

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

# ------------------ Factory Pattern ------------------

class FoodItem(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def name(self):
        pass

class Burger(FoodItem):
    def prepare(self):
        print("Preparing Burger.")
    def name(self):
        return "Burger"

class Pizza(FoodItem):
    def prepare(self):
        print("Preparing Pizza.")
    def name(self):
        return "Pizza"

# ------------------ Abstract Factory Pattern ------------------

class Drink(ABC):
    @abstractmethod
    def serve(self):
        pass

    @abstractmethod
    def name(self):
        pass

class GarlicBread(Drink):
    def serve(self):
        print("Serving Garlic Bread.")
    def name(self):
        return "Garlic Bread"

class SoftDrink(Drink):
    def serve(self):
        print("Serving Soft Drink.")
    def name(self):
        return "Soft Drink"

class MealFactory(ABC):
    @abstractmethod
    def create_main(self) -> FoodItem:
        pass

    @abstractmethod
    def create_side(self) -> Drink:
        pass

class BurgerMealFactory(MealFactory):
    def create_main(self):
        return Burger()

    def create_side(self):
        return GarlicBread()

class PizzaMealFactory(MealFactory):
    def create_main(self):
        return Pizza()

    def create_side(self):
        return SoftDrink()

# ------------------ Singleton Pattern ------------------

class OrderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderManager, cls).__new__(cls)
            cls._instance.orders = []
        return cls._instance

    def add_order(self, item_name):
        self.orders.append(item_name)

    def show_orders(self):
        print("\n All Orders So Far:")
        for i, item in enumerate(self.orders):
            print(f"{i+1}. {item}")

# ------------------ Client Code ------------------

def prepare_meal(factory: MealFactory, payment_strategy: PaymentStrategy, amount: int):
    main = factory.create_main()
    side = factory.create_side()

    main.prepare()
    side.serve()

    # Log to Singleton OrderManager
    order_manager = OrderManager()
    order_manager.add_order(main.name())
    order_manager.add_order(side.name())

    # Process payment
    processor = PaymentProcessor(payment_strategy)
    processor.process_payment(amount)

# ------------------ Usage ------------------

print("Burger Meal with UPI Payment:")
prepare_meal(BurgerMealFactory(), UpiPayment(), 250)

print("\nPizza Meal with Credit Card Payment:")
prepare_meal(PizzaMealFactory(), CreditCardPayment(), 400)

# Show all orders
OrderManager().show_orders()
