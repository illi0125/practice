''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITANCE <
    (3) POLYMORPHISM <
'''

print("==== INHERITANCE ====")
# PARENT > CHILD
# Parent inherits only public & protected properties(state + method) for children


class Animal():  # Parent
    # state
    description = "The class is parent for animals"
    # constuctor

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice
    # method

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")

# DOG


class Dog(Animal):  # Child
    # state
    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect home!")

    def make_voice(self):
        print(f"the {self.name} says: {self.sound}")

# CAT


class Cat(Animal):  # Child
    # state
    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass

# FISH


class Fish(Animal):  # Child
    # state
    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound
    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("=====")  # inherits from parent
dog.make_voice()
cat.make_voice()
fish.make_voice()

print("=====")
print(Animal.description)
print(Dog.description)
print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)


print("==== POLYMORPHISM ====")

dog.make_voice()
cat.make_voice()
fish.make_voice()

print("=====")
# Fish > Fish > Animal > Object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)