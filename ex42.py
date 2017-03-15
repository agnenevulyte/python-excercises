## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self):
        pass

    def valgyti(self, maistas):
        print "Gyvunas paziuri i %s." % maistas
        if maistas == "desra" or maistas == "bybys":
            print "Gyvunas patenkintas."
        else:
            print "Gyvunas praso desros."
        return

## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## class Dog has-a __init__ that takes self and name parameters
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes self and name parameters
        self.name = name

## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        ## Employee has-a name????????????????????????????
        ## Turejo buti: Return a proxy object that delegates method calls to a parent or sibling class of type.
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halinut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary get the pet attribute and set it to satan. so satan is-a pet and mary has-a pet
## turejo buti: pet attribute of mary is-a sat
mary.pet = satan

## frank is-a Employee and franks has-a 120000
## turejo buti: frank is-a Employee instance
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover. so rover is-a pet and frank has-a pet
## turejo buti: pet attribute of frank is-a rover
frank.pet = rover

## set flipper to an instance of class Fish. flipper is-a Fish
## turejo buti: flipper is-a Fish instance
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## Harry is-a Halibut instance
harry = Halibut()