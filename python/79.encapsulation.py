class BankAccount:
    def __init__(self, name, balance):
        self.name = name            # Public
        self.__balance = balance    # Private

    # Getter (to read private balance)
    def get_balance(self):
        return self.__balance

    # Setter (to update private balance safely)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

    def show_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.__balance}")

# Creating object
acc = BankAccount("Nisha", 5000)

# Accessing public member
print(acc.name)

# Accessing private member (via method)
print(acc.get_balance())  # ✅ Safe access

# Trying to access private directly (❌)
# print(acc.__balance)    # ❌ Will raise an error

# Using methods to modify data
acc.deposit(1000)
acc.withdraw(300)

# Final status
acc.show_details()
