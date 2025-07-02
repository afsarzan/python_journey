name = "Afsar is my name"
# print(name)
# this is comment

print('*' * 20)


def greet(name):
    """Function to greet a person with their name."""
    print(f"Hello, {name}!")


def get_expected_cost(beds, baths):
    value = 80000 + (beds*30000) + (baths * 10000)
    return value


print(get_expected_cost(3, 2))


def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    # round the cost to 2 decimal places
    return round(cost, 2)


print(get_cost(1000, 500, 350, 25))

course  = "python journey"
# String formatting examples
print(course.upper())
print(course.lower())   
print(course.title())
print(course.find("journey"))
print(course.replace("journey", "adventure"))   
print('python' in course)   
print('Python' not in course)  # Check if a substring is not in the string
print(course.split(" "))  # Split the string into a list of words
print(len(course))
print(course.strip())  # Remove leading and trailing whitespace
print(course.lstrip())  # Remove leading whitespace
print(course.rstrip())  # Remove trailing whitespace
print(course.count("p")) # Count occurrences of a character or substring
print(course.startswith("py")) # Check if the string starts with a specific prefix
print(course.endswith("y")) # Check if the string ends with a specific suffix
print(course.find("journey")) # Find the index of a substring
print(course.index("journey")) # Find the index of a substring (raises error if not found)

#numbers in python
x = 10  #integer number
x = 1.1  #float number
x = 1 + 2j # complex number



# number functions
print(abs(-10))  # Absolute value
print(pow(2, 3))  # Power function (2 raised to the power of
# 3)
print(max(1, 2, 3, 4, 5))  # Maximum value
print(min(1, 2, 3, 4, 5))  # Minimum value
print(round(3.14159, 2))  # Round to 2 decimal places   
print(sum([1, 2, 3, 4, 5]))  # Sum of a list of numbers
print(divmod(10, 3))  # Returns a tuple (quotient, remainder)
#use ceiling and floor functions
import math 
print(math.ceil(3.14))  # Ceiling function (rounds up)

print(math.floor(3.14))  # Floor function (rounds down)
# use math functions
print(math.sqrt(16))  # Square root    
print(math.factorial(5))  # Factorial of a number
print(math.gcd(12, 15))  # Greatest common divisor
print(math.lcm(12, 15))  # Least common multiple
# use random module
import random
print(random.randint(1, 10))  # Generate a random integer between 1 and 10
print(random.random())  # Generate a random float between 0 and 1
print(random.choice(['apple', 'banana', 'cherry']))  # Select a random element from a list



#learning control flow
# if-else statements
age = 20
if age >= 18:
    print("You are an adult.")
elif age < 18:
    print("You are a minor.")
else:
    print("Invalid input")

#ternary operator
is_adult = "You are an adult." if age >= 18 else "You are a minor."
print(is_adult) 

#3 logical operators
is_adult = True 
is_student = False
has_job = True
if is_adult and has_job:
    print("You are an adult with a job.")
elif is_adult or is_student:
    print("You are either an adult or a student.")
else:
    print("You are neither an adult nor a student.")    

#chain comparison operators
x = 10
y = 20
if x < y < 30:
    print("x is less than y and y is less than 30.")
else:
    print("At least one condition is false.")

# range step looping
for i in range(0, 10, 2):  # Loop from 0 to 9 with a step of 2
    print(i)

for i in range(0,10):
    if i % 2 == 0:  # Check if the number is even
        print(f"{i} is even")
    elif i % 2 != 0:
        print(f"{i} is odd")

print(type(range(5)))

for x in [1, 2, 3, 4, 5]:
    print(x)

# command = ""
# while command.lower() != "quit":
#     command = input("Enter a command (or 'quit' to exit): ")
#     print(f"You entered: {command}")

#  unpacking list
numbers = [1, 2, 3, 4, 5]
a, b, c, *rest = numbers  # Unpacking with rest
print(f"a: {a}, b: {b}, c: {c}, rest: {rest}")

del numbers[0:2]  # Delete the first two elements
print(f"After deletion: {numbers}")

numbers.sort(reverse=True)  #sort the list in descending order
print(f"Sorted list: {numbers}")

sorted_numbers = sorted(numbers)  #sorted function returns a new sorted list
print(f"Sorted list using sorted(): {sorted_numbers}")

ages = [25, 30, 18, 22, 35];

x =filter(lambda age: age>21,ages)
#count length of the filtered list using len() function
print(f"Number of ages greater than 21: {len(list(x))}")
x = list(x)  # Convert the filter object to a list  
print(f"Filtered ages: {x}")

print([age for age in ages if age > 21])  # List comprehension to filter ages greater than 21

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7]
#add two lists and sort()
print(f"Sorted merged list: {sorted}")  # Merge and sort two lists
#sort combined list
print(sorted(list1 + list2))  # Sort the combined list
print((list1 + list2))  # Concatenate two lists


#dictionaries
point = {"x": 1, "y": 2}
point = dict (x = 1 , y = 2 )
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point ["a"])
print(point.get("a", 0))
del point ["x"]
print(point)
for key in point:
 print(key, point[key])