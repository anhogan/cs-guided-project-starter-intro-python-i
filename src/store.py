class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return f"{self.name} costs ${self.price}"

class Department:
  # Products are a tuple with signature(str, int) because tuples are immutable
  def __init__(self, name, products=[]):
    self.name = name
    self.products = [Product(p[0], p[1]) for p in products]
    # Same as Product(*p)

  def __str__(self):
    return f"The {self.name} department has {len(self.products)} products"

class Store:
  def __init__(self, name, location, departments):
    self.name = name
    self.location = location
    self.departments = [Department(d) for d in departments]

  def __str__(self):
    return f"Store {self.name}, {self.location}, {self.departments}"

store = Store('Lambda Store', 'San Francisco', ['Clothing', 'Cookware', 'Sporting Goods', 'Electronics', 'Home and Office'])

# While loop allows continuous inputs until a specific exit is specified
while True:
  # Handle user input
  selection = input("Select the number of a department or type 'exit' to leave: ")

  # Break out of the loop
  if selection == 'exit':
    print('Thanks for shopping with us!')
    break

  # How Python handles error handling
  try:
    # Cast selection into an int() ... might cause an error which we handle before
    selection = int(selection)
    if selection >= len(store.departments):
      print("That's not a valid department")
    elif selection >=0 and selection < len(store.departments):
      print("The user selected: " + store.departments[selection])
    else:
      # Negative number input
      print("Department numbers are positive")
  except ValueError:
    # User didn't give a valid input
    print("Please enter your choice as a number")