__author__ = 'Vijay'

def printer(message):
    print message

printer('hello world')

#-----------------------------------------

def print_max(a, b):
    if a > b:
        print a, 'is maximum'
    elif a == b:
        print a, 'is equal to', b
    else:
        print b, 'is maximum'

# directly pass literal values
print_max(3, 4)
#----------------------------------------------

x = 50
def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

func(x)
print 'x is still', x

#---------------------------------------------

x = 70
def funcglobal():
    global x
    print 'x is', x
    x = 2
    print 'Changed global x to', x

funcglobal()
print 'Value of x is', x