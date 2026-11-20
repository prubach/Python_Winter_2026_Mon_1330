from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(200))
    email = Column(String(300))
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), nullable=False)
    bank = relationship('Bank', lazy='select', back_populates='cust_list')
    accounts = relationship('Account', back_populates='customer')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"C[{self.id}, {self.first_name}, {self.last_name}]"

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float)
    currency = Column(String(3))
    yearly_interest_rate = Column(Float) # TODO - will be used to update the interest rate

    fk_bank_id = Column(Integer, ForeignKey('bank.id'), nullable=False)
    bank = relationship('Bank', lazy='select', back_populates='acc_list')
    fk_customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    customer = relationship(Customer, lazy='select', back_populates='accounts')

    def __init__(self, customer, currency='USD'):
        self.customer = customer
        self.currency = currency
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount: int):
        if amount > 0:
            # TODO: currency mismatch
            self.balance += amount
        else:
            raise InvalidAmountException(f"Invalid value {amount}")
            print("Invalid value.")

    def withdraw(self, amount: int):
        if amount <= 0:
            raise InvalidAmountException(f"Invalid value {amount}")
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsException(f"Insufficient funds requested/available {amount}/{self.balance}", amount, self.balance)

    # def deposit(self, amount):
    #     if amount <= 0:
    #         raise ValueError("Deposit amount must be greater than zero.")
    #     self.__balance += amount
    #     return self.__balance
    #
    # def withdraw(self, amount):
    #     if amount <= 0:
    #         raise ValueError("Withdrawal amount must be greater than zero.")
    #     if amount > self.__balance:
    #         raise ValueError("Insufficient funds for withdrawal.")
    #     self.__balance -= amount
    #     return self.__balance

    def __repr__(self):
        return f"A[{self.id}, {self.customer.last_name}, {self.balance} {self.currency}]"

class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    cust_list = relationship(Customer, back_populates='bank')
    acc_list = relationship(Account, back_populates='bank')

    def __init__(self, name):
        self.name = name
        self.cust_list = []
        self.acc_list = []

    def create_customer(self, first_name, last_name):
        customer = Customer(first_name, last_name)
        self.cust_list.append(customer)
        return customer

    def create_account(self, customer, currency = 'USD'):
        account = Account(customer, currency)
        self.acc_list.append(account)
        return account

    def transfer_money(self, from_account_id, to_account_id, amount):
        # TODO - as part of the home assignment please implement this method - as names suggest the input parameters are
        # ids of the accounts to transfer money from and to and amount to transfer. You may need a helper method to find
        # those accounts based on their ids.
        pass

    def run_daily_interest_updater(self):
        # TODO - as part of the home assignment please implement this method
        pass

    def __repr__(self):
        return f'{self.name} bank[\n{self.cust_list}\n{self.acc_list}]'


class BankException(Exception):
    pass

class InvalidAmountException(BankException):
    pass

class InsufficientFundsException(BankException):
    def __init__(self, message, amount_req, amount_avl):
        super().__init__(message)
        self.amount_req = amount_req
        self.amount_avl = amount_avl






#TODO
# add deposit(amount) and withdraw(amount) methods and show how they can be used.
# Take into account different cases/scenarios.