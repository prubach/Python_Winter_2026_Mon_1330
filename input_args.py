import sys
from bank import Bank

print(sys.argv)

bank_name = sys.argv[1] if len(sys.argv) > 1 else 'DEFAULT'

bank = Bank(bank_name)
c1 = bank.create_customer('Anne', 'Brown')
a1 = bank.create_account(c1)
print(bank)