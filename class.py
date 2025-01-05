from function import numbers

class RotateList:
    def __init__(self):
        self.numbers = numbers
    def rotateList(self):
        return self.numbers[::-1]

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)