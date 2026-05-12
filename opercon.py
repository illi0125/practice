''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Conditions
    (3) Logical Operators
'''

print("===== Operators =====")
# + - > >= < <= * == is /   // % += -= **
a = 19
b = 5
print("a > b", a > b)
print("a < b", a < b)
print("a * b", a * b)
print("a / b", a / b)
print("a + b", a + b)
print("a - b", a - b)
print("a >= b", a >= b)
print("a <= b", a <= b)

result = a // b  # whole result
left = a % b  # remainder
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)
print("b**2", b**2)
print("b**3", b**3)

print("="*7)

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c # same reference and value
print("c==d", c == d) # only value not reference
print(id(c), id(d), id(e))

print("c is d", c is d) # different reference
print("c is e", c is e)

print("===== Conditions =====")
x = 15
if x > 50:
  print("Case A")
elif x > 10:
  print("Case B")
else:
  print("Case C")


print("===== Logical Operators =====")
age = 20
# person = None
# if age > 16:
#   person = "adult"
# else:
#   person = "child"

# TERNARY
person = "adult" if age > 18 else "minor"
print("person:", person)

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
  print("Welcome here, do you want to be student!")
elif is_admin:
  print("Please go to that office!")
elif is_guest or is_parent:
  print("Waiting room is over there!")
else:
  print("Other case!")