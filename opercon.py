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