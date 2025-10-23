#Design Patterns Python.

### Singleton.

## Normal singleton.

class Singleton:
    _instance = None
    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

def create_instance():
    instance = Singleton.get_instance()
    print(f"Instance ID: {id(instance)}")


# Usage
singleton_instance1 = create_instance()
singleton_instance2 = create_instance()
print(singleton_instance1, singleton_instance2)
print(singleton_instance1==singleton_instance2)




#to simulate to see the issue that threads can create mutliple instances, even though class is singleton.

# import threading
# import time
#
# class Singleton:
#     _instance = None
#
#     def __init__(self):
#         time.sleep(0.01)  # Simulate delay
#
#     @staticmethod
#     def get_instance():
#         if Singleton._instance is None:
#             Singleton._instance = Singleton()
#         return Singleton._instance
#
# def create_instance():
#     instance = Singleton.get_instance()
#     print(f"Instance ID: {id(instance)}")
#
# threads = []
# for _ in range(100):
#     t = threading.Thread(target=create_instance)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()


# # thread safe singleton

import threading
import time
class SingletonThreadsafe:
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        time.sleep(0.01)

    @staticmethod
    def get_instance():
        if SingletonThreadsafe._instance is None:
            with SingletonThreadsafe._lock:
                if SingletonThreadsafe._instance is None:
                    SingletonThreadsafe._instance = SingletonThreadsafe()
        return SingletonThreadsafe._instance

def create_instance():
    instance = SingletonThreadsafe.get_instance()
    print(f"Instance ID: {id(instance)}")


threads = []
for _ in range(100):
    t = threading.Thread(target=create_instance)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
