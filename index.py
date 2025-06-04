name = "Afsar is my name"
# print(name)
# this is comment


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