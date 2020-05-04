from abc import ABC, abstractmethod

# wrong
class A:
    @abstractmethod
    def do_something(self):
        print("Hi")
# a = A()
# a.do_something() # it prints 'Hi'

# correct
class A(ABC):
    @abstractmethod
    def do_something(self):
        print("Hi")

#a = A()
#a.do_something() # it calls the error

class B(A):
    def do_something_else(self):
        print("Something else")

    def do_something(self):
        print("Hi there...")

b = B()
b.do_something_else()
b.do_something()
