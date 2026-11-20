from bank import Account, Customer, Bank, BankException, InsufficientFundsException

bank = Bank('SGH')
c1 = bank.create_customer('Anne', 'Brown')
a1 = bank.create_account(c1)
a2 = bank.create_account(c1, currency='EUR')
c2 = bank.create_customer('John', 'Doe')
a3 = bank.create_account(c2, currency='USD')
a4 = bank.create_account(c2, currency='EUR')
print(bank)
print('---- deposit/withdraw operations ----')
try:
    a3.deposit(400)
    a3.withdraw(200)

    a1.deposit(200)
    print(f'You have: {a1.get_balance()} {a1.currency}')
    withdraw_amount_str = input('Enter withdraw amount: ')
    withdraw_amount = float(withdraw_amount_str)
    a1.withdraw(withdraw_amount)
    #a1.withdraw(100)

except InsufficientFundsException as e:
    print(e)
    print(f'req/avl: {e.amount_req}/{e.amount_avl}')

#except:
#    print('Error')
except BankException as e:
    print(e)

import sys
#sys.exit(-1000)
print(bank)

