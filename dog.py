class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name

# Driver code
# Object instantiation
Kaga = Dog("Kaga")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Kaga is a {}".format(Kaga.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Kaga.name))
print("My name is {}".format(Tommy.name))
class Phone:
    def __init__(self, phoneName, model, owner): 
        self.phoneName = phoneName                 
        self.model = model
        self.owner = owner

    def makecall(self):
        print("Iphone is making call")

    def sendMsg(self):
        print("Iphone receives and sends messages")


iphone14 = Phone("Apple Iphone", "Iphone14 Pro Max", "Tola")

iphone14.makecall()
iphone14.sendMsg()

print("the phone name is  {}".format(iphone14.phoneName))
print("The phone model is   {}".format(iphone14.model))
print("The phone owner is   {}".format(iphone14.owner))
