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

p1.age = 5
print(f"{p1.name} is now {p1.age} years old.")  # Output: Buddy is now 5 years old.

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


# Create a class Student with an __init__ that takes name and grade, and stores them as properties
# Create an object s1 with name "Anna" and grade "A"
# Print the grade of s1
# Change the grade of s1 to "B"
# Print the updated grade

class Student:
   def __init__(self, name, grade):
      self.name = name
      self.grade = grade

s1 = Student("Anna", "A")
print(s1.grade)  # Output: A

s1.grade = "B"
print(s1.grade)  # Output: B 

# inharitance

# Inside the editor, complete the following steps:
# Create a parent class Animal with an __init__ that takes name
# Add a method speak that prints the name
# Create a child class Dog that inherits from Animal
# Create an object d1 = Dog("Rex")
# Call d1.speak()


class Animal:
    def __init__(self, name):
        self.name = name

    # def speak(self):
    #     print(f"My name is {self.name}")


class Dog(Animal):
     def speak(self):
            print(f"My name is {self.name}")


d1 = Dog("Rex")
d1.speak()

d2 = Dog("Warner")
d2.speak()

print("PLYMORPHISM")

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


#   Encapsulation

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

print("encapsulation with private attributes")

# Inside the editor, complete the following steps:
# Create a class ScoreBoard
# Add an __init__ with a score parameter and store it as a private attribute
# Add a method called get_score that returns the private score
# Create an object s1 with a score of 0
# Print the score of s1

class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

s1 = ScoreBoard(10)
print(s1.get_score())