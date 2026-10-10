
# Topic 1: Type Conversion

age = input("Enter your age: ")
new_age = int(age) + 1
print("Next year, your age will be:", new_age)


# Topic 2: Sum of Two Numbers

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print("Sum is:", a + b)


# Topic 3: String Methods

name = "arham"

# Convert string to uppercase
print(name.upper())

# Find the index of a character
print(name.find("a"))  # Output: 0

# Replace text
print(name.replace("arham", "khan"))
print(name)  # Original string remains unchanged

# Check whether a character exists
print("a" in name)  # True


# Topic 4: Practice Exercise 2

# Take prices of three products
product_1 = float(input("Enter Product 1 price: "))
product_2 = float(input("Enter Product 2 price: "))
product_3 = float(input("Enter Product 3 price: "))

# Calculate total and average
total_amount = product_1 + product_2 + product_3
average_price = total_amount / 3

print("Total bill amount:", round(total_amount, 2))
print("Average product price:", round(average_price, 2))


# Check whether superhero name starts with S or s
superhero_name = input("Enter your superhero name: ")

if superhero_name.startswith(("S", "s")):
    print("Your superhero name starts with S!")
else:
    print("Your superhero name does not start with S.")
