"""
    多态
"""


class Animal:

    def say(self):
        pass


class Dog(Animal):

    def say(self):
        print("汪汪")


class Cat(Animal):

    def say(self):
        print("喵喵")


def say_something(animal):
    animal.say()


dog = Dog()
cat = Cat()
say_something(dog)
say_something(cat)
