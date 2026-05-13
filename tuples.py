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