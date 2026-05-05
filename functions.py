''' FUNCTIONS
  (1) DEFINE vs CALL
  (2) Parametr vs Argument
  (3) Keyword & default arguments
  (4) Scope
'''

print("==== DEFINE (parametr) vs CALL (argument) ====")
# build in function > print() type()
# Function - reusable block of code:
# Instead of block {} in JAVA, Python uses indentation!

# DEFINE - build (parametr)


def greet(a):
    print(f"How do yo do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute (argument)
greet("Martin")

result = greet("Leo")  # void function
print("result:", result)

result2 = greeting("Leo")  # return function
print("result2:", result2)


print("==== Keyword & default arguments ====")

# DEFINE


def give_greet(name, age=22):  # default argument
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Justin", age=28)  # keyword argument
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)


print("==== Scope ====")
b = 100 # 3rd priority

def calculate(a, b): # 2nd priority
    c = a * b # 1st priority
    print(f"the c value: {c}")

calculate(5, 50)