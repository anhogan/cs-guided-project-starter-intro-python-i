# Can parameters be any data type?
  # Assuming only type int and str are passed in

# What if a decimal is passed in?
  # If a string, convert to int and round ... otherwise round

# What about negative numbers?
  # Handle as an edge case and return an error

# Who is passing in paramters? A user? Or is it generated?
  # Assuming user input

# How do we want to handle the int and string combo?
  # Problem states to return none

# if both str, convert to int and return sum
# elif both either int or float, convert to string and concat ... round float
# else, if they don't match, return None

def stupid_addition(a, b):
    if (isinstance(a, str) and isinstance(b, str)):
      return int(a) + int(b)
    elif ((isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float))):
      return str(round(a)) + str(round(b))
    else:
      return 'None'

print(stupid_addition(1,2))
print(stupid_addition('1','2'))
print(stupid_addition(1,'2'))
print(stupid_addition(1.3,2.7))