''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLYMORPHISM
'''

print("==== ENCAPSULATION ====")
'''
C++ JAVA > public private protected
PHP Typescript > public private protected
Python > public __private _protected
'''


class Account():
    # state
    description = "This class makes bank accounts"
    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount
    # method

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner
    
    @holder.setter
    def holder(self, new_owner):
        print("holder.seter:", new_owner)
        self.__owner = new_owner
    
    def change_ownership(self, new_owner):
        print("change_ownership", new_owner)
        self.__owner = new_owner


my_account = Account("Leo", 2000)
my_account.get_balance()
print("=======")
my_account.deposit(4000)
my_account.withdraw(500)
my_account.get_balance()

print("=======")
my_account.amount = 1000000
my_account.owner = "Martin"
my_account.amount = 10000000
my_account.get_balance()

print("=======")
try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found", err)

print("==== getter vs setter ====")
print("owner before:", my_account.holder) # state due to decorator
print("=======")
# my_account.change_ownership("Martin")
my_account.holder = "Martin" # state due to decorator
print("owner after:", my_account.holder)