# Lesson 2 - Types
#
# Most languages are "strictly typed" which means
# a variable can only hold one type of information.

# Basic types called primitive types. While the available primitive types
# can vary from language to language they are usually whole numbers, floating
# point numbers, boolean numbers, and *strings
def types():
    # Ints are whole numbers that can be positive or negative
    # In some languages the keyword unsigned can be used to specify
    # if the variable can store negative values. Some languages use
    # specifiers like long and short to specify how much data the value
    # can use
    val1: int = 10

    # Floats are floating point numbers. Some languages have subtypes like
    # decimal which uses a different way of representing the floating point
    # number in memory. Some languages also allow unsigned to be used to designate
    # if a floating point number can store negative values or not.
    #
    # Floating point numbers are very common, especially in game engines, but
    # can be inaccurate due to how they have to be stored and how hardware can
    # handle them. For example 12.5 can actually be 12.49999999999 in some systems.
    # Due to this floating point numbers can accrue errors over time and are generally
    # not good for systems that have to be deterministic.
    val2: float = 12.3

    # Bool or booleans represent values that can only be true or false.
    val3: bool = True

    val4: str = "This is a string. Strings represent a line of textual characters. They are usually " \
                "used to display information, but due to their free form nature are also used to store" \
                "random data (including images and other binary information at times)"

    # If you try to preform an operation like add on values that are
    # do not support adding together like string and bool you will get an
    # exception
    val1 = val4 + val3
    pass


# Types like arrays, lists, maps, and objects are considered complex types. These types are usually
# more complex or larger in size then most primitive types
def complexTypes():
    # Arrays hold a fixed number of elements of the same type. Their main advantage
    # is they are very fast and efficient. Their main issue is they are of a fixed
    # size.
    #
    # A variant of an array is called a list. Unlike arrays that are of fixed size,
    # lists can change their size at run time. This comes at a cost of speed and
    # efficiency
    val1: list = [1, 2, 3, 4, 7]

    # Most languages access elements on a 0 based index.
    print(val1[0])  # Prints 1
    print(val1[2])  # Prints 3

    # Dictionary or maps are a type of collection that hold
    # key value pairs. Unlike lists or arrays values are accessed
    # via the assigned key. This makes them very flexible for data access
    # when you have to care about the actual data you are accessing and can
    # be just as fast as arrays for accessing but require more memory and
    # can be hard to iterate through in some languages
    val2: dict = {"testVal1": 100, "testVal2": 300}

    print(val2["testVal2"])  # Prints 300
    pass


if __name__ == '__main__':
    types()
    complexTypes()
