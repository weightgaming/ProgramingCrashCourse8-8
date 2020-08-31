# Lesson 5 - Classes
#
# Classes (also know as custom Types) are a way to organize more complex data
# into reusable packages. Classes can contain 2 general categories of data,
# properties which store data, and methods which define actions the class can
# preform. Classes can then be used to create versions of itself called "objects"
# when the program runs.
#
# It should be noted, most languages allow to to specify the access levels of properties
# and methods. Private is used to say the property or method is only available to that class,
# protected says that the property or method is available to only that class and classes that
# inherit from it, and finally public says the property or method is available to everyone.
#
# Unfortunately this feature is not in python and instead naming conventions are used to communicate
# intent. "_" in front of a property or method is usually used to communicate that it is private or
# protected and really should not be messed with.

# This is a basic class
class BasicClass:
    # This class contains 2 properties, one an int and the other a float
    _var1: int
    _var2: float

    # This portion is called a constructor. Constructors are called when you
    # create an object from a class and is usually used to setup initial data
    # in the class. In most languages constructors are usually a method that
    # uses the classes name, for example in C# it would be
    # "Public BasicClass(int var1, float var2)". Python uses the
    # a keyword instead. The main purpose of constructors.
    def __init__(self, var1: int, var2: float):
        self._var1 = var1
        self._var2 = var2

    # This is a destructor. Destructors are special methods that get called
    # when an object is deleted from memory. The point of a destructor is to
    # clean up anything that may need to be cleaned up or preform some action
    # when the object is removed such as tracing. This is very important
    # when you deal with more advanced I/O operations as a file handle or
    # database connection may need to be manually closed or it may corrupt
    # the file or screw with the data base. In general, unless in C++, you
    # do not use these much as the use cases for them are mainly handled by
    # what is called a "Garbage Collector" in most modern languages.
    def __del__(self):
        print(str(self.Sum()) + ' has been deleted')

    # This is a method. A Method is just a function that is contained in an class.
    # This method takes var1 and adds it to var2 and returns the result.
    def Sum(self) -> float:
        return self._var1 + self._var2


if __name__ == '__main__':
    # Calling a classes constructor will create a new object from that class.
    # In most C like languages the keyword new usually needs to be before the call
    # but this rule is a bit more loose among general languages
    bc: BasicClass = BasicClass(10, 12.3)
    print(bc.Sum())

    # Objects are automatically deleted when no more references to them exist, but
    # most languages allow for explict deletion through a delete keyword. Most C like
    # languages just use the keyword "delete" but python uses "del". You need to be
    # careful though as if you try to call bc.Sum() again after deleting it you will
    # get a crash for it being undefined.
    del bc
