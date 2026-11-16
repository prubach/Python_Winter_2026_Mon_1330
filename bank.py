class Customer:
    last_id = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f"C[{self.id}, {self.first_name}, {self.last_name}]"

class Account:
    last_id = 1000

    def __init__(self, customer, currency='USD'):
        self.customer = customer
        self.currency = currency
        Account.last_id += 1
        self.id = Account.last_id
        self.__balance = 0

    def __repr__(self):
        return f"A[{self.id}, {self.customer.last_name}, {self.__balance} {self.currency}]"

class Bank:
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

    def __repr__(self):
        return f'{self.name} bank[\n{self.cust_list}\n{self.acc_list}]'



#TODO
# add deposit(amount) and withdraw(amount) methods and show how they can be used.
# Take into account different cases/scenarios.