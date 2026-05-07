print("==== Iterable objects & RANGE ====")
range_obj = range(3)  # [0, 3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")


print("==== DICTIONARY ====")
# Dictionary is JSON object:
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

name = person_obj["name"]
print("name:", name)

# name2 = person_obj["hobby"]
# print("name2:", name2) ERROR

# method: get()
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)  # default value
print(f"the name: {name}, hobby {hobby} and balance: {balance}")

# the reason why dict is iterable
for key in person_obj:
    print(f"the key: {key}")

del person_obj["single"] # removes single state
for key in person_obj:
    print(f"the key: {key}")

for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]}") # or {person_obj.get(key)}