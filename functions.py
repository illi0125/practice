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
