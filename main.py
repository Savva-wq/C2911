class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.is_sleeping = False

    def sleep(self):
        if not self.is_sleeping:
            print(f"{self.name} is now sleeping.")
            self.is_sleeping = True
        else:
            print(f"{self.name} is already sleeping.")

    def wake_up(self):
        if self.is_sleeping:
            print(f"{self.name} woke up.")
            self.is_sleeping = False
        else:
            print(f"{self.name} is already awake.")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def meow(self):
        print(f"{self.name} says: Meow!")

my_cat = Cat("Whiskers", 5, "gray")

my_cat.sleep()
my_cat.sleep()
my_cat.wake_up()
my_cat.eat("fish")
my_cat.meow()