import Cython

# Learning how to use Cython

# Create a new list 'a' with modified elements
a = [x + 1 for x in range(9)]
b = a[:]  # Create a copy of 'a' to avoid modifying 'b'
a[3] = 49.0
assert b[3] == 4  # Check that 'b[3]' is still 4

# Reassign 'a' to an integer (which is not a list)
a = 10
assert not isinstance(a, list)  # Verify that 'a' is no longer a list
assert isinstance(b, list)

# Declare Cython variables
cdef int my_int
cdef float my_float

# Perform some operations
my_int = 0
my_float = 12.0
result = 2 * my_float

assert my_int != result  # Check that 'my_int' and 'result' are different


# function pointer
#cdef int (*signal(int (*f)(int)(int))(int))


def autoInfer():
    a = 1
    b = 2.0
    c = 3 + 4j
    r = a * b + c
    return r
    
'''
@cython.infer_types(True)
    def inferDec():
        a = 1
        b = 2.0
        c = 3 + 4j
        r = a * b + c
        return r
'''