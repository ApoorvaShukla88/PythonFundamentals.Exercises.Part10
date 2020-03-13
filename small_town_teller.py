class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:
   def __init__(self, acc_number, acc_type, owner, balance):
       self.acc_number = acc_number
       self.acc_type = acc_type
       self.owner = owner
       self.balance = balance


class Bank(Person, Account):

        def add_customer(self, id, first_name, last_name):
          self.customer.append(id)
          self.customer.append(first_name)
          self.customer.remove(last_name)

        def add_account(self, acc_number, acc_type, owner):
            self.customer.append(acc_number)
            self.customer.append(acc_type)
            self.customer.append(owner)

        balance = 0

        def deposit(amount):
            global balance
            balance += amount
            return balance

        def withdraw(amount):
            global balance
            balance -= amount
            return balance










