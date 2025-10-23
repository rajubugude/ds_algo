import contextlib

@contextlib.contextmanager
def my_custom_context():
    print("Entering the context")
    yield  # Code within the 'with' block executes here
    print("Exiting the context")

with my_custom_context():
    print("Inside the context")


'''
Context managers achieve this by implementing two special methods:
Context managers in Python are objects designed to manage resources, ensuring they are properly acquired and released,
 even in the presence of errors. They are primarily used with the with statement, which provides a convenient and safe 
 way to handle setup and teardown operations.

__enter__(self): This method is called when the with statement is entered. 
    It typically performs setup operations and can return a value that is assigned to the as variable in the with 
    statement (e.g., with open('file.txt') as f:).
__exit__(self, exc_type, exc_val, exc_tb): This method is called when the with block is exited, 
    regardless of whether an exception occurred. It handles cleanup operations. 
    The arguments exc_type, exc_val, and exc_tb provide information about any exception that was raised within the with
     block. If this method returns a truthy value, it suppresses the exception.
'''
with open('example.txt', 'w') as file:
    file.write('This is a test.')
# The file is automatically closed here, even if an error occurred during writing.


class ContextManager:
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

with FileManager('test.txt', 'w') as f:
    f.write('Test')
print(f.closed)