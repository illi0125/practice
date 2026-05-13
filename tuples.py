''' Tuple
    (1) What is tuple: tuple vs list
    (2) Unpacking arguments
    (3) zip
'''

print("====== What is tuple: tuple vs list ======")
# Java/PHP/NpdeJS array => Python list

# literal
numbs = [3, 5, 7, 9]
car_dict = {"brand": "Ferrari", "year": 2026}
print(numbs)

# constructor
letters = list("Hello World!")
person_obj = dict(name="Martin", age=35)
print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruiits:", fruits)

# we cannot mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)
print(animals[0])
# animals[0] = "bird" error




print("====== Unpacking arguments ======")
# try avoid this 
people = "Andrew", "John"
animals = "dog",

# groups = ["MIT", "FLEXY", "DEVEX", "MG"]
# (x, y, z, a) = groups
# print(f"the x: {x} and y: {y}")

groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z) # list


# *args > tuple
def calculate(*args):
  print("*args", args)
  total = 1
  for x in args:
    total *= x
  print(f"the total value: {total}")
  return total
calculate(1, 7, 2, 3)
print("------------")
calculate(0, 2, 300)
print("------------")
calculate(2, 300)