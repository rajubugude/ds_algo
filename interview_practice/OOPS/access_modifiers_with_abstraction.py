from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount          # Public: Accessible everywhere
        self._status = "Pending"     # Protected: For subclasses
        self.__transaction_id = "TXN001"  # Private: Restricted to Payment

    # Public method
    def get_payment_info(self):
        return f"Amount: {self.amount}, Status: {self._status}, ID: {self.__transaction_id}"

    # Protected method
    def _update_status(self, status):
        self._status = status
        return f"Status updated to {self._status}"

    # Private method
    def __generate_transaction_id(self):
        return f"Transaction-{self.__transaction_id}"

    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number  # Public attribute

    # Implement abstract method (required for abstraction)
    def process_payment(self):
        # Use protected method to update status
        self._update_status("Processed")
        return f"Credit card payment of {self.amount} processed with card ending {self.card_number[-4:]}"

    # Attempt to access private method
    def try_private(self):
        try:
            return self.__generate_transaction_id()  # Will raise AttributeError
        except AttributeError:
            return "Cannot access private __generate_transaction_id"

# Test the example
def main():
    # Cannot instantiate abstract class
    try:
        payment = Payment(100)  # Raises TypeError
    except TypeError:
        print("Cannot instantiate abstract class Payment")

    # Create concrete class instance
    credit_payment = CreditCardPayment(100, "1234567890123456")

    # Access modifiers
    print("\nAccessing attributes:")
    print(credit_payment.amount)        # Public: 100
    print(credit_payment.card_number)   # Public: 1234567890123456
    print(credit_payment._status)       # Protected: Pending (accessible but not recommended)
    try:
        print(credit_payment.__transaction_id)  # Private: Raises AttributeError
    except AttributeError:
        print("Cannot access private __transaction_id")

    # Accessing methods
    print("\nAccessing methods:")
    print(credit_payment.get_payment_info())  # Public: Amount: 100, Status: Pending, ID: TXN001
    print(credit_payment._update_status("Approved"))  # Protected: Status updated to Approved
    print(credit_payment.try_private())  # Cannot access private __generate_transaction_id

    # Abstraction
    print("\nAbstraction:")
    print(credit_payment.process_payment())  # Credit card payment of 100 processed with card ending 3456
    print(credit_payment.get_payment_info())  # Updated status: Amount: 100, Status: Processed, ID: TXN001

if __name__ == "__main__":
    main()