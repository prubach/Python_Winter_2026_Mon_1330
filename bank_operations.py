from bank import Account, Customer, Bank

bank = Bank('SGH')
c1 = bank.create_customer('Anne', 'Brown')
a1 = bank.create_account(c1)
a2 = bank.create_account(c1, currency='EUR')
c2 = bank.create_customer('John', 'Doe')
a3 = bank.create_account(c2, currency='USD')
a4 = bank.create_account(c2, currency='EUR')
print(bank)
print('---- deposit/withdraw operations ----')
a1.deposit(200)
a3.deposit(400)
a1.withdraw(100)
#a3.withdraw('500')
import sys
sys.exit(-1000)
print(bank)

