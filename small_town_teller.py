import PersistenceUtils
from typing import Dict
import pickle


class Person:
    base_customer_id = 1

    def __init__(self, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, acc_number, acc_type, owner):
        self.acc_number = Account.acc_number
        self.acc_type = acc_type
        self.owner = owner
        self.balance = 0


class Bank:

    def __init__(self):
        self.customers = []
        self.acc_num = []

    def add_customer(self, customer: Person):
        if customer.id in self.customers:
            raise ValueError(f"Customer with id {customer.id} already exists.")
        else:
            self.customers[customer.id] = customer

    def add_account(self, account: Account):
        if account.owner.id not in self.acc_num:
            raise ValueError("Invalid user")
        elif Account.acc_number in self.acc_num:
            raise ValueError("Account number already exists")
        else:
            self.acc_num[Account.acc_number] = Account


    def remove_acc(self, account: Account):
        self.acc_num.remove(Account.acc_number)

    def deposit(self, amount, account: Account):
        curr_bal = Account.balance
        Account.balance = curr_bal + amount

    def withdraw(self, amount, account: Account):
        curr_bal = Account.balance
        Account.balance = curr_bal - amount

    def chk_balance(self, account: Account):
        return Account.balance



