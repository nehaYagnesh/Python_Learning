""" Example to create a class,object and method """
# class PartyAnimal:
#     x = 0

#     # Declaring a method name party
#     def party(self):
#         self.x = self.x + 1
#         print(self.x)

# # Creating an object/instance for PartyAnimal
# an = PartyAnimal()

# # Consuming the method of PartyAnimal.
# # Here due to self the statement below will be equivalent to PartyAnimal.party(an)
# an.party()
# an.party()
# an.party()
# print('Type:',type(an))
# print('Dir:',dir(an))

""" dir() and type()
dir() command lists capabilities
type() tells us the type of the variable """
# x = list()
# print(type(x))
# print(dir(x))


""" Object Lifecycle 
* Objects are created,used and discarded
* We have special blocks of code(methods) that get called 
     1. At the moment of creation(constructor)
     2. At the moment of destruction(destructor)
* Constructors are used a lot
* Destructors are seldom used

CONSTRUCTOR : The primary purpose of the constructor is to set up
some instance variables to have the proper initial values when the object is created

Note: Constructor and destructor are optional. The constructor is typically used to set up variables.
"""
# class PartyAnimal:
#     x = 0

#     def __init__(self):
#         print('I am constructed')
    
#     def party(self):
#         self.x = self.x + 1
#         print('So far',self.x)
    
#     def __del__(self):
#         print('I am destructed',self.x)

# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains',an)


""" Constructor in a class is a special block of statements called
when an object is created """

""" Many Instances
1. We can create lot of objects - the class is the template for the object
2. We can store each distinct object in its own variable
3. We call this having multiple instances of the same class
4. Each instance has its own copy of the instance variables 

Constructors can have additional parameters. These can be used to set 
up instance variables for the particular instance of the class
(i.e., for the particular object) """

# class PartyAnimal:
#     x = 0
#     name = ''
#     def __init__(self,z):
#         self.name = z
#         print(self.name,'constructed')
    
#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)
    
# a = PartyAnimal('Sally')
# a.party()

# b = PartyAnimal('Nick')
# b.party()
# a.party()


""" Inheritance 
1. When we make a new class - we can reuse an existing class 
and inherit all the capabitilies of an existing class and then 
add our own little bit to make our new class
2. Another form of store and reuse
3. Write once - reuse many times
4. The new class (child) has all the capabilities of the old class(parent)
and then some more

'Subclasses' are more specialized version of a class, which inherit
attributes and behaviour from their parent classes, and can introduce their own
 """
# class PartyAnimal():
#     x = 0 
#     name = ''

#     def __init__(self,nam):
#         self.name = nam
#         print(self.name,'constructed')

#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)

# class FootballFan(PartyAnimal):
#     points = 0
#     def touchdown(self):
#         self.points = self.points + 7
#         self.party()
#         print(self.name,'points',self.points)

# s = PartyAnimal('Sally')
# s.party()

# j = FootballFan('Jim')
# j.party()
# j.touchdown()


""" Definitions

1. Class => A template
2. Attribute => A variable within a class
3. Method => A function within a class
4. Object => A particular instance of a class
5. Constructor => Code that runs when an object is created
6. Inheritance => The ability to extend a class to make a new class
"""
