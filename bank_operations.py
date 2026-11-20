from bank import Account, Customer, Bank, BankException, InsufficientFundsException


def withdraw_amount_from_input(acc):
    is_done = False
    while not is_done:
        try:
            print(f'You have: {acc.get_balance()} {acc.currency}')
            withdraw_amount_str = input('Enter withdraw amount: ')
            withdraw_amount = float(withdraw_amount_str)
            if withdraw_amount == 0:
                break
            acc.withdraw(withdraw_amount)
            is_done = True
        except InsufficientFundsException as e:
            print(e)
            print(f'req/avl: {e.amount_req}/{e.amount_avl}')
        except ValueError as e:
            print('The amount provided is invalid')
            # except:
            #    print('Error')
        except BankException as e:
            print(e)


bank = Bank('SGH')
c1 = bank.create_customer('Anne', 'Brown')
a1 = bank.create_account(c1)
a2 = bank.create_account(c1, currency='EUR')
c2 = bank.create_customer('John', 'Doe')
a3 = bank.create_account(c2, currency='USD')
a4 = bank.create_account(c2, currency='EUR')
print(bank)
print('---- deposit/withdraw operations ----')

a3.deposit(400)
a3.withdraw(200)

a1.deposit(200)

withdraw_amount_from_input(a1)

try:
    a3.deposit(400)
    a3.withdraw(200)

    # a = 1414
    # b = '2545'
    # c = a + b
    a1.deposit(200)
    print(f'You have: {a1.get_balance()} {a1.currency}')
    withdraw_amount_str = input('Enter withdraw amount: ')
    withdraw_amount = float(withdraw_amount_str)
    a1.withdraw(withdraw_amount)
    #a1.withdraw(100)
except InsufficientFundsException as e:
    print(e)
    print(f'req/avl: {e.amount_req}/{e.amount_avl}')
except ValueError as e:
    print('The amount provided is invalid')
except BankException as e:
    print(e)
# except:
#    print('Error')
# except Exception as e:  # Don't use it as this will hide every error or bug
#     print(f'SEVERE error {e}')
#     raise e

import sys
#sys.exit(-1000)
print(bank)


