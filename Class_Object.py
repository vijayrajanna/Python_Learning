class Person:
    pass #empty block

personObject = Person()
print(personObject)

#################################################

class Human:
    def sayHi(self, name):
        print "I'm human",
        print ' My name is {}'.format(name)

humanObject = Human()
humanObject.sayHi("Vijay Rajanna")

#################################################

# Creating a new object field
# in the below function both name and home are object fields
# both objects get their own fields

class HumanWithName:

    TotalNumberHumans = 0
    def __init__(self,myname):
        self.name = myname
        self.home = "Sringeri"
        HumanWithName.TotalNumberHumans += 1

    def sayHi(self):
        print "I'm human and my name is {}".format(self.name)
        print('I come from a place called {}'.format(self.home))

    @classmethod #This is a class method, similar to static class, no need of object creation
    def howManyHumans(cls):
        print('There are total of {} Humans'.format(cls.TotalNumberHumans))


humanObjectName1 = HumanWithName("Vijay Rajanna")
humanObjectName1.sayHi()

humanObjectName2 = HumanWithName("Vijay Rajanna")
humanObjectName2.name = "Vinay Rajanna" #reassigning name
humanObjectName2.home = "Texas"
humanObjectName2.sayHi()

HumanWithName.howManyHumans()
print HumanWithName.TotalNumberHumans

#################################################