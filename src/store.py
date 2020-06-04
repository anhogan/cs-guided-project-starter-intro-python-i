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
    self.products = products
    # Same as Product(*p)

  def __str__(self):
    return f"Welcome to the {self.name} department"

  def add_product(self, product, price):
    self.products.append(Product(product, price))

  def print_products(self):
    for p in self.products:
      print(p)

class Store:
  def __init__(self, name, location, departments):
    self.name = name
    self.location = location
    self.departments = [Department(department_name, department_products) for department_name, department_products in departments.items()]

  def __str__(self):
    return f"Store {self.name}, {self.location}, {self.departments}"

  def print_products(self):
    for d in self.departments:
      d.print_products()

  def print_departments(self):
    for d in self.departments:
      print(d)

products_and_departments = {
  "Clothing": [Product("Sneakers", 100)],
  "Cookware": [Product("Cast Iron Fishing Pan", 30), Product("Non Stick Frying Pan", 25)],
  "Sporting Goods": [Product("Golf Club Set", 350), Product("Basketball", 30)],
  "Electronics": [Product("Nintendo Switch", 300)],
  "Home and Office": [Product("Notebook", 2)]
}

store = Store('Lambda Store', 'San Francisco', products_and_departments)

store.print_products()
store.print_departments()

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