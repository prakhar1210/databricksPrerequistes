# def my_name():
#     name = input("What is your name? ")
#     print(f"Hello, {name}!")

# my_name()

# lambda_function = lambda x: x * 2
# print(lambda_function(5))  # Output: 10


# Class and objects

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")      

# p1 = Person("John", 30)
# p1.greet()  # Output: Hello, my name is John and I am

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")

p1 = Dog("Buddy", 3)
p1.bark()  # Output: Buddy says Woof!
    

