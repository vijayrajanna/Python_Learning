_Author_ = 'Vijay Rajanna'

# An example program show function scopes.

x = 50

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

func(x) # This is equivalent to pass by value

print 'x is still', x

# The below X is the same X that you have created above with value x = 50
# Even if you understand that it is a different X, that is not a problem.

x = 20
print 'Global x now changed to', x

# ---------------------------------------------------------------------
# An important thing to remember about the scope of variables in python.
# You can directly access a global variable inside a function, i.e., as shown below 'p' is accessed
# inside of the 'accessvariable' function.
# However, if you update that variable "p=124" you are not working with the global(original variable), but you created
# a local variable P (same name as global variable), and you update the local variable, the
# global variable remains unchanged.
# ---------------------------------------------------------------------

P = 123
def accessvariable():
    print 'p is', P   # printing value of global variable
    #P = 124   # Now, this is not a global variable, you have created a local "p"
accessvariable()

print 'Since I changed the value of P to 124 inside the function, the new value of P is: {}'.format(P)

# ---------------------------------------------------------------------
# To fix the above error, to make P, a global variable accessible inside function accessvariable, and update
# the global variable, use term keyword 'global'
# ---------------------------------------------------------------------

def accessvariableglobal():
    global P
    P = 136 # changing the value of global P
    print 'Changed value of p is', P # updated global P value
    P = 137  # Updating global P again
accessvariableglobal()

print 'Since I changed the value of P to 137 inside the function, the new value of P is: {}'.format(P)

# ---------------------------
# Example to show the return value from function feature.
# ---------------------------

def retunvalu():
    return 3, 4, 5

first, second, third =  retunvalu()

print 'After Calling function\
the value of first is {}, second is {}, and third is {}'.format(first,second,third)