num = int(21)

if((num%2) == 0):
    print("Even")
else:
    print("odd")


    # largest of the three numbers

a = 10
b = 20
c = 30  

if(a >= b) and (a >= c):
    largest = a
elif(b >= a) and (b >= c):
    largest = b
else:
    largest = c

print("The largest number is:", largest)


# reverse a  string
string = "Hello World"
reversed_string = string[::-1]
print("The reversed string is:", reversed_string)

# count vowels in a string
string = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("The number of vowels in the string is:", count)

# find the sum of elements in a list
numbers = [1, 2, 3, 4, 5]   
total = sum(numbers)    
print("The sum of the elements in the list is:", total)

# collections in python

# counter in python

from collections import Counter 
  
# Creating Counter from a list (sequence of items)  
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# Creating Counter from a dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
  
# Creating Counter using keyword arguments
print(Counter(A=3, B=5, C=2))

print(Counter("hello world"))


# dictionary in python

user = {
    "name": "Prakhar",
    "role": "Developer",
    "experience": 4
}

print(user["name"])  # Output: Prakhar


user["skill"] = "Python"  # Adding a new key-value pair
print(user)  # Output: {'name': 'Prakhar', 'role': '