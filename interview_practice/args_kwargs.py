def add(*args):
    return sum(args)

print(add(1,2,3))


def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Raju", role="Engineer", location="Bengaluru")


def demo_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo_function(1, 2, 3, name="Raju", job="Engineer")


## 4. Forwarding arguments to another function

def greet(name, greeting):
    print(f"{greeting}, {name}!")

def wrapper(*args, **kwargs):
    greet(*args, **kwargs)

wrapper("Raju", greeting="Hi")


## 5. Default values with **kwargs
def connect_to_db(**kwargs):
    host = kwargs.get("host", "localhost")
    port = kwargs.get("port", 3306)
    print(f"Connecting to {host}:{port}")

connect_to_db(host="192.168.1.1")


### 6. Unpacking lists and dicts into functions

def show_details(name, age):
    print(f"{name} is {age} years old.")

data = ("Raju", 30)
show_details(*data)

info = {"name": "Raju", "age": 30}
show_details(**info)


### 7. Restricting arguments after *args
def example(*args, keyword_only=None):
    print("Args:", args)
    print("Keyword-only:", keyword_only)

example(1, 2, keyword_only="Only via keyword")


### Method Overloading - Compile time polymorphism simulation using python.

class Greeter:
    def greet(self, *args, **kwargs):
        if args and kwargs:
            print(f"Hello {args[0]}, you are a {kwargs.get('role')}")
        elif args:
            print(f"Hello {args[0]}")
        elif kwargs:
            print(f"Hello {kwargs.get('name')}, your role is {kwargs.get('role')}")
        else:
            print("Hello, Guest!")

# Usage
g = Greeter()
g.greet()  # No arguments
g.greet("Raju")  # Positional only
g.greet(name="Raju", role="Engineer")  # Keyword only
g.greet("Raju", role="Engineer")  # Mixed
