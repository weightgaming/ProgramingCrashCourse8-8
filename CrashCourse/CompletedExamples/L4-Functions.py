# Lesson 4 - Functions
#
# Functions allow you to combine instructions into reusable
# calls. The calls can take no to as many arguments as you may like
# and return or not return values. Procedure or Subroutine is sometimes
# used to describe functions that return no value where the term function
# is usually almost always used to describe functions that return a value.
# Technically though all the terms are interchangeable.
#
# Functions are a very important concept as they help to prevent duplication of code,
# which makes coding much faster as well as making maintenance much easier over time.

# This function simply prints the below statement. It takes no arguments and returns
# no value
def printMessage():
    print('This is a function that prints this string and takes no arguments.')


# This function takes one argument that it then appends hello to and prints
def sayHello(name: str):
    print('Hello ' + name)


# This function takes one value and returns that value * itself
def square(value: float) -> float:
    return value * value


# You can also take multiple arguments and return a completely different type
def equals(value1: int, value2: int) -> bool:
    return value1 == value2


# Some functions can change what is passed into them. Whether or not an argument
# can be changed depends if they are mutable or immutable in python or in most other
# languages if they where passed by value or by reference. Arguments passed by value
# (known as Immutable in python) make a new copy of that value when passed into a function.
# This means modifying this value has no risk of modifying the original.
#
# Arguments passed by reference (known as mutable in python) do not make a copy of themselves
# but instead refer to the original. This means that changing these types of arguments will
# change the value ot the original.
#
# In general, most modern languages will base primitive types by value and complex types like
# collections and objects by reference. Though it should be noted that this is not always true
# and some languages like C/C++ force you to specify when something is by reference or allow
# you the option to explicit specify how an argument should be passed like in C#.
#
# This method below uses a list which is a mutable collection in python so any changes done to
# the list in this function will persist into the original list
def fuckWithTheList(value: list):
    value[0] = -1
    value[len(value)-1] = -1000


if __name__ == '__main__':
    printMessage()

    sayHello('Everyone!')

    print(square(5))

    print(equals(1, 3))

    testList: list = [55, 33, 11234, 11, 0]
    print(testList)
    fuckWithTheList(testList)
    print(testList)