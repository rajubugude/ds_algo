class Laptop:
    def __init__(self, model):
        self.model = model            # Public: Accessible everywhere
        self._processor = "Intel i5"  # Protected: Conventionally internal
        self.__serial = "SN12345"     # Private: Name-mangled, restricted

    def get_specs(self):  # Public method
        return f"Model: {self.model}, Processor: {self._processor}"

    def _upgrade_processor(self):  # Protected method
        return f"Upgrading processor to {self._processor}"

    def __get_serial(self):  # Private method
        return f"Serial: {self.__serial}"

# Test access modifiers
def main():
    laptop = Laptop("Dell XPS")

    # Accessing attributes
    print("Accessing attributes:")
    print(laptop.model)          # Public: Dell XPS
    print(laptop._processor)     # Protected: Intel i5 (accessible but not recommended)
    try:
        print(laptop.__serial)   # Private: Raises AttributeError
    except AttributeError:
        print("Cannot access private __serial")

    # Accessing methods
    print("\nAccessing methods:")
    print(laptop.get_specs())    # Public: Model: Dell XPS, Processor: Intel i5
    print(laptop._upgrade_processor())  # Protected: Upgrading processor to Intel i5
    try:
        print(laptop.__get_serial())  # Private: Raises AttributeError
    except AttributeError:
        print("Cannot access private __get_serial")

if __name__ == "__main__":
    main()