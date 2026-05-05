# Dunder __builtins__, __init__
print("Hello World!")

message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print(result)

''' In Python, there are builtin tools:
  (1) TYPES > int float str list dict
  (2) FUNCTIONS > print() len() input() type()
  (3) CONSTANTS > True False None
'''

print(dir(__builtins__))
