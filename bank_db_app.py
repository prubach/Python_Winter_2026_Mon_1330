from bank_models import *

db = DBSession().db_session()

def add_data():
    bank = Bank('SGH')
    db.add(bank)
    c1 = bank.create_customer('Anne', 'Brown')
    db.add(c1)
    a1 = bank.create_account(c1)
    a2 = bank.create_account(c1, currency='EUR')
    db.add(a1)
    db.add(a2)
    c2 = bank.create_customer('John', 'Doe')
    db.add(c2)
    a3 = bank.create_account(c2, currency='USD')
    a4 = bank.create_account(c2, currency='EUR')
    db.add(a3)
    db.add(a4)





if __name__ == '__main__':
    #init_db()
    add_data()
    db.commit()