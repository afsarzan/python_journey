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