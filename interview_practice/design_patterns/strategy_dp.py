
### Strategy DP.

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"amount: {amount} paid through creditcard")

class UPIPaymentStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"amount: {amount} paid through UPI")


class ConcretePayment:
    def __init__(self, paymentStrategy = None):
        self.paymentStrategy = paymentStrategy

    def set_strategy(self, paymentStrategy):
        self.paymentStrategy = paymentStrategy

    def payamount(self, amount):
        if self.paymentStrategy is None:
            return "Set payment strategy first"
        self.paymentStrategy.pay(amount)


# Usage
payement_obj = ConcretePayment()
payement_obj.set_strategy(CreditCardPaymentStrategy())
payement_obj.payamount(100)

payement_obj.set_strategy(UPIPaymentStrategy())
payement_obj.payamount(200)


'''
🧠 Strategy Pattern: Not more inheritance, prefer composition.
Purpose:
Encapsulates algorithms or behaviors and lets you switch between them at runtime.

Use When:

You have multiple ways to perform a task (e.g., payment via UPI, credit card, etc.).
You want to change behavior dynamically without modifying the context class.
    You want to follow Open/Closed Principle — add new strategies without changing existing code.
How to Think:

"I need to perform an action, but the way it's done can vary. Let me define a family of interchangeable behaviors."

Example:

Payment methods
Sorting algorithms
Compression strategies

🧠 Decision Guide
If you're choosing how something is done → use Strategy.
If you're choosing what object to create → use Factory.
If you're creating families of related objects → use Abstract Factory.
'''