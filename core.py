class TagCloud:
    def __init__(self):
        self.tags = {}
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    def __iter__(self):
        return iter(self.tags.items())

cloud = TagCloud()
# cloud["python"]
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")

print(cloud.tags)
print(cloud["python"])  # Accessing the tag count
print(cloud["java"])    # Accessing a tag that doesn't exist, should return 0

# Setting a tag count
cloud["java"] = 5 
print(cloud["java"])  # Now accessing the tag count for "java" should return 5
# Adding more tags
cloud.add("Java")
cloud.add("JavaScript") 
cloud.add("JavaScript")
print(cloud.tags)  # Display all tags and their counts

# Iterating through the tags
for tag, count in cloud:
    print(f"{tag}: {count}")

#using properties
class Product:
    def __init__(self, price):
        self.set_price(price)
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

product = Product(100)
print(product.price)  # Accessing the price using the property
product.price = 150  # Setting a new price using the property
print(product.price)  # Accessing the updated price
product.price = -50  # Uncommenting this line will raise a ValueError
