class Person:
    def __init__(self, name):
        self.name = name
        self.dog = None

    def adopt_dog(self, dog):
        self.dog = dog
        print(f"{self.name} adopted a dog named {dog.name}.")

    def walk_dog(self):
        if self.dog is not None:
            print(f"{self.name} is walking with {self.dog.name}.")
        else:
            print(f"{self.name} doesn't have a dog to walk.")

    def feed_dog(self):
        if self.dog is not None:
            print(f"{self.name} is feeding {self.dog.name}.")
        else:
            print(f"{self.name} doesn't have a dog to feed.")


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

person = Person("John")
dog = Dog("Max", "Labrador")

person.adopt_dog(dog)
person.walk_dog()
person.feed_dog()
dog.bark()