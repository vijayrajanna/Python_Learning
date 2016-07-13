import sys
from sys import modules
print('The command line arguments are')
for i in sys.argv:
    print(i)
print(sys.api_version)
print(sys.version)
print(sys.byteorder)
print(sys.copyright)
print(sys.path)
print(modules)
