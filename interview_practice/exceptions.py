# print(4//0)
try:
    print(4 // 0)
except ZeroDivisionError as e:
    print(f"some issue : {e}")

class MyCustomException(Exception):
    """Custom exception for unavailable menu items."""
    def __init__(self, msg=None):
        self.msg = msg
        super().__init__(msg)

def place_order_without_crash(item):
    """
    Returns a message or an exception object if the item is not available.
    Does not raise the exception.
    """
    if item not in ["burger", "pizza"]:
        return MyCustomException(f"'{item}' is not available on the menu.")
    return f"Order placed for {item}."

def place_order_with_crash(item):
    """
    Raises a custom exception if the item is not available.
    """
    if item not in ["burger", "pizza"]:
        raise MyCustomException(f"'{item}' is not available on the menu.")
    return f"Order placed for {item}."



if __name__ == "__main__":
    # Testing without crash
    result1 = place_order_without_crash("pasta")
    print(result1)
    print("Type check:", type(result1))

    result2 = place_order_without_crash("burger")
    print(result2)
    print("Type check:", type(result2))

    # Testing with crash
    # # Individual ordering.
    try:
        print(place_order_with_crash("pizza"))  # Valid order
        print(place_order_with_crash("pasta"))  # Raises exception
        print(place_order_with_crash("burger")) # from here it won't execute, becoz it goes to below except block.
    except MyCustomException as e:
        print(f"Custom error caught: {e}")

    # # Now every order will execute. using loop
    items = ["pizza", "pasta", "burger"]
    for item in items:
        try:
            print(place_order_with_crash(item))
        except MyCustomException as e:
            print(f"Custom error caught for '{item}': {e}")



### With logging.
#
# import logging
#
# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
#
# class MyCustomException(Exception):
#     """Custom exception for unavailable menu items."""
#     def __init__(self, msg=None):
#         self.msg = msg
#         super().__init__(msg)
#
# def place_order_without_crash(item):
#     """
#     Returns a message or an exception object if the item is not available.
#     Does not raise the exception.
#     """
#     if item not in ["burger", "pizza"]:
#         logging.warning(f"Attempted to order unavailable item: {item}")
#         return MyCustomException(f"'{item}' is not available on the menu.")
#     logging.info(f"Order placed successfully for: {item}")
#     return f"Order placed for {item}."
#
# def place_order_with_crash(item):
#     """
#     Raises a custom exception if the item is not available.
#     """
#     if item not in ["burger", "pizza"]:
#         logging.error(f"Invalid order attempt: {item}")
#         raise MyCustomException(f"'{item}' is not available on the menu.")
#     logging.info(f"Order placed successfully for: {item}")
#     return f"Order placed for {item}."
#
# if __name__ == "__main__":
#     # Testing without crash
#     result1 = place_order_without_crash("pasta")
#     print(result1)
#     print("Type check:", type(result1))
#
#     result2 = place_order_without_crash("burger")
#     print(result2)
#     print("Type check:", type(result2))
#
#     # Testing with crash
#     try:
#         print(place_order_with_crash("pizza"))  # Valid order
#         print(place_order_with_crash("pasta"))  # Raises exception
#     except MyCustomException as e:
#         print(f"Custom error caught: {e}")
