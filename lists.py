''' LIST
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumarate, map and filter
'''

print("====== Working with lists ======")
# Java/PHP/NpdeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Leo")  # tuple
groups = ["MIT", "FLEXY", "MG"]  # list
for team in groups:
    print(f"the team: {team}")

# constructor
letters = list("Hello World1!")
print(f"the letters: {letters} and size: {len(letters)}")

print("---------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]  # jumps 3 times
d = fruits[::-1]  # reverse

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
