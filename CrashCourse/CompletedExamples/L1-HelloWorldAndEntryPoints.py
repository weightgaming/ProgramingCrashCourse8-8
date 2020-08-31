# Lesson 1 - Hello world and entry points
#
# All languages have an "entry point"
# An entry point is where the program begins execution
# "Main" is a common keyword used to specify the entry point
#
# Common C style entry points:
# int main()
# {
#   return 0;
# }
# or
# void main()
# {
# }

# Hello World is a common and simple IO program to test a language
# and teach very basic concepts like console I/O
def helloWorld():
    print("Hello World")


if __name__ == '__main__':
    helloWorld()