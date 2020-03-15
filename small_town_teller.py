class Person:
    base_customer_id = 1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.base_customer_id = Person.base_customer_id + 1
        self.id = Person.base_customer_id


class Account:
    def __init__(self, acc_number, acc_type, owner, balance):
        Account.acc_number = Account.acc_number + 1000
        self.acc_number = Account.acc_number
        self.acc_type = acc_type
        self.owner = owner
        self.balance = balance


class Bank:

    def __init__(self):
        self.customers = []
        self.acc_num = []

    def add_customer(self, customer: Person):
        if customer in self.customers:
            print("This person already exists")
        else:
            print(customer.id)
            self.customers.append(customer)


    def add_account(self, account: Account):
        self.acc_num.append(account)

    def remove_acc(self, account: Account):
        self.acc_num.remove(account)

    def deposit(self, amount, account: Account):
        curr_bal = Account.balance
        deposit_bal = curr_bal + amount
        Account.balance = deposit_bal


    def withdraw(self, amount, account: Account):
        curr_bal = Account.balance
        new_bal = curr_bal - amount
        Account.balance = new_bal

    def chk_balance(self, account: Account):
        return Account.balance

def main():
  if __name__ == "__main__":
      main()




zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
print(bob)

# from small_town_teller import Person, Account, Bank
#
# zc_bank = Bank()
# bob = Person(1, "Bob", "Smith")
# zc_bank.add_customer(bob)
# bob_savings = Account(1001, "SAVINGS", bob)
# zc_bank.add_account(bob_savings)
# zc_bank.balance_inquiry(1001)
# # 0
# zc_bank.deposit(1001, 256.02)
# zc_bank.balance_inquiry(1001)
# # 256.02
# zc_bank.withdrawal(1001, 128)
# zc_bank.balance_inquiry(1001)
# # 128.02
