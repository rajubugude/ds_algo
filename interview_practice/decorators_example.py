
### Decorators
def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Finished function: {func.__name__}")
    return wrapper

@log_decorator
def greet():
    print("Hello!")

greet()


### Parameterized
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        print("func call start")
        result = func(*args, **kwargs)
        print("func call end")
        return result
    return wrapper

@timing_decorator
def slow_add(a, b):
    return a + b

print(slow_add(3, 4))

def logger(func):
    def abc(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return abc


@logger
def add(a, b):
    return a + b

@logger
def greet(name="Guest"):
    return f"Hello, {name}!"

# Usage
add(10, 20)
greet(name="Raju")

